from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import roadtrips_collection
from ..dependencies import get_token_header
from ..internal.roadtrip import Roadtrip

router = APIRouter(
    prefix="/roadtrips",
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_token_header)]
)

@router.get("/")
async def get_roadtrips():
    '''
    # Get all roadtrips
    '''
    roadtrips_exits = roadtrips_collection.get_roadtrips()
    if not roadtrips_exits:
        raise HTTPException(status_code=404, detail="No roadtrips found")
    return roadtrips_exits


@router.post("/")
async def create_roadtrip(body: dict):
    '''
    # Create a new roadtrip
    ### request body
    - title: `str`
    - sub_title: `str`
    - description: `str`
    - category: `str`
    - summary: `str`
    - user_id: `str`
    '''

    # validate body
    if not body:
        return HTTPException(status_code=400, detail="Body is required")
    if not body['title']:
        return HTTPException(status_code=400, detail="Title is required")
    if not body['sub_title']:
        return HTTPException(status_code=400, detail="Sub title is required")
    if not body['description']:
        return HTTPException(status_code=400, detail="Description is required")
    if not body['category']:
        return HTTPException(status_code=400, detail="Category is required")
    if not body['summary']:
        return HTTPException(status_code=400, detail="Summary is required")
    if not body['user_id']:
        return HTTPException(status_code=400, detail="User id is required")

    new_roadtrip = Roadtrip(
        title=body['title'],
        sub_title=body['sub_title'],
        description=body['description'],
        category=body['category'],
        summary=body['summary'],
        user_id=body['user_id']
    )

    roadtrips_collection.add_roadtrip(new_roadtrip)

    return {
        "detail": "Roadtrip created successfully",
        "roadtrip": new_roadtrip
    }

@router.get("/{roadtrip_id}")
async def get_roadtrip(roadtrip_id: str):
    '''
    # Get a roadtrip by id
    '''
    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(status_code=404, detail="Roadtrip not found")
    
    return roadtrip_exists

@router.put("/{roadtrip_id}")
async def update_roadtrip(roadtrip_id: str, body: dict):
    # TODO implement update roadtrip
    # update roadtrip by id
    pass