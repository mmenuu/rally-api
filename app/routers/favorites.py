from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ..dependencies import get_current_user
from ..databases import users_collection
from ..internal.landmark import Landmark
from ..internal.user import User

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_favorites(current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # get all favorite landmarks by current user
    '''

    # get favorite landmarks
    favorite_landmarks = current_user.get_favorite_landmarks()
    return favorite_landmarks


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def read_favorite_landmarks(user_id: str):
    '''
    # get all favorite landmarks by user id
    '''

    # get user by id
    user_exists = users_collection.get_user_by_id(user_id)

    if user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    # get favorite landmarks
    favorite_landmarks = user_exists.get_favorite_landmarks()
    return favorite_landmarks


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_favorite_landmark(body: dict, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Add favorite landmark

    @param body: `dict` landmark object
    '''
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    try:
        favorite_landmark = Landmark(**body)
        exists = current_user.get_favorite_landmark_by_id(
            favorite_landmark.get_id())

        if exists is not None:
            raise HTTPException(
                status_code=400, detail="Favorite landmark already exists")

        current_user.add_favorite_landmark(favorite_landmark)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid landmark")

    return {
        "detail": "Favorite landmark added successfully",
    }


@router.delete("/{landmark_id}", status_code=status.HTTP_200_OK)
async def remove_favorite_landmark(landmark_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Remove favorite landmark by landmark id

    @param landmark_id: `str` id of the landmark
    '''

    favorite_landmark_exists = current_user.get_favorite_landmark_by_id(
        landmark_id)

    if favorite_landmark_exists is None:
        raise HTTPException(
            status_code=404, detail="Favorite landmark not found")

    current_user.remove_favorite_landmark(favorite_landmark_exists)

    return {
        "detail": "Favorite landmark deleted successfully",
    }
