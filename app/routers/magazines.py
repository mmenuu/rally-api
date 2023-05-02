from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ..dependencies import check_admin_role, get_current_user
from ..databases import magazines_collection, roadtrips_collection

from ..internal.admin import Admin
from ..internal.magazine import Magazine

router = APIRouter(
    prefix="/magazines",
    tags=["magazines"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_magazines():
    '''
    # get all magazine objects in magazine catalog
    '''

    return [ magazine.to_dict() for magazine in magazines_collection.get_magazines()]


@router.get("/{magazine_id}", status_code=status.HTTP_200_OK)
async def get_magazine_by_id(magazine_id: str):
    '''
    # get magazine by id
    '''
    magazine_exists = magazines_collection.get_magazine_by_id(magazine_id)

    if magazine_exists is None:
        raise HTTPException(status_code=404, detail="No magazines found")

    return {
        "id": magazine_exists.get_id(),
        "title": magazine_exists.get_title(),
        "description": magazine_exists.get_description(),
        "roadtrips": [ roadtrip.to_dict() for roadtrip in roadtrips_collection.get_roadtrips_by_magazine_id(magazine_exists.get_id()) ]
    }


@ router.post("/", status_code=status.HTTP_201_CREATED)
async def create_magazine(body: dict, current_user: Annotated[Admin, Depends(check_admin_role)]):
    '''
    # create new magazine
    ### request body
    - title: `str`
    - description: `str`
    - roadtrips_ids: `list[str]`
    '''

    if not body:
        raise HTTPException(status_code=400, detail="Body is required")

    roadtrips = body.get("roadtrips", [])

    for roadtrip_id in roadtrips:
        if roadtrips_collection.get_roadtrip_by_id(roadtrip_id) is None:
            raise HTTPException(status_code=404, detail="Roadtrip not found")

    new_magazine = Magazine(
        title=body.get("title", ""),
        description=body.get("description", ""),
    )
    magazines_collection.add_magazine(new_magazine)

    for roadtrip_id in roadtrips:
        roadtrips_collection.get_roadtrip_by_id(
            roadtrip_id).add_magazine(new_magazine)

    return {
        "detail": "magazine created successfully",
        "magazine_id": new_magazine.get_id()
    }


@router.patch("/{magazine_id}", status_code=status.HTTP_200_OK)
async def update_magazine(magazine_id: str, body: dict, current_user: Annotated[Admin, Depends(check_admin_role)]):
    '''
    #edit magazine by id
    @param magazine_id: `str` id of magazine

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

    magazine_exists.set_title(body.get("title", magazine_exists.get_title()))
    magazine_exists.set_description(
        body.get("description", magazine_exists.get_description()))

    return {
        "detail": "magazine edited successfully",
    }


@router.delete("/{magazine_id}", status_code=status.HTTP_200_OK)
async def delete_roadtrip(magazine_id: str, current_user: Annotated[Admin, Depends(check_admin_role)]):
    '''
    # delete magazine by id
    @param roadtrip_id: `str` id of the roadtrip
    '''
    magazine_exists = magazines_collection.get_magazine_by_id(magazine_id)
    if magazine_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Magazine not found")

    magazines_collection.remove_magazine(magazine_exists)

    return {
        "detail": "magazine deleted successfully",
    }
