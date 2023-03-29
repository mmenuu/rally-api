from fastapi import APIRouter

from app.internal.user_catalog import UserCatalog
from app.internal.user import User

user_storage = UserCatalog()

router = APIRouter(  # กำหนด instance
    prefix="/users",
    responses={  # response กรณีที่ค้นหาไม่เจอ
        404: {
            'message': 'Not Found'
        }
    }
)


@router.post("/")
async def register(body: dict):
    new_user = User(
        email=body["email"],
        username=body["username"],
        password=body["password"]
    )

    user_storage.add_user(new_user)

    return {"message": "User created successfully"}


@router.get('/')
async def read_users():
    result = user_storage.get_users()
    return result
