from fastapi import APIRouter, HTTPException, status
from ..databases import users_collection
from ..internal.landmark import Landmark

router = APIRouter(
    prefix="/favorites",
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)


@router.get("/{user_id}")
async def read_favorites(user_id: str):
    user = users_collection.get_user_by_id(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")

    return user.get_favorite_landmarks()


@router.post("/")
async def add_favorites(body: dict):
    user_id = body["user_id"]
    landmark = body["landmark"]

    user = users_collection.get_user_by_id(user_id=user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")

    user.add_favorite_landmark(landmark)
    return user.get_favorite_landmarks()


@router.delete('/')
async def remove_favorites(body: dict):
    user_id = body["user_id"]
    landmark = body["landmark"]
    user = users_collection.get_user_by_id(user_id=user_id)
    output = user.remove_favorite_landmark_by_id(landmark)
    return output
