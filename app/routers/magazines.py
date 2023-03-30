from fastapi import APIRouter

from app.internal.magazine_catalog import MagazineCatalog
from app.internal.magazine import Magazine

magazines_collection = MagazineCatalog()

router = APIRouter(  # กำหนด instance
    prefix="/magazines",  # กำหนด prefix ของ path
    responses={  # response กรณีที่ค้นหาไม่เจอ
        404: {
            'message': 'Not Found'
        }
    }
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