from .internal.roadtrip_catalog import RoadtripCatalog
from .internal.user_catalog import UserCatalog
from .internal.magazine_catalog import MagazineCatalog
from .internal.review_catalog import ReviewCatalog
from .internal.favorite_catalog import FavoriteCatalog

roadtrips_collection = RoadtripCatalog()
users_collection = UserCatalog()
magazines_collection = MagazineCatalog()
reviews_collection = ReviewCatalog()
favorite_collection = FavoriteCatalog()
