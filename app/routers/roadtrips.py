from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends

from ..databases import roadtrips_collection, magazines_collection, persons_collection
from ..dependencies import get_current_user, User

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
    dependencies=[Depends(get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_roadtrips(user: str | None = None, search: str | None = None):
    if user:
        user_exists = persons_collection.get_person_by_username(user)
        if not user_exists:
            raise HTTPException(status_code=404, detail="User not found")

        return [ roadtrip.to_dict() for roadtrip in roadtrips_collection.get_roadtrips_by_username(user_exists.get_username())]

    return [ roadtrip.to_dict() for roadtrip in roadtrips_collection.get_roadtrips() ]


@router.get("/{roadtrip_id}", status_code=status.HTTP_200_OK)
async def read_roadtrip(roadtrip_id: str):
    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if roadtrip_exists is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    return roadtrip_exists.to_dict()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_roadtrip(body: dict, current_user: Annotated[User, Depends(get_current_user)]):
    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")

    new_roadtrip = Roadtrip(
        author=current_user.get_username(),
    )

    new_roadtrip.set_title(body.get('title', ''))
    new_roadtrip.set_sub_title(body.get('sub_title', ''))
    new_roadtrip.set_description(body.get('description', ''))
    new_roadtrip.set_category(body.get('category', ''))
    new_roadtrip.set_total_distance(body.get('total_distance', 0))
    new_roadtrip.set_total_time(body.get('total_time', 0))
    new_roadtrip.set_summary(body.get('summary', ''))
    new_roadtrip.set_distance_between_waypoints(
        body.get('distance_between_waypoints', []))
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
    if not body:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Body is required")

    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)
    if not roadtrip_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    if roadtrip_exists.get_author() != current_user.get_username():
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
    roadtrip_exists.set_total_distance(
        body.get('total_distance', roadtrip_exists.get_total_distance()))
    roadtrip_exists.set_total_time(
        body.get('total_time', roadtrip_exists.get_total_time()))
    roadtrip_exists.set_distance_between_waypoints(
        body.get('distance_between_waypoints', roadtrip_exists.get_distance_between_waypoints()))
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
async def remove_roadtrip(roadtrip_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    roadtrip_exists = roadtrips_collection.get_roadtrip_by_id(roadtrip_id)

    if not roadtrip_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Roadtrip not found")

    if roadtrip_exists.get_author() != current_user.get_username():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to delete this roadtrip")

    roadtrips_collection.remove_roadtrip(roadtrip_exists)

    return {
        "detail": "Roadtrip deleted successfully",
    }
