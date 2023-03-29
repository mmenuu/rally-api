from fastapi import FastAPI
from app.routers import users, favorites

app = FastAPI()
app.include_router(users.router)
app.include_router(favorites.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}