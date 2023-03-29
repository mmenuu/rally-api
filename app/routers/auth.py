from fastapi import APIRouter, HTTPException, status

from ..internal.user import User
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

    ## body
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
        "message": "User created successfully",
        "data": new_user
    }
