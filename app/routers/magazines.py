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
    new_magazine = Magazine(
        name = body["name"],
        description = body["description"]
    )

    magazines_collection.add_magazine(new_magazine)
    return {"message": "User created successfully"}

@router.get("/")
async def read_magazine():
    result = magazines_collection.get_magazines()
    return result