from blog_creation.hashing import Hash
from sqlalchemy.orm import Session
from blog_creation import models,schema
from fastapi import HTTPException,status,Response



def create_user(resquest:schema.users,db:Session):
    new_user = models.users(name=resquest.name,email=resquest.email,password=Hash.get_password_hash(resquest.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(id:int,db:Session):
    user = db.query(models.users).filter(models.users.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the user with id{id} is not found")

    return user
