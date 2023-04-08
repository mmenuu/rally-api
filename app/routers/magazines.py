from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ..dependencies import get_current_user
from ..databases import magazines_collection, roadtrips_collection
from ..internal.magazine import Magazine
from ..internal.user import User

router = APIRouter(
    prefix="/magazines",
    tags=["magazines"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
)


@router.get("/")
async def read_magazines():
    '''
    # get all magazine
    '''
    return magazines_collection.get_magazines()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_magazine(body: dict):
    '''
    # create new magazine
    ### request body
    - title: `str`
    - description: `str`
    '''

    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    new_magazine = Magazine(
        title=body.get("title", ""),
        description=body.get("description", ""),
    )

    magazines_collection.add_magazine(new_magazine)

    return {
        "detail": "magazine created successfully",
    }

@router.get("/")
async def get_all_magazine():
    '''
    # get all magazine objects in magazine catalog
    '''
    all_magazines = magazines_collection.get_magazines()

    if not all_magazines:
        raise HTTPException(status_code=404, detail="No magazines found")    
    
    return all_magazines


@router.get("/{magazine_id}", status_code=status.HTTP_200_OK)
async def get_magazine_by_id(magazine_id: str):
    '''
    # get magazine by id
    '''
    magazine_exists = magazines_collection.get_magazine_by_id(magazine_id)

    if not magazine_exists:
        raise HTTPException(status_code=404, detail="No magazines found")

    return magazine_exists


@router.patch("/{magazine_id}", status_code=status.HTTP_200_OK)
async def update_magazine(magazine_id: str, body: dict):
    '''
    #edit magazine by id
    ### request body
     - magazine_id: `str` required
     - title: `str` optional
     - description: `str` optional
    '''

    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    magazine_exists = magazines_collection.get_magazine_by_id(magazine_id)
    if magazine_exists is None:
        raise HTTPException(status_code=404, detail="Magazine not found")

    magazine_exists.set_name(body.get("title", magazine_exists.get_title()))
    magazine_exists.set_description(body.get("description", magazine_exists.get_description()))

    return {
        "detail": "magazine edited successfully",
    }


@router.delete("/{magazine_id}")
async def delete_roadtrip(magazine_id: str):
    '''
    # delete magazine by id
    '''
    magazine_exists = magazines_collection.get_magazine_by_id(magazine_id)
    magazines_collection.remove_magazine(magazine_exists)
    
    return {
        "detail": "magazine deleted successfully",
    }