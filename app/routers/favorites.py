from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import users_collection
from ..internal.landmark import Landmark

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
)


@router.get("/{user_id}")
async def read_favorites(user_id: str):
    '''
    # get all favorite landmarks by user_id
    '''

    # get user by id
    user_exists = users_collection.get_user_by_id(user_id)

    # check if user exist
    if user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    # get favorite landmarks
    favorite_landmarks = user_exists.get_favorite_landmarks()

    if not favorite_landmarks:
        raise HTTPException(
            status_code=404, detail="No favorite landmarks found")

    return favorite_landmarks


@router.post("/{user_id}")
async def add_favorite_landmark(user_id: str, body: dict):
    user_exists = users_collection.get_user_by_id(user_id)

    if user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    if not body['favorite_landmark']:
        raise HTTPException(status_code=400, detail="new_landmark is required")

    new_landmark = Landmark(
        id=body['favorite_landmark']['id'],
        name=body['favorite_landmark']['name'],
        amenity=body['favorite_landmark']['amenity'],
        location=body['favorite_landmark']['location'],
        opening_hours=body['favorite_landmark']['opening_hours']
    )

    user_exists.add_favorite_landmark(new_landmark)
    return {
        "detail": "Favorite landmark added successfully",
    }


# @router.delete("/{user_id}")
# async def delete_favorite_landmark(user_id: str, body: dict):
#     user_exists = users_collection.get_user_by_id(user_id)
#     if user_exists is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     if not body:
#         raise HTTPException(status_code=400, detail="Body is required")

#     if not body['favorite_landmark']:
#         raise HTTPException(status_code=400, detail="landmark is required")

    
#     landmark_id = body["landmark_id"]
#     user_exists.remove_favorite_landmark(landmark_id)
#     return {
#         "detail": "Favorite landmark added successfully",
#     }
