from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import roadtrips_collection, magazines_collection, users_collection
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
async def read_roadtrips(user: str | None = None):
    '''
    # Get all roadtrips
    '''

    if user:
        user_exists = users_collection.get_user_by_username(user)
        if not user_exists:
            raise HTTPException(status_code=404, detail="User not found")

        return [
            {
                'id': roadtrip.get_id(),
                'title': roadtrip.get_title(),
                'sub_title': roadtrip.get_sub_title(),
                'author': roadtrip.get_author(),
                'waypoints': [
                    {
                        'id': waypoint.get_id(),
                        'name': waypoint.get_name(),
                        'description': waypoint.get_description(),
                        'position': waypoint.get_position(),
                        'note': waypoint.get_note(),
                    } for waypoint in roadtrip.get_waypoints()
                ],
                'magazines': roadtrip.get_magazines_id(),
                'category': roadtrip.get_category(),
                'summary': roadtrip.get_summary()
            }
            for roadtrip in roadtrips_collection.get_roadtrips_by_user_id(user_exists.get_id())
        ]

    return [
        {
            'id': roadtrip.get_id(),
            'title': roadtrip.get_title(),
            'sub_title': roadtrip.get_sub_title(),
            'author': roadtrip.get_author(),
            'waypoints': [
                {
                    'id': waypoint.get_id(),
                    'name': waypoint.get_name(),
                    'description': waypoint.get_description(),
                    'position': waypoint.get_position(),
                    'note': waypoint.get_note(),
                } for waypoint in roadtrip.get_waypoints()
            ],
            'magazines': roadtrip.get_magazines_id(),
            'category': roadtrip.get_category(),
            'summary': roadtrip.get_summary()
        }
        for roadtrip in roadtrips_collection.get_roadtrips()
    ]


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

    return {
        'id': roadtrip_exists.get_id(),
        'title': roadtrip_exists.get_title(),
        'sub_title': roadtrip_exists.get_sub_title(),
        'description': roadtrip_exists.get_description(),
        'waypoints': [
            {
                'id': waypoint.get_id(),
                'name': waypoint.get_name(),
                'description': waypoint.get_description(),
                'position': waypoint.get_position(),
                'note': waypoint.get_note(),
            } for waypoint in roadtrip_exists.get_waypoints()
        ],
        'magazines': roadtrip_exists.get_magazines_id(),
        'category': roadtrip_exists.get_category(),
        'summary': roadtrip_exists.get_summary(),
        'author': roadtrip_exists.get_author()
    }


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
        "roadtrip_id": new_roadtrip.get_id()
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
    - waypoints: `list` optional
    - magazine_id: `str` optional
    '''

    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if not roadtrip_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    if roadtrip_exists.get_author() != current_user.get_id():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to update this roadtrip")

    # Update Roadtrip attributes with values from the request body
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

    if body.get('magazine_id'):
        magazine_id = body.get('magazine_id')
        magazine_exists = magazines_collection.get_magazine_by_id(magazine_id)
        if not magazine_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Magazine not found")

        if magazine_id not in roadtrip_exists.get_magazines_id():
            roadtrip_exists.add_magazine_id(magazine_id)
        else:
            roadtrip_exists.remove_magazine_id(magazine_id)

    return {
        "detail": "Roadtrip updated successfully",
    }


@router.delete("/{roadtrip_id}", status_code=status.HTTP_200_OK)
async def remove_roadtrip(roadtrip_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    '''
    # Remove a roadtrip

    @param roadtrip_id: `str` id of the roadtrip
    '''

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if not roadtrip_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    if roadtrip_exists.get_author() != current_user.get_id():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to delete this roadtrip")

    roadtrips_collection.remove_roadtrip(roadtrip_exists)

    return {
        "detail": "Roadtrip deleted successfully",
    }
