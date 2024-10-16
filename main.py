from fastapi import FastAPI

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