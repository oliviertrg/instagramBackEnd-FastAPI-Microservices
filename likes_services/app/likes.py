from fastapi import FastAPI ,Response,status ,HTTPException,APIRouter,Depends, Request
from app import auth2,schema
import requests
import json
from datetime import datetime
from app.config import curso
import uuid
import random
import string




# ORDER_KAFKA_TOPIC = "transactions_details"

# producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9300'],
#                          api_version=(0,11,5))
  

router = APIRouter (
    prefix = "/api/v1/web/likes",
    tags = ["likes"]
)


@router.get("/{post_id}/views/")
async def view(post_id:str,current_users : int = Depends(auth2.get_current_user)):
    try :
        db = curso()
        c = db.cursor()
 
        sql = (f'''SELECT * FROM "likes" where "post_id" = '{post_id}' ;''')
        c.execute(sql)
        l = c.fetchall()
        db.close()
        # x = (
        #     schema.likes(
        #     post_id=i[0],
        #     user_id=i[1],
        #     created_at=str(i[2]),
            
        # ).dict()
        # for (i) in session.execute(f"""SELECT * FROM post_likes.likes  WHERE post_id  = '{post_id}';""") 
        #     )
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
         # x = (
        #     schema.likes(
        #     post_id=i[0],
        #     user_id=i[1],
        #     created_at=str(i[2]),
            
        # ).dict()
        # for (i) in session.execute(f"""SELECT * FROM post_likes.likes  WHERE post_id  = '{post_id}';""") 
        #     )
    return {"data":l} 

@router.post("/{post_id}/like/")
async def test(post_id: str,current_users : int = Depends(auth2.get_current_user)):
    try:
        x = schema.likes(      
        user_id = str(current_users.id),
        created_at = str(datetime.now()),
        post_id = post_id     
        ).dict()   
    
        session = csd() 
        # x = session.execute(f"""SELECT count(user_id) FROM post_likes.likes  
        #                     WHERE post_id = '{post_id}' and user_id = '{current_users.id}' ; """) ;
        # print(x)
        # print(x[0][0])
        # if  x[0][0] == 0 :
        x = session.execute(f'''INSERT INTO post_likes.likes (post_id,user_id,liked_at)
                        VALUES ('{post_id }','{current_users.id}','{datetime.now()}') ;
                                 WHERE user_id NOT IN (
                                                      SELECT user_id FROM post_likes.likes
                                                            WHERE post_id = '{post_id}' 
                                                            )    ;
                                ''')
        # else :
        #      return Response(status_code=status.HTTP_403_FORBIDDEN,
        #                             content={"detail":"Not authorized to perform requested action "})
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    return x

@router.delete("/{comment_id}/detele/")
async def test(comment_id: str,current_users : int = Depends(auth2.get_current_user)):
   try : 

    session = csd() 
    x = tuple(session.execute(f'''SELECT * FROM comment.photo_comments
                        WHERE id = {comment_id} ; '''))
    if len(x) != 0:
           
        if int(current_users.id) == int(x[0][1]) :

            session.execute(f'''DELETE FROM comment.photo_comments
                            WHERE id = {comment_id} ; ''')
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


