from typing import Annotated

from fastapi import HTTPException, status, Depends, Header, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel

from .internal.user import User
from .internal.admin import Admin
from .internal.person import Person
from .databases import persons_collection
from .config import get_settings

settings = get_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    username: str | None = None


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = persons_collection.get_person_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    
    return user


async def check_admin_role(current_user = Depends(get_current_user)):
    if not isinstance(current_user, Admin):
        raise HTTPException(status_code=403, detail="Forbidden")
    
    return current_user