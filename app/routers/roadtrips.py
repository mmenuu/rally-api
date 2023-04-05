from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import roadtrips_collection
from ..dependencies import get_token_header
from ..internal.roadtrip import Roadtrip
from ..internal.waypoint import Waypoint

router = APIRouter(
    prefix="/roadtrips",
    tags=["roadtrips"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_token_header)]
)


@router.get("/")
async def read_roadtrips():
    '''
    # Get all roadtrips
    '''
    roadtrips_exits = roadtrips_collection.get_roadtrips()
    if not roadtrips_exits:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No roadtrips found")
    return roadtrips_exits


@router.get("/{roadtrip_id}")
async def read_roadtrip(roadtrip_id: str):
    '''
    # Get a roadtrip by id
    '''
    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    return roadtrip_exists


@router.post("/", status_code=status.HTTP_201_CREATED)
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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")
    if not body['user_id']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User id is required")

    new_roadtrip = Roadtrip(
        user_id=body['user_id']
    )

    if body['title']:
        new_roadtrip.set_title(body['title'])
    if body['sub_title']:
        new_roadtrip.set_sub_title(body['sub_title'])
    if body['description']:
        new_roadtrip.set_description(body['description'])
    if body['category']:
        new_roadtrip.set_category(body['category'])
    if body['summary']:
        new_roadtrip.set_summary(body['summary'])

    roadtrips_collection.add_roadtrip(new_roadtrip)

    return {
        "detail": "Roadtrip created successfully",
    }


@router.patch("/{roadtrip_id}")
async def update_roadtrip(roadtrip_id: str, body: dict):
    '''
    # Update a roadtrip
    ### request body
    - title: `str` optional
    - sub_title: `str` optional
    - description: `str` optional
    - category: `str` optional
    - summary: `str` optional
    - user_id: `str` required
    '''

    # validate body
    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")
    if not body['user_id']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User id is required")

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    if body['title']:
        roadtrip_exists.set_title(body['title'])
    if body['sub_title']:
        roadtrip_exists.set_sub_title(body['sub_title'])
    if body['description']:
        roadtrip_exists.set_description(body['description'])
    if body['category']:
        roadtrip_exists.set_category(body['category'])
    if body['summary']:
        roadtrip_exists.set_summary(body['summary'])

    roadtrips_collection.update_roadtrip(
        roadtrip_exists.get_id(), roadtrip_exists)

    return {
        "detail": "Roadtrip updated successfully",
    }


@router.get("/{roadtrip_id}/waypoints")
async def read_roadtrip_waypoints(roadtrip_id: str):
    '''
    # Get a roadtrip waypoints by id
    '''
    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    return roadtrip_exists.get_waypoints()


@router.patch("/{roadtrip_id}/waypoints")
async def update_roadtrip_waypoints(roadtrip_id: str, body: dict):
    '''
    # Update a roadtrip waypoints
    ### request body
    - waypoints: `list` required
    '''

    # validate body
    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")
    if not body['waypoints']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Waypoints are required")

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    waypoints = []
    for waypoint in body['waypoints']:
        waypoints.append(Waypoint(
            id=waypoint['id'],
            name=waypoint['name'],
            position=waypoint['position'],
            description=waypoint['description'],
            note=waypoint['note'],
            amenity=waypoint['amenity'],
        ))

    roadtrips_collection.update_waypoints_by_id(roadtrip_id, waypoints)

    return {
        "detail": "Roadtrip waypoints updated successfully",
    }


@ router.delete("/{roadtrip_id}")
async def delete_roadtrip(roadtrip_id: str):

    if not roadtrips_collection.remove_roadtrip_by_id(roadtrip_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    return {
        "detail": "Roadtrip deleted successfully",
    }
