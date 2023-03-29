from fastapi import FastAPI
from app.user_catalog import UserCatalog
from app.user import User

app = FastAPI()

user_storage = UserCatalog()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/register")
def register(body: dict):
    new_user = User(email=body["email"],
                    username=body["username"],
                    password=body["password"]
                    )
    
    user_storage.add_user(new_user)

    return {"message": "User created successfully"}


@app.get('/users')
def read_users():
    result = user_storage.get_users()
    return result