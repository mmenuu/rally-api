from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from ..internal.user import User
from ..databases import users_collection
from ..dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)


@router.get('/', status_code=status.HTTP_200_OK)
async def read_users():
    '''
    # Get all users
    '''

    # get all users
    users_exists = users_collection.get_users()

    # check if users exist
    if not users_exists:
        raise HTTPException(status_code=404, detail="No users found")

    return users_exists


@router.get('/profile', status_code=status.HTTP_200_OK)
async def read_profile(current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Get profile
    '''
    return current_user


@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def read_user(user_id: str):
    '''
    # Get a user by id
    @param user_id: `str` id of the user
    '''
    # get user by id
    user_exists = users_collection.get_user_by_id(user_id)

    # check if user exist
    if user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_exists