from fastapi import APIRouter,status,Depends,HTTPException
from .. import models,schema
from sqlalchemy.orm import session
from ..database import get_db
from..hashing import Hash
from..jwttoken import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=["login"])


@router.post("/login",status_code= status.HTTP_200_OK)
def athentication(request:OAuth2PasswordRequestForm = Depends(),db:session=Depends(get_db)):
     user = db.query(models.users).filter(models.users.email==request.username).first()
     if not user:
         raise HTTPException(status_code=401,detail="invalid credentials")
        
     if not Hash.verify_password(request.password,user.password):
         raise HTTPException(status_code=401,detail="password not matched")


     access_token = create_access_token(data={"sub":user.email})
     return {"access_token":access_token,"token_type":"bearer"}

     


    