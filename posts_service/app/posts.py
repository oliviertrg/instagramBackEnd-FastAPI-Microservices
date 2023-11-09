from fastapi import FastAPI ,Response,status ,HTTPException,APIRouter,Depends, Request,BackgroundTasks
from app import auth2,schema
import requests
import json
from datetime import datetime
from app.config import csd
import uuid
import random
import string
import aiohttp
import asyncio
from kafka import KafkaProducer
KAFKA_TOPIC = "UPDATE_NUMBERS_OF_POSTS"

# producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9093'],
#                          api_version=(0,11,5))

producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9093'],
                         api_version=(0,11,5),
                         security_protocol = "SASL_PLAINTEXT",
                         sasl_mechanisms = "SCRAM-SHA-512",
                         sasl_username = "my_username",
                         sasl_password = "my_password")

# "security_protocol": "SASL_PLAINTEXT",
#     "sasl_mechanisms": "SCRAM-SHA-512",
#     "sasl_username": "my_username",
#     "sasl_password": "my_password"
router = APIRouter (
    prefix = "/api/v1/web/posts",
    tags = ["posts"]
)

@router.get("/{post_id}/views/")
async def view(post_id:str,current_users : int = Depends(auth2.get_current_user)):
    try :

        my_headers =  {'Authorization' : f'Bearer {current_users.access_token}'}

        async with aiohttp.ClientSession() as sessionn:
          async with sessionn.get(f'http://host.docker.internal:7778/api/v1/web/comments/{post_id}/views/',
                                 headers=my_headers) as response:
          
            response_data = await response.json()
          async with sessionn.get(f'http://host.docker.internal:7782/api/v1/web/likes/{post_id}/views/',
                                 headers=my_headers) as resp:
          
            resp_data = await resp.json()  

        # x = {"data-1":str(session),"testing":f"done{post_id}"} 
        # x.update(response_data)
        # x.update(resp_data)

        session = csd() 
        i = session.execute(f""" select * from posts.posts where post_id = {post_id};""")
        x = schema.posts(
            user_id=str(i[0][0]),
            posts_id=post_id,
            caption=i[0][2],
            imgage_url = i[0][4],
            create_at=str(i[0][3]),
            likes =  resp_data,
            comments = response_data
         
        ).dict()
        
        print(x)
        session.shutdown()

    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    
    return x
    
def post_producer(user_id:int):
    session = csd()
    y = session.execute(f"""select count(post_id) from posts.posts where user_id = {user_id} ;""")
    body = {"total_posts":f"{y[0][0]}","user_id" : f"{user_id}"}
    print(body)   
    d = (json.dumps(body).encode("utf-8"))
    producer.send(KAFKA_TOPIC,d)

@router.post("/add/")
async def posting(new_posts : schema.posts,background_tasks: BackgroundTasks,current_users : int = Depends(auth2.get_current_user)):
    try:      
        new_posts.user_id = current_users.id
        new_posts.posts_id = uuid.uuid4()
        new_posts.create_at = datetime.now()

        
        session = csd() 
        x = session.execute(f"""INSERT INTO posts.posts (user_id,post_id,caption,create_at ,image_url)
                        VALUES ({new_posts.user_id},{new_posts.posts_id},
                        '{new_posts.caption}', '{new_posts.create_at}',
                        '{new_posts.imgage_url}') ;
                                """)
        background_tasks.add_task(post_producer,new_posts.user_id)
        # y = session.execute(f"""select count(post_id) from posts.posts where user_id = {new_posts.user_id} ;""")
        # body = {"total_posts":f"{y[0][0]}","user_id" : f"{new_posts.user_id}"}   
        # d = (json.dumps(body).encode("utf-8"))
        # producer.send(ORDER_KAFKA_TOPIC,d)
        

    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    return new_posts

@router.delete("/{post_id}/detele/")
async def delete_post(post_id: str,current_users : int = Depends(auth2.get_current_user)):
   try : 

    session = csd() 
    x = tuple(session.execute(f'''SELECT * FROM posts.posts 
                        WHERE post_id = {post_id} ; '''))
    if len(x) != 0:
           
        if int(current_users.id) == int(x[0][0]) :

            session.execute(f'''DELETE FROM posts.posts
                            WHERE post_id = {post_id} ; ''')
        else :

            return Response(status_code=status.HTTP_403_FORBIDDEN,
                                    content={"detail":"Not authorized to perform requested action "})
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
 
   except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action") 
    
   return Response(status_code=status.HTTP_204_NO_CONTENT) 

    
   


