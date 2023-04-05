from fastapi import APIRouter, HTTPException, status, Depends

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/favorites",
    tags=["favorites"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_token_header)]
)


@router.get("/")
async def read_favorites():
    '''
    # get all favorite_landmark
    '''
    result = favorite_collection.get_favorite_landmarks()
    if not result:
        raise HTTPException(
            status_code=404, detail="No favorite_landmark found")
    return result


@router.post("/")
async def add_favorites(body: dict):
    '''
    # add favorite landmark to store in system
    ### request body
    - user_id: `str`
    - new_landmark: `str` # landmark_id
    '''
    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not body['user_id']:
        raise HTTPException(status_code=400, detail="user_id is required")
    if not body['new_landmark']:
        raise HTTPException(status_code=400, detail="landmark_id is required")

    user_id = body["user_id"]
    new_landmark = body["new_landmark"]
    output = favorite_collection.add_favorite_landmark_by_user_id(
        user_id=user_id, new_landmark=new_landmark)

    return output
