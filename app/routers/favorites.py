from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ..dependencies import get_current_user, User
from ..databases import landmarks_collection
from ..internal.landmark import Landmark

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_favorites(current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # get all favorite landmarks by current user
    '''

    favorite_landmarks = [landmarks_collection.get_landmark_by_id(
        landmark_id) for landmark_id in current_user.get_favorite_landmarks()]

    return [{
        "id": landmark.get_id(),
        "name": landmark.get_name(),
        "amenity": landmark.get_amenity(),
        "position": landmark.get_position(),
        "opening_hours": landmark.get_opening_hours(),
    } for landmark in favorite_landmarks]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_favorite_landmark(body: dict, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Add favorite landmark

    @param body: `dict` landmark object
    '''
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    try:
        landmark_exists = landmarks_collection.get_landmark_by_id(
            body.get("id"))

        if not landmark_exists:
            new_landmark = Landmark(**body)
            landmarks_collection.add_landmark(new_landmark)

        favorite_exists = current_user.get_favorite_landmark_by_id(
            body.get("id"))
        if favorite_exists:
            raise HTTPException(
                status_code=400, detail="Favorite landmark already exists")

        current_user.add_favorite_landmark(body.get("id"))
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

    if not favorite_landmark_exists:
        raise HTTPException(
            status_code=404, detail="Favorite landmark not found")

    current_user.remove_favorite_landmark(favorite_landmark_exists)

    return {
        "detail": "Favorite landmark deleted successfully",
    }
