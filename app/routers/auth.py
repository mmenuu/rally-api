from fastapi import APIRouter

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


@router.post("/register")
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
        return {"message": "Body is empty"}
    if not body["email"]:
        return {"message": "Email is required"}
    if not body["username"]:
        return {"message": "Username is required"}
    if not body["password"]:
        return {"message": "Password is required"}

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