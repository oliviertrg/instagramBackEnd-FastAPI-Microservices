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
    prefix = "/api/v1/web/follows",
    tags = ["follows"]
)


@router.get("/{user_id}/views/follwing")
async def view(user_id:str,current_users : int = Depends(auth2.get_current_user)):
    try :
        db = curso()
        c = db.cursor()
 
        sql = (f"""SELECT following_id,create_at
               FROM "followers" where 
               "user_id" = '{user_id}' ;""")
        c.execute(sql)
        z = c.fetchall()


        x = (
                schema.followings(
                following=i[0] ,
                follow_at = str(i[1])
                
            ).dict()
            for i in z
                )
        db.close()
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    
    return {"data":x} 

@router.get("/{user_id}/views/followed")
async def view(user_id:str,current_users : int = Depends(auth2.get_current_user)):
    try :
        db = curso()
        c = db.cursor()
 
        sql = (f"""SELECT user_id,create_at
               FROM "followers" where 
               "following_id" = '{user_id}' ;""")
        c.execute(sql)
        z = c.fetchall()


        x = (
                schema.followed(
                followed=i[0],
                follow_at = str(i[1])
            ).dict()
            for i in z
                )
        db.close()
    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    
    return {"data":x} 

@router.post("/{user_id}/add/")
async def follows(user_id: str,current_users : int = Depends(auth2.get_current_user)):
    try:
        x = schema.follows(      
        users_id = current_users.id ,
        following  = user_id,
        follow_at = str(datetime.now())
        ).dict()
        db = curso()
        c = db.cursor()
        sql = (f"""INSERT INTO followers
                                (user_id,following_id,create_at)
                            SELECT '{current_users.id}','{user_id}','{datetime.now()}'
                            WHERE NOT EXISTS 
                                (
                                    SELECT following_id FROM followers
                                            WHERE user_id = '{current_users.id}'
                                             and  following_id = '{user_id}' 
                                            
                                ); """ )
        c.execute(sql)
        db.commit()
        db.close()

    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    return x

@router.delete("/{user_id}/unfollows/")
async def test(user_id: str,current_users : int = Depends(auth2.get_current_user)):
   try : 
    db = curso()
    c = db.cursor()
    c.execute(f"""DELETE FROM followers
                                WHERE user_id = '{current_users.id}'
                                and following_id = '{user_id}';""")
    db.commit()
    db.close()
 
   except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action") 
    
   return Response(status_code=status.HTTP_204_NO_CONTENT) 


