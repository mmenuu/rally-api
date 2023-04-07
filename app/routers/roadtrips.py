from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import roadtrips_collection
from ..dependencies import get_current_user

from ..internal.roadtrip import Roadtrip
from ..internal.waypoint import Waypoint
from ..internal.user import User

router = APIRouter(
    prefix="/roadtrips",
    tags=["roadtrips"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_roadtrips():
    '''
    # Get all roadtrips
    '''
    roadtrips_exits = roadtrips_collection.get_roadtrips()
    return roadtrips_exits


@router.get("/{roadtrip_id}", status_code=status.HTTP_200_OK)
async def read_roadtrip(roadtrip_id: str):
    '''
    # Get a roadtrip by id
    @param roadtrip_id: `str` id of the roadtrip
    '''
    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    return roadtrip_exists


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_roadtrip(body: dict, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Create a new roadtrip

    ### request body
    - title: `str`
    - sub_title: `str`
    - description: `str`
    - category: `str`
    - summary: `str`
    '''

    # validate body
    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")

    new_roadtrip = Roadtrip(
        user_id=current_user.get_id(),
    )

    new_roadtrip.set_title(body.get('title', ''))
    new_roadtrip.set_sub_title(body.get('sub_title', ''))
    new_roadtrip.set_description(body.get('description', ''))
    new_roadtrip.set_category(body.get('category', ''))
    new_roadtrip.set_summary(body.get('summary', ''))
    if body.get('waypoints'):
        try:
            waypoints = [Waypoint(**waypoint)
                         for waypoint in body['waypoints']]
            new_roadtrip.set_waypoints(waypoints)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid waypoints: {e}")

    roadtrips_collection.add_roadtrip(new_roadtrip)

    return {
        "detail": "Roadtrip created successfully",
    }


@router.patch("/{roadtrip_id}", status_code=status.HTTP_200_OK)
async def update_roadtrip(roadtrip_id: str, body: dict, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Update a roadtrip
    @param roadtrip_id: `str` id of the roadtrip

    ### request body
    - title: `str` optional
    - sub_title: `str` optional
    - description: `str` optional
    - category: `str` optional
    - summary: `str` optional
    '''

    # validate body
    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)
    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")\

    if roadtrip_exists.get_author() != current_user.get_id():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to update this roadtrip")

    roadtrip_exists.set_title(body.get('title', roadtrip_exists.get_title()))
    roadtrip_exists.set_sub_title(
        body.get('sub_title', roadtrip_exists.get_sub_title()))
    roadtrip_exists.set_description(
        body.get('description', roadtrip_exists.get_description()))
    roadtrip_exists.set_category(
        body.get('category', roadtrip_exists.get_category()))
    roadtrip_exists.set_summary(
        body.get('summary', roadtrip_exists.get_summary()))
    if body.get('waypoints'):
        try:
            waypoints = [Waypoint(**waypoint)
                         for waypoint in body['waypoints']]
            roadtrip_exists.set_waypoints(waypoints)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid waypoints: {e}")

    return {
        "detail": "Roadtrip updated successfully",
    }


@router.delete("/{roadtrip_id}", status_code=status.HTTP_200_OK)
async def delete_roadtrip(roadtrip_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Delete a roadtrip

    @param roadtrip_id: `str` id of the roadtrip
    '''

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)
    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    if roadtrip_exists.get_author() != current_user.get_id():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to delete this roadtrip")

    roadtrips_collection.remove_roadtrip(roadtrip_exists)

    return {
        "detail": "Roadtrip deleted successfully",
    }
