from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from ..databases import users_collection
from ..internal.user import User
from .. import config

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)

settings = config.get_settings()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    user = users_collection.get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user.get_password()):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


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
    user = users_collection.get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(body: dict):
    # TODO implement register and Return a JWT token.
    # verify if user already exists in the database.

    '''
    # Register a new user

    ### request body (json)
    - email: `str`
    - username: `str`
    - password: `str`

    ### response body
    - access_token: `str`
    - token_type: `str`

    '''

    # Validate body
    if not body:
        return HTTPException(status_code=400, detail="Body is required")
    if not body["email"]:
        return HTTPException(status_code=400, detail="Email is required")
    if not body["username"]:
        return HTTPException(status_code=400, detail="Username is required")
    if not body["password"]:
        return HTTPException(status_code=400, detail="Password is required")

    # create new user
    new_user = User(
        email=body["email"],
        username=body["username"],
        password=get_password_hash(body["password"])
    )

    # add user to collection
    users_collection.add_user(new_user)

    return {
        "detail": "User created successfully",
        "access_token": create_access_token(
            data={"sub": new_user.get_username()}
        ),
        "token_type": "bearer"
    }


@router.post("/login",  response_model=Token, status_code=status.HTTP_200_OK)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    '''
    # Login a user

    ### request body (form-encoded)
    - username: `str`
    - password: `str`

    ### response body
    - access_token: `str`
    - token_type: `str`
    '''

    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.get_username()}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
