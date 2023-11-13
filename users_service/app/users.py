from fastapi import FastAPI,Depends,status ,HTTPException,APIRouter,Response
from app.config import curso
from app.utils import hashpass
from app.schema import update_users,users,bio_users
from app import auth2
import json
import aiohttp
import asyncio
router = APIRouter (
         prefix = "/users" ,
         tags = ["users"]
)

@router.get("/{user_id}/views/")
async def view(user_id:str,current_users : int = Depends(auth2.get_current_user)):
    try :
        sql = f"""SELECT usersname,email,
                        post,followers,followings,create_at  
                        from users where user_id = {user_id} ;"""
        
        db = curso()
        c = db.cursor()
        c.execute(sql)
        i = c.fetchall()
        x = bio_users(
            username = str(i[0][0]),
            email = str(i[0][1]),
            post = i[0][2],
            followers = i[0][3],
            followings = i[0][4],
            create_at = str(i[0][5])
         
        ).dict()
        
        db.close()

        my_headers =  {'Authorization' : f'Bearer {current_users.access_token}'}

        async with aiohttp.ClientSession() as sessionn:
          async with sessionn.get(f'http://host.docker.internal:7778/api/v1/web/comments/{post_id}/views/',
                                 headers=my_headers) as response:
          
            response_data = await response.json()

        

    except Exception as e:
         print(f"Error {e}")
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Not authorized to perform requested action")
    
    return {"bio":x,"post":response_data}

@router.post('/register',status_code=status.HTTP_201_CREATED)
def register(new_user : users):
 try: 
  db = curso()
  c = db.cursor()
  sql = f'''select * from users where usersname = '{new_user.username}'; ''' 
  c.execute(sql)
  check = c.fetchall()
  if len(check) != 0 :
          j =  {"detail":"look like someone already used it usersname ,please try difference usersname"}
          # Decode the JSON string into a Python object
          JSON_string = json.dumps(j)
          return Response(status_code=status.HTTP_403_FORBIDDEN,
                          content=JSON_string)
                        
  else:      
    new_pass = hashpass(new_user.password)
    new_user.password = new_pass
    x = (new_user.username,new_user.email,new_user.password,new_user.is_actice)
    sql = (""" insert into users(usersname,email,passwords,is_active) 
                values (%s,%s,%s,%s) RETURNING user_id ;""")
    c.execute(sql,x)
    x = c.fetchall() 
    db.commit()
    db.close()
 except Exception as e:
     print(f"Error {e}")
     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
 return { "user_id":x[0][0],
          "username":new_user.username,
          "email":new_user.email }
@router.put('/update/{id}',response_model = update_users)
def update_user(id : int,new_update_user : update_users,current_user : int = Depends(auth2.get_current_user)): 
    db = curso()
    c = db.cursor() 
    sql = f'''select * from "users"	where "user_id" = {id} ;'''
    c.execute(sql)
    x = c.fetchall()
  
    if len(x) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")
    if id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    else:
        try:
            sql1 = f'''UPDATE "users" SET 
                           usersname = '{new_update_user.username}' ,
                           email = '{new_update_user.email}' ,
                           is_staff = '{new_update_user.is_staff}'
                           WHERE user_id = {id} ;'''
            c.execute(sql1)
            db.commit()
            db.close()
        except Exception as e:
            print(f"Error {e}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f"{e}")
            
        return new_update_user

@router.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int,current_user : int = Depends(auth2.get_current_user)):
  db = curso()
  c = db.cursor() 
  sql = f'''select * from "users"	where "user_id" = {id} ;'''
  c.execute(sql)
  x = c.fetchall()

  if len(x) == 0 :
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"user with id: {id} does not exist")
  if id != int(current_user.id) :
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                          detail="Not authorized to perform requested action")
  else:
      sql1 = f'''delete from "users" where "user_id" = {id} ;'''
      c.execute(sql1)
      db.commit()
      db.close()

  return Response(status_code=status.HTTP_204_NO_CONTENT)

