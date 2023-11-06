from pydantic import BaseModel,EmailStr
from typing import Optional,List
from starlette.requests import Request
from datetime import datetime

# class users(BaseModel):
#     username : str
#     email : EmailStr
#     password : str
#     is_actice : bool = True



# class login(BaseModel):
#     email : EmailStr
#     password : str

    
class tokendata(BaseModel):
    id : Optional[str] = None
    access_token : Optional[str] = None
class token(BaseModel) :
    access_token : str
    token_type : str

# class update_users(BaseModel):
#     username : str
#     email : str
#     is_staff : bool

class follows(BaseModel):
    users_id : str = None
    following : str = None
    followed : str = None
    follow_at : str = None

class followings(BaseModel):
    following : str = None
    follow_at : str = None    

class followed(BaseModel):

    followed : str = None
    follow_at : str = None


#  {
#     "id": "18082293499389226",
#     "from": {
#         "id": "3534134895",
#         "username": "olivier_trgg",
#         "full_name": "Vũ Vũ",
#         "profile_picture": "https://instagram.fhan2-4.fna.fbcdn.net/v/t51.2885-19/237058358_312378743909639_8698233212349077717_n.jpg?stp=dst-jpg_s150x150\u0026_nc_ht=instagram.fhan2-4.fna.fbcdn.net\u0026_nc_cat=111\u0026_nc_ohc=63Dvk53C5s4AX_zQe9q\u0026edm=AOLdatgBAAAA\u0026ccb=7-5\u0026oh=00_AfA3LUZ6sHHzsTkWCtGLGC-JVNG-ydBedLYbkrzZ75QqGw\u0026oe=65228073\u0026_nc_sid=beb6a3"
#     },
#     "text": "none",
#     "created_time": 1696438175,
#     "status": "ok"
# }
   

# class add(BaseModel):
#     orders_id : str = None
#     item_id : str
#     item_name : str
#     units_sold : int = 0
#     unit_price : float
#     total_prices : float = None
#     orders_status : str = "unpaid"

# class items(BaseModel):
#      __root__: List[add]    
  
    
# class new_transactions(BaseModel):
#     order_id : str = None
#     id_customer : str = None
#     payment_methods : str 
#     order_status : str = 'Processing'
#     order_date : datetime = None
#     total_prices : float = None
#     note : str 
        
# class update_cart(BaseModel):
#     item_id : str 
#     units_sold : int = 0	
