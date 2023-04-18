from .internal.roadtrip_catalog import RoadtripCatalog
from .internal.account_catalog import AccountCatalog
from .internal.magazine_catalog import MagazineCatalog
from .internal.landmark_catalog import LandmarkCatalog

from .internal.user import User
from .internal.admin import Admin
from .utils import get_password_hash

roadtrips_collection = RoadtripCatalog()
accounts_collection = AccountCatalog()
magazines_collection = MagazineCatalog()
landmarks_collection = LandmarkCatalog()

fake_user = {
    "username": "1tpp",
    "password": get_password_hash("1"),
    "email": "1tpp@gmail.com"
}

fake_admin = {
    "username": "admin",
    "password": get_password_hash("admin"),
    "email": "admin@gmail.com"
}


accounts_collection.add_account(User(**fake_user))
accounts_collection.add_account(Admin(**fake_admin))