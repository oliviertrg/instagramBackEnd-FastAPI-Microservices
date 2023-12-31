from fastapi import FastAPI ,Response,status ,HTTPException,APIRouter,Depends, Request
from app import auth2,schema
import requests
import json
from datetime import datetime
from app.config import curso
import uuid
import random
import string
import numpy as np



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
 
        sql = (f"""SELECT *,ROW_NUMBER() OVER(PARTITION BY post_id) AS row_num 
               FROM "likes" where "post_id" = '{post_id}' ORDER BY row_num DESC ;""")
        c.execute(sql)
        z = c.fetchall()
        print(z)
        print(len(z))
        if len(z) != 0 :
            x = (
                schema.likes(
                post_id=i[1],
                user_id=i[2],
                created_at=str(i[3]),
                
            ).dict()
            for i in z
                )
            t = z[0][4]
        else :
                t = 0
                x = list()
        db.close()
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")

    return {"total_likes" : f"{t}","like_data":x} 

@router.post("/{post_id}/like/")
async def like_post(post_id: str,current_users : int = Depends(auth2.get_current_user)):
    try:
        x = schema.likes(      
        user_id = str(current_users.id),
        created_at = str(datetime.now()),
        post_id = post_id     
        ).dict()   
    
        db = curso()
        c = db.cursor()
        sql = (f"""INSERT INTO likes
                                (post_id,user_id,liked_at)
                            SELECT '{post_id}','{current_users.id}','{datetime.now()}'
                            WHERE NOT EXISTS 
                                (
                                    SELECT user_id FROM likes 
                                            WHERE post_id = '{post_id}' 
                                            and user_id = '{current_users.id}' 
                                ); """ )
        c.execute(sql)
        db.commit()
        db.close()

    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    return x

@router.delete("/{post_id}/detele/")
async def delete_like(post_id: str,current_users : int = Depends(auth2.get_current_user)):
   try : 

    db = curso()
    c = db.cursor()
    c.execute(f"""DELETE FROM likes
                                WHERE user_id = '{current_users.id}'
                                and post_id = '{post_id}';""")
    db.commit()
    db.close()

 
   except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action") 
    
   return Response(status_code=status.HTTP_204_NO_CONTENT) 


