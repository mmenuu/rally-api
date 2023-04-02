from fastapi import APIRouter, HTTPException, status

from ..databases import users_collection
from .users import users_collection

router = APIRouter(
    prefix="/auth",
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: dict):
    '''
    # Register a new user

    ### request body
    - email: `str`
    - username: `str`
    - password: `str`
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
        password=body["password"]
    )

    # add user to collection
    users_collection.add_user(new_user)

    return {
        "detail": "User created successfully",
        "user": new_user
    }


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(body: dict):
    # TODO: implement login
    # 1. validate body
    # 2. check if user exists
    # 3. check if password is correct
    # 4. return jwt token
    pass