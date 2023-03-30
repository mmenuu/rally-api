from fastapi import FastAPI
from app.routers import users, magazines

app = FastAPI()

app.include_router(users.router)
app.include_router(magazines.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
