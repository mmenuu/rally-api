from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header

from app.internal.user_catalog import UserCatalog
from app.internal.user import User


# catalog of users
users_collection = UserCatalog()

router = APIRouter(
    prefix="/users",
    dependencies=[Depends(get_token_header)],
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)

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
