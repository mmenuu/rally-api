from .internal.roadtrip_catalog import RoadtripCatalog
from .internal.user_catalog import UserCatalog
from .internal.magazine_catalog import MagazineCatalog
from .internal.review_catalog import ReviewCatalog

from .internal.user import User
from .utils import get_password_hash

roadtrips_collection = RoadtripCatalog()
users_collection = UserCatalog()
magazines_collection = MagazineCatalog()
reviews_collection = ReviewCatalog()

fake_user = {
    "username": "1tpp",
    "password": get_password_hash("1"),
    "email": "1tpp@gmail.com"
}

users_collection.add_user(User(**fake_user))
