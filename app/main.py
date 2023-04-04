from fastapi import FastAPI

from .routers import users, auth, roadtrips, magazines, reviews, favorites

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(magazines.router)
app.include_router(roadtrips.router)
app.include_router(reviews.router)
app.include_router(favorites.router)


@app.get("/")
def read_root():
    return {"Hello": "world"}
