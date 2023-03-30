from fastapi import FastAPI
<<<<<<< HEAD
from app.routers import users, reviews
=======

from .routers import users, auth, roadtrips
>>>>>>> b92ec929d545db498b82b15918b5c38bc99fa691

app = FastAPI()

app.include_router(users.router)
<<<<<<< HEAD
app.include_router(reviews.router)
=======
app.include_router(auth.router)
app.include_router(roadtrips.router)
>>>>>>> b92ec929d545db498b82b15918b5c38bc99fa691

@app.get("/")
def read_root():
    return {"Hello": "world"}