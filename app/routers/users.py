from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from ..databases import persons_collection
from ..dependencies import get_current_user, User, check_admin_role, Admin

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
async def read_users(isAdmin: Annotated[bool, Depends(check_admin_role)]):
    return [ user.to_dict() for user in persons_collection.get_persons()]


@router.get('/profile', status_code=status.HTTP_200_OK)
async def read_profile(current_user: Annotated[User | Admin, Depends(get_current_user)]):
    return {
        **current_user.to_dict(),
        'is_admin': isinstance(current_user, Admin)
    }


@router.get('/profile/{username}', status_code=status.HTTP_200_OK)
async def read_profile_by_username(username: str):
    user_exists = persons_collection.get_person_by_username(username)

    if user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_exists.to_dict()
