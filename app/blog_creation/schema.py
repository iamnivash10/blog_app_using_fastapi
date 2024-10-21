from pydantic import BaseModel
from typing import Optional, List

class blog(BaseModel):
    title:str
    content:str
    class Config(): 
        orm_mode = True 

class users(BaseModel):
    name:str
    email:str
    password:str
    class Config():
        orm_mode = True

class user_name_email(BaseModel):
    name:str
    email:str
    blogs:List[blog]=[]
    class Config():
        orm_mode = True

class user_name_email_only(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True

class show_blog(BaseModel):
    title:str
    content:str
    creator :user_name_email_only
    class Config():
        orm_mode = True

class show_blogs(BaseModel):
    title:str
    content:str
    creator :user_name_email_only
    class Config():
        orm_mode = True

class login(BaseModel):
    username :str
    password:str
    class Config():
        orm_mode = True

class token_data(BaseModel):
    email:Optional[str]=None
    class Config():
        orm_mode = True