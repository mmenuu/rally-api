from fastapi import APIRouter

from app.internal.user_catalog import UserCatalog
from app.internal.user import User

# catalog of users
users_collection = UserCatalog()

router = APIRouter(  
    prefix="/users",
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)


@router.post("/")
async def register(body: dict):
    '''
    # Register a new user

    ## body
    - email: `str`
    - username: `str`
    - password: `str`
    '''

    # Validate body
    if not body: return {"message": "Body is empty"}
    if not body["email"]: return {"message": "Email is required"}
    if not body["username"]: return {"message": "Username is required"}
    if not body["password"]: return {"message": "Password is required"}

    # create new user
    new_user = User(
        email = body["email"],
        username = body["username"],
        password = body["password"]
    )

    # add user to collection
    users_collection.add_user(new_user)

    return {
        "message": "User created successfully",
        "data": new_user
    }

@router.get('/')
async def read_users():
    '''Get all users'''

    # get all users
    users_exist = users_collection.get_users()

    # check if users exist
    if not users_exist:
        return {"message": "No users found"}

    return users_exist


@router.get('/{user_id}')
async def read_user(user_id: str):
    '''Get a user by id'''

    # get user by id
    user_exist = users_collection.get_user_by_id(user_id)

    # check if user exist
    if user_exist is None:
        return {"message": "User not found"}
    
    return user_exist