from fastapi import FastAPI ,Response,status ,HTTPException,APIRouter,Depends, Request
from app import auth2,schema
import requests
import json
from datetime import datetime
from app.config import csd
import uuid
import random
import string




# ORDER_KAFKA_TOPIC = "transactions_details"

# producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9300'],
#                          api_version=(0,11,5))
  

router = APIRouter (
    prefix = "/api/v1/web/posts",
    tags = ["posts"]
)


@router.get("/{post_id}/views/")
async def view(post_id:str,current_users : int = Depends(auth2.get_current_user)):
    try :
        session = csd()
        print(session)
        my_headers =  {'Authorization' : f'Bearer {current_users.access_token}'}
        # await requests.get(f'http://host.docker.internal:7778/api/v1/web/comments/{post_id}/views/', headers=my_headers)
        req = requests.get(f'http://host.docker.internal:7778/api/v1/web/comments/{post_id}/views/', headers=my_headers)
        response_data = req.json()
        print(response_data)
        # print(response_data.json())
        # print(type(response_data.json()))
        x = {"data-1":str(session),"testing":f"done{post_id}"} 
        x.update(response_data)
        print(x)
        session.shutdown()


        # my_dict = {
        #     "name": "Bard",
        #     "age": 1,
        #     "hobbies": ["coding", "reading", "playing games"],
        #     "address": {
        #         "street": "123 Main Street",
        #         "city": "San Francisco",
        #         "state": "CA",
        #         "zip": "94105"
        #     }
        # }

        # json_string = json.dumps(my_dict)

        # print(json_string)

        # import aiohttp

        # async def main():
        #     async with aiohttp.ClientSession() as session:
        #         async with session.get('https://example.com/') as response:
        #             response_data = await response.json()
        #             print(response_data)

        # if __name__ == '__main__':
        #     asyncio.run(main())
        # x = (
        #     schema.comments(
        #     id=str(i[0]),
        #     post_id=i[4],
        #     author=i[1],
        #     comment=i[2],
        #     user_id=i[6],
        #     created_at=str(i[3]),
        #     thread_id=str(i[5])
        # ).dict()
        # for (i) in session.execute(f"""SELECT * from comment.photo_comments WHERE post_id  = '{post_id}';""") )
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    
    return x

@router.post("/{post_id}/add/")
async def test(post_id: str,comments : schema.comments,current_users : int = Depends(auth2.get_current_user)):
    try:      
        comments.user_id = 'xxx'
        comments.author = current_users.id
        comments.created_at = datetime.now()
        comments.post_id = post_id
        comments.id = uuid.uuid4()
        comments.thread_id = uuid.uuid4()
        
        session = csd() 
        x = session.execute(f'''INSERT INTO comment.photo_comments (id,post_id,user_id,comment,author,thread_id,create_at)
                        VALUES ({comments.id},'{post_id}','{comments.user_id}', '{comments.comment}',
                        '{comments.author}',{comments.thread_id},'{comments.created_at}') ;
                                ''')

    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    return comments

@router.delete("/{comment_id}/detele/")
async def test(comment_id: str,current_users : int = Depends(auth2.get_current_user)):
   try : 

    session = csd() 

    session.execute(f'''DELETE FROM comment.photo_comments
                        WHERE id = {comment_id} ; ''')
   except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action") 
    
   return Response(status_code=status.HTTP_204_NO_CONTENT) 


