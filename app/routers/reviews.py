from fastapi import APIRouter

from app.internal.review_catalog import ReviewCatalog
from app.internal.review import Review

review_collection = ReviewCatalog()

router = APIRouter(  
    prefix="/reviews",
    responses={
        404: {
            'message': 'Not Found'
        }
    }
)

@router.get('/')
async def read_reviews():
    result = review_collection.get_reviews()
    return result 

@router.post('/')
async def create_review(body: dict):
    new_review = Review(
        review_text = body["review_text"], 
        user_id = body["reviewer"],
        landmark_id = body["landmark_id"],
        rating = body["rating"]
    )

    review_collection.add_review(new_review)
    
    return new_review

