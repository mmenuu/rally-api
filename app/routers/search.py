from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ..databases import roadtrips_collection, landmarks_collection, accounts_collection
from ..internal.landmark import Landmark
from ..dependencies import get_current_user, User


router = APIRouter(
    prefix="/search",
    tags=["search"],
    responses={
        404: {
            'message': 'Not Found'
        }
    },
    dependencies=[Depends(get_current_user)]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_search(query: str | None = None):
    if query:
      result = [
          {
            **roadtrip.to_dict(),
            'type': 'roadtrip'
          }
          for roadtrip in roadtrips_collection.get_roadtrips_by_keyword(query)

        ] + [
            {
                **landmark.to_dict(),
                'type': 'landmark'
            }
            for landmark in landmarks_collection.get_landmarks_by_keyword(query)
        ] + [
            {
                **account.to_dict(),
                'type': 'user'
            }
            for account in accounts_collection.get_accounts_by_keyword(query)
      ]

      return result
      
    return []