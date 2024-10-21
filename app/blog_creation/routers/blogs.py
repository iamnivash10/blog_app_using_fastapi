from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import models,schema,database
from typing import List
from ..database import get_db
from sqlalchemy.orm import session
from ..repository import blog
from ..oauth2 import get_current_user



router = APIRouter()


@router.post("/add",status_code=status.HTTP_201_CREATED,tags = ["blog"])
async def add(request:schema.blog,db:session=Depends(get_db)):
    return blog.create_new_blog(request,db)
@router.get("/allblogs",response_model=list[schema.show_blogs],tags = ["blog"])
def get(db:session=Depends(get_db),current_user: schema.users = Depends(get_current_user)):
    return blog.show_all_blogs(db)   

@router.put("/blogupdate/{id}",status_code = status.HTTP_202_ACCEPTED,tags = ["blog"])
def update(id:int,request:schema.blog,db:session=Depends(get_db)):
   return blog.update_blog_by_id(id,request,db)

@router.get("/blog/{id}",response_model=schema.show_blog,tags = ["blog"])
def show(id:int,response:Response,db:session=Depends(get_db)):
    return blog.show_blog_by_id(id,response,db)
@router.delete("/blogdelete/{id}",status_code=status.HTTP_204_NO_CONTENT,tags = ["blog"])
def destroy(id:int,db:session=Depends(get_db)):
    return blog.delete_blog_by_id(id,db)