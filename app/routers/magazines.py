from fastapi import APIRouter, HTTPException, status, Depends

from ..dependencies import get_token_header
from ..databases import magazines_collection
from ..internal.magazine import Magazine

router = APIRouter(
    prefix="/magazines",
    tags=["magazines"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_token_header)]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_magazine(body: dict):
    '''
    # create new magazine
    ### request body
    - title: `str`
    - description: `str`
    '''
    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not body['title']:
        raise HTTPException(status_code=400, detail="title is required")
    if not body['description']:
        raise HTTPException(status_code=400, detail="description is required")

    new_magazine = Magazine(
        name=body["title"],
        description=body["description"]
    )

    # add magazine to list
    magazines_collection.add_magazine(new_magazine)

    return {
        "detail": "User created successfully",
        "detail": new_magazine
    }


@router.get("/")
async def read_magazine():
    '''
    # get all magazine
    '''
    result = magazines_collection.get_magazines()
    if not result:
        raise HTTPException(status_code=404, detail="No magazines found")
    return result


@router.get("/{magazine_id}") # get all roadtrip from magazine tag
async def get_magazine_by_id(magazine_id:str):
    '''
    # get magazine by id
    '''
    # validate magazine_id
    if not magazine_id:
        raise HTTPException(status_code=400, detail="magazine_id is required")
        
    new_magazine = magazines_collection.get_magazine_by_id(magazine_id)

    if not new_magazine:
        raise HTTPException(status_code=404, detail="No magazines found")
        
    return new_magazine



@router.patch("/{magazine_id}") # update magazine
async def update_magazine(magazine_id:str, body: dict):
    '''
    #edit magazine by id
    ### request body
     - magazine_id: `str` required
     - title: `str` optional
     - description: `str` optional
    '''

    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not magazine_id:
        raise HTTPException(status_code=400, detail="magazine_id is required")

    new_magazine = magazines_collection.get_magazine_by_id(magazine_id)
    if new_magazine is None:
        raise HTTPException(status_code=404, detail= "Magazine not found")

    # edit magazine by id
    if body['title']:
        new_magazine.set_name(body['title'])
    if body['description']:
        new_magazine.set_description(body['description'])

    magazines_collection.update_magazine_by_id(new_magazine.get_id(), new_magazine)

    return {
        "detail": "magazine edited successfully",
        "detail": new_magazine
    }


@router.patch("/{magazine_id}/add_roadtrip") # add magazine to roadtrip
async def add_magazine(magazine_id: str, body: dict):
    '''
    # Update a magazine roadtrip
    ### request body
    - roadtrip_id: `str` # roadtrip_id
    '''
    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not magazine_id:
        raise HTTPException(status_code=400, detail="magazine_id is required")
    if not body['roadtrip_id']:
        raise HTTPException(status_code=400, detail="roadtrip is required")

    magazines_collection.add_roadtrip(magazine_id, body['roadtrip_id'])
    new_magazine = magazines_collection.get_magazine_by_id(magazine_id)
    return{
        "detail": "add_roadtrip_successfully",
        "detail": new_magazine
    }
@router.delete("/{magazine_id}")
async def delete_roadtrip(roadtrip_id: str, body: dict):
    '''
    #delete roadtrip from magazine
    request body
    - roadtrip_id: `str`
    '''
    # validate roadtrip
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not magazine_id:
        raise HTTPException(status_code=400, detail="magazine_id is required")
    if not body['roadtrip']:
        raise HTTPException(status_code=400, detail="roadtrip is required")

    magazines_collection.remove_roadtrip(magazine_id, roadtrip_id)


@router.delete("/")
async def delete_magazine(body: dict):
    '''
    # delete existing magazine
    ### request body
    - magazine_id: `str`
    '''

    # validate body
    if not body:
        raise HTTPException(status_code=400, detail="Body is required")
    if not body['magazine_id']:
        raise HTTPException(status_code=400, detail="magazine_id is required")

    magazines_collection.remove_magazine(body['magazine_id'])

    return {
        "detail": "Magazine deleted successfully"
    }
 