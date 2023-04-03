from fastapi import APIRouter, Depends
from ..dependencies import get_token_header
from ..databases import magazines_collection
from ..internal.magazine import Magazine

router = APIRouter( 
    prefix="/magazines",
    responses={ 
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_token_header)]
)

@router.post("/")
async def create_magazine(body: dict):
    '''
    # create new magazine
    ### request body
    - name: `str`
    - description: `str`
    '''
    new_magazine = Magazine(
        name=body["name"],
        description=body["description"]
    )

    # add magazine to list 
    magazines_collection.add_magazine(new_magazine)

    return {
        "message": "User created successfully",
        "new_magazine": new_magazine
    }

@router.get("/")
async def read_magazine():
    '''
    # get all magazine
    '''
    result = magazines_collection.get_magazines()
    return result

@router.put("/")
async def edit_magazine():
    '''
    #edit magazine by id
    ### request body
     - magazine_id: `str`
     - title: `str`
     - description: `str`
     - add_roadtrip_id: `str`
     - remove_roadtrip_id: `str`
    '''

    # validate body
    if not body:
        return HTTPException(status_code=400, detail="Body is required")
    if not body['magazine_id']:
        return HTTPException(status_code=400, detail="magazine_id is required")
    if not body['title']:
        return HTTPException(status_code=400, detail="title is required")
    if not body['description']:
        return HTTPException(status_code=400, detail="description is required")

    new_magazine = magazines_collection.get_magazine_by_id(magazine_id)

    # edit magazine by id
    if body['title'] != '':
        new_magazine.set_name(body['title'])

    if body['description'] != '':
        new_magazine.set_description(body['description'])

    if body['add_roadtrip_id'] != '':
        new_magazine.add_roadtrip_id(body['add_roadtrip_id'])

    if body['remove_roadtrip_id'] != '':    
        new_magazine.remove_roadtrip_id(body['remove_roadtrip_id'])
    
    return {"message":"magazine edited successfully"}


