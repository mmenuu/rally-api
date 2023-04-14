
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users, auth, roadtrips, magazines, favorites, reviews, landmarks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Authorization"]
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(magazines.router)
app.include_router(roadtrips.router)
app.include_router(landmarks.router)
app.include_router(reviews.router)

app.include_router(favorites.router)


@app.get("/")
def read_root():
    return {"Hello": "world"}
