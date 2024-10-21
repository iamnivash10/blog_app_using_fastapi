from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog_creation.jwttoken import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    return verify_token(token)