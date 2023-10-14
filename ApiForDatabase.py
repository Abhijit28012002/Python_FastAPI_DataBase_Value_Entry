from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange
from ValueEnterinTable import EnterValue

app = FastAPI()

class Post(BaseModel):
    name: str
    roll: int

@app.get("/") 
def root():
    return {"message": "Welcome to my Database API"}

@app.post("/posts")
def create_posts(post: Post):
    post_dict=post.dict()
    EnterValue(post_dict['name'],post_dict['roll'])
    return {"data" : "DataBase Entry Successfull"}
    