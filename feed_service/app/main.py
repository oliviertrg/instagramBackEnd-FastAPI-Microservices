from fastapi import FastAPI , status ,HTTPException,APIRouter,Depends
from fastapi.middleware.cors import  CORSMiddleware
from starlette.requests import Request

from app import posts
import json
from typing import Optional

from fastapi import FastAPI
from strawberry import Schema, type
import strawberry
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import Info

from strawberry.fastapi import GraphQLRouter
app = FastAPI()

def custom_context_dependency() -> str:
    return "John"

def custom_context_dependencyy() -> str:
    return "Parrot"

def custom_context_dependencyyy() -> str:
    return "DJ Parrot"

def url_img() -> str:
    return "bsdjfgsdncjsgdhvj"

async def get_context(
    custom_value=Depends(custom_context_dependency),custom_value1=Depends(custom_context_dependencyy)
    ,custom_value2=Depends(custom_context_dependencyyy)
    ,custom_value3=Depends(url_img)
):
    return {
        "custom_value": custom_value,
        "custom_values": custom_value1,
        "custom_valuess": custom_value2,
        "img": custom_value3, 
    }
@strawberry.type
class Book:
    title: str
    author: str
    genre: str
from typing import List



@strawberry.type
class Query:
    @strawberry.field
    async def test(self, info: Info) -> str:
        return f"Testing<DONE> : {info.context['custom_value']}"
    @strawberry.field
    async def test1(self, info: Info) -> str:
        return f"Testing1<DONE> : {info.context['custom_values']}"
    @strawberry.field
    async def test2(self, info: Info) -> str:
        return f"Testing1<DONE> : {info.context['custom_valuess']}"
    

@strawberry.type
class new:
    @strawberry.field
    async def test(self, info: Info) -> str:
        return f"Testing<DONE> : {info.context['custom_value']}"
    @strawberry.field
    async def test1(self, info: Info) -> str:
        return f"Testing1<DONE> : {info.context['custom_values']}"
    @strawberry.field
    async def test2(self, info: Info) -> str:
        return f"Testing2<DONE> : {info.context['custom_valuess']}"
    @strawberry.field
    async def test3(self, info: Info) -> str:
        return f"Testing3<DONE> : {info.context['img']}" 
    @strawberry.field
    async def test4(self, x : str) -> str:
        return f"Testing3<DONE> : {x}"
    @strawberry.field
    async def test5(self, data: str) -> str:
        j = {"TestingXX<DONE>":f"{data}"}
        z = [j for i in range(10)]
        x = json.dumps(j)   
        return  x
    @strawberry.field
    async def book(self) -> List[Book]:
        book = [Book(title="The Hitchhiker's Guide to the Galaxy1", author="Douglas Adams", genre="Science fiction1"),
                Book(title="The Hitchhiker's Guide to the Galaxy2", author="Douglas Adams", genre="Science fiction2"),
                Book(title="The Hitchhiker's Guide to the Galaxy3", author="Douglas Adams", genre="Science fiction3")]
        return book


schema = strawberry.Schema(new)
# schema2 = strawberry.Schema(new)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)





app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def test() :
    b = (1,2,3,4,5)
    a = (int(i) for i in range(100))
    return {"testing":b,"testing----":f"{type(b)}","testing":b,"testing----":f"{type(b)}",
            "testing":"this is posts_server",
            "testing":"this is posts_server11111111111111111111"}

# schema = Schema()
# strawberry = strawberry()
# GraphQL type for a book
# @schema.type
# class Book:
#     title: str
#     author: str
#     genre: str


# @strawberry.type
# class Book:
#     title: str
#     author: str
#     genre: str
#     @strawberry.field
#     def hello(self) -> str:
#         return "Hello World"
    
# @strawberry.query(name="book")
# async def get_book(id: Optional[int] = None) :
#     # Get the book from a database or other data source
#      book = Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", genre="Science fiction")

#     # Return the book
#      return book
    
    


# Query field to get a book by its ID
# @schema.query(name="book")
# async def get_book(id: Optional[int] = None) :
#     # Get the book from a database or other data source
#     book = Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", genre="Science fiction")

#     # Return the book
#     return book


# graphql_app = GraphQLRouter(schema)

# app = FastAPI()
# app.include_router(graphql_app, prefix="/graphql")


# Create a FastAPI app with the GraphQL schema
# @app.get("/")
# async def graphql(schema: Schema = schema) :
#     await schema.execute_query(await app.request.body())

# Start the FastAPI server
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)

