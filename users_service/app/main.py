from fastapi import FastAPI , status ,HTTPException,APIRouter
from fastapi.middleware.cors import  CORSMiddleware
from starlette.requests import Request
from app import auth_users,users


app = FastAPI(
        title="instagram",
        description="Fast API"
        # version="1.0.0"
    )




origins = ["http://0.0.0.0:7777/"]
app.add_middleware(
    CORSMiddleware ,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"] ,
    allow_headers = ["*"]
)
app.include_router(users.router)
app.include_router(auth_users.router)





@app.get("/test")
def test():
    b = (1,2,3,4,5)
    a = (int(i) for i in range(100))
    return {"testing":b,"testing----":f"{type(b)}","testing":"this is user_server"}

