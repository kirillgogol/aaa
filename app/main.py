from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

import app.model as model
from app.config import engine

 
model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# @app.get('/blog')
# def index(limit=10, published:bool=True, sort:Optional[bool]=None):
#     if published:
#         return {"data": f'{limit} published blogs'}
#     else:
#         return {"data": f'{limit} blogs'}


# class Blog(BaseModel):
#     title: str
#     body: str
#     is_published: Optional[bool]


# @app.post('/blog')
# def create_blog(blog: Blog):
#     return {'data': f'blog iss created with title as {blog.title}'}
    

# @app.get('/blog/{id}')
# def show(id:int):
#     return {"data": id}
