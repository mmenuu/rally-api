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
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_landmarks(current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # get all landmarks
    '''

    return [{
        "id": landmark.get_id(),
        "name": landmark.get_name(),
        "amenity": landmark.get_amenity(),
        "position": landmark.get_position(),
        "opening_hours": landmark.get_opening_hours(),
        "reviews": [{
            "id": review.get_id(),
            "reviewer": review.get_reviewer(),
            "review_text": review.get_review_text(),
            "rating": review.get_rating()
        } for review in landmark.get_reviews()]
    } for landmark in landmarks_collection.get_landmarks()]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_landmark(body: dict, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # create new landmark

    @param body: `dict` landmark object
    '''

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
    '''
    # get landmark by id

    @param landmark_id: `str` landmark id
    '''

    landmark = landmarks_collection.get_landmark_by_id(landmark_id)

    if not landmark:
        raise HTTPException(status_code=404, detail="Landmark not found")

    return {
        "id": landmark.get_id(),
        "name": landmark.get_name(),
        "amenity": landmark.get_amenity(),
        "position": landmark.get_position(),
        "opening_hours": landmark.get_opening_hours(),
        "reviews": [{
            "id": review.get_id(),
            "reviewer": review.get_reviewer(),
            "review_text": review.get_review_text(),
            "rating": review.get_rating()
        } for review in landmark.get_reviews()]
    }