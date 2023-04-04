from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import favorite_collection
from ..dependencies import get_token_header
from ..internal.favorite_catalog import FavoriteCatalog
from ..internal.favorite_landmark import FavoriteLandmark

router = APIRouter( 
    prefix="/favorites",
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
        raise HTTPException(status_code=404, detail="No favorite_landmark found")
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
        return HTTPException(status_code=400, detail="Body is required")
    if not body['user_id']:
        return HTTPException(status_code=400, detail="user_id is required")
    if not body['new_landmark']:
        return HTTPException(status_code=400, detail="landmark_id is required")

    user_id = body["user_id"]
    new_landmark = body["new_landmark"]
    output = favorite_collection.add_favorite_landmark_by_user_id(user_id=user_id, new_landmark=new_landmark)
    return output


