from fastapi import APIRouter

from app.internal.favorite_catalog import FavoriteCatalog
from app.internal.favorite_landmark import FavoriteLandmark

favorite_collection = FavoriteCatalog()

router = APIRouter( 
    prefix="/favorites",
    responses={ 
        404: {
            'message': 'Not Found'
        }
    }
)

@router.get("/")
async def read_favorites():
    result = favorite_collection.get_favorite_landmarks() 
    return result

@router.post("/")
async def add_favorites(body: dict):
    user_id = body["user_id"]
    new_landmark = body["new_landmark"]
    output = favorite_collection.add_favorite_landmark_by_user_id(user_id=user_id, new_landmark=new_landmark)
    return output


