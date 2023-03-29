from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header
from ..internal.user_catalog import UserCatalog

# catalog of users
users_collection = UserCatalog()

router = APIRouter(
    prefix="/users",
    dependencies=[Depends(get_token_header)],
    tags=["users"],
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
        raise HTTPException(status_code=404, detail="No users found")

    return users_exist


@router.get('/{user_id}')
async def read_user(user_id: str):
    '''Get a user by id'''

    # get user by id
    user_exist = users_collection.get_user_by_id(user_id)

    # check if user exist
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_exist
