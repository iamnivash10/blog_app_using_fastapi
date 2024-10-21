from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"data": {"message": "Hello World"}}

@app.get("/about")
async def about():
    return {"data": "About Page"}

@app.get("/about/{id}")
async def ab(id:int):
    return {"data": id}

@app.get("/blog")
async def blog(limit:int=10,published:bool=True):
    if published:
         return {"data": f'{limit}Blog from database published'}
    else:
         return {"data": f'{limit}Blog from database'}
class blog(BaseModel):
    title:str
    content:str
    published:bool
@app.post("/blogadd")
async def blogadd(data:blog):
    return {"data": f"Blog added with title as {data.title}"}
