from fastapi import APIRouter,Depends,status,HTTPException,Response
from blog_creation import models,schema,database
from blog_creation.database import get_db
from typing import List
from passlib.context import CryptContext
from sqlalchemy.orm import session
from blog_creation.repository import user


router = APIRouter() 



@router.post("/user",status_code=status.HTTP_201_CREATED,response_model=schema.user_name_email,tags = ["user"])
def createuser(resquest:schema.users,db:session=Depends(get_db)):
    user.create_user(resquest,db)
    
@router.get("/user/{id}",response_model=schema.user_name_email,status_code=status.HTTP_200_OK,tags = ["user"])
def getusers(id:int,db:session=Depends(get_db)):
    return user.get_user_by_id(id,db)