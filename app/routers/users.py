from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from ..databases import users_collection
from ..dependencies import get_current_user, User

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
async def read_users(user_id: str | None = None):
    '''
    # Get all users
    '''

    if user_id:
        user_exists = users_collection.get_user_by_id(user_id)

        # check if user exist
        if user_exists is None:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            'id': user_exists.get_id(),
            'username': user_exists.get_username(),
            'email': user_exists.get_email()
        }

    return [
        {
            'id': user.get_id(),
            'username': user.get_username(),
            'email': user.get_email()
        }
        for user in users_collection.get_users()
    ]


@router.get('/profile', status_code=status.HTTP_200_OK)
async def read_profile(current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Get profile
    '''
    return {
        'id': current_user.get_id(),
        'username': current_user.get_username(),
        'email': current_user.get_email()
    }


@router.get('/profile/{username}', status_code=status.HTTP_200_OK)
async def read_profile_by_username(username: str):
    '''
    # Get profile by username
    '''
    user_exists = users_collection.get_user_by_username(username)

    if user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        'id': user_exists.get_id(),
        'username': user_exists.get_username(),
        'email': user_exists.get_email()
    }
