from fastapi import APIRouter, Depends

from ..dependencies import get_token_header
from ..databases import reviews_collection
from ..internal.review import Review 


router = APIRouter(  
    prefix="/reviews",
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_token_header)]    
)

@router.get('/')
async def read_reviews():
    '''
    # get all review
    '''
    result = reviews_collection.get_reviews()
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
        return HTTPException(status_code=400, detail="Body is required")
    if not body['review_text']:
        return HTTPException(status_code=400, detail="title is required")
    if not body['reviewer']:
        return HTTPException(status_code=400, detail="description is required")
    if not body['landmark_id']:
        return HTTPException(status_code=400, detail="description is required")
    if not body['rating']:
        return HTTPException(status_code=400, detail="description is required")

    new_review = Review(
        review_text = body["review_text"], 
        user_id = body["reviewer"],
        landmark_id = body["landmark_id"],
        rating = body["rating"]
    )

    reviews_collection.add_review(new_review)
    
    return {
        "message": "review created successfully",
        "message": new_review
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
        return HTTPException(status_code=400, detail="Body is required")
    if not body['review_text']:
        return HTTPException(status_code=400, detail="title is required")
    if not body['reviewer']:
        return HTTPException(status_code=400, detail="reviewer is required")
    if not body['landmark_id']:
        return HTTPException(status_code=400, detail="landmark_id is required")
    if not body['rating']:
        return HTTPException(status_code=400, detail="rating is required")
    
    new_review = reviews_collection.get_review(body['reviewer'], body['landmark_id'])
    
    # edit review 
    # not sure how to edit review
    if body['review_text'] != "":
        new_review.set_review_text(body['review_text'])
    if body[rating] != "":
        new_review.set_rating(body['rating'])
    
    return {"message":"review edited successfully",
            "new_magazine": new_review
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
        return HTTPException(status_code=400, detail="Body is required")
    if not body['magazine_id']:
        return HTTPException(status_code=400, detail="magazine_id is required")

    reviews_collection.remove_review(body['user_id'], body['landmark_id'])
    
    return {
        "message" : "review deleted successfully"
    }
    

    
