from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ..databases import landmarks_collection
from ..internal.landmark import Landmark
from ..dependencies import get_current_user, User


router = APIRouter(
    prefix="/landmarks",
    tags=["landmarks"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_landmarks(current_user: Annotated[User, Depends(get_current_user)]):
    return [landmark.to_dict() for landmark in landmarks_collection.get_landmarks()]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_landmark(body: dict, current_user: Annotated[User, Depends(get_current_user)]):

    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    landmark_exists = landmarks_collection.get_landmark_by_id(body.get("id"))

    if landmark_exists:
        raise HTTPException(status_code=400, detail="Landmark already exists")

    new_landmark = Landmark(**body)
    landmarks_collection.add_landmark(new_landmark)

    return {
        'detail': 'Landmark created'
    }

@router.get("/{landmark_id}", status_code=status.HTTP_200_OK)
async def read_landmark(landmark_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    landmark = landmarks_collection.get_landmark_by_id(landmark_id)

    if not landmark:
        raise HTTPException(status_code=404, detail="Landmark not found")

    return landmark.to_dict()