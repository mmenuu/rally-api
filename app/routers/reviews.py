from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import reviews_collection
from ..internal.review import Review 


router = APIRouter(  
    prefix="/reviews",
    tags=["reviews"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
)

@router.get('/')
async def read_reviews():
    '''
    # get all review
    '''
    result = reviews_collection.get_reviews()
    if not result:
        raise HTTPException(status_code=404, detail="No reviews found")
    return result 

@router.post('/')
async def create_review(body: dict):
    '''
    # create new magazine
    ### request body
    - review_text: `str`
    - reviewer: `str` # user_id
    - landmark_id: `str`
    - rating: `float`
    '''

    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not body['review_text']:
        raise HTTPException(status_code=400, detail="review_text is required")
    if not body['reviewer']:
        raise HTTPException(status_code=400, detail="reviewer(user_id) is required")
    if not body['landmark_id']:
        raise HTTPException(status_code=400, detail="landmark_id is required")
    if not body['rating']:
        raise HTTPException(status_code=400, detail="rating is required")

    new_review = Review(
        review_text = body["review_text"], 
        user_id = body["reviewer"],
        landmark_id = body["landmark_id"],
        rating = body["rating"]
    )

    reviews_collection.add_review(new_review)
    
    return {
        "detail": "review created successfully",
    }

@router.put("/")
async def edit_review(body: dict):
    '''
    #edit review
    ### request body
    - review_text: `str`
    - reviewer: `str` # user_id
    - landmark_id: `str`
    - rating: `float`
    '''
    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not body['review_text']:
        raise HTTPException(status_code=400, detail="reviewe_text is required")
    if not body['reviewer']:
        raise HTTPException(status_code=400, detail="reviewer(user_id) is required")
    if not body['landmark_id']:
        raise HTTPException(status_code=400, detail="landmark_id is required")
    if not body['rating']:
        raise HTTPException(status_code=400, detail="rating is required")
    
    new_review = reviews_collection.get_review(body['reviewer'], body['landmark_id'])
    
    # edit review 
    # not sure how to edit review
    if body['review_text'] != "":
        new_review.set_review_text(body['review_text'])
    if body['rating'] != "":
        new_review.set_rating(body['rating'])
    
    return {
        "detail":"review edited successfully",
    }
@router.delete("/")
async def delete_review(body: dict):
    '''
    # delete existing review
    ### request body
    - user_id: `str`
    - landmark_id: `str`
    '''
    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not body['magazine_id']:
        raise HTTPException(status_code=400, detail="magazine_id is required")

    reviews_collection.remove_review(body['user_id'], body['landmark_id'])
    
    return {
        "detail" : "review deleted successfully"
    }
    

    
