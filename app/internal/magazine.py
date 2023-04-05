from app.internal.roadtrip import Roadtrip
from app.internal.roadtrip_catalog import RoadtripCatalog
import uuid

class Magazine:
    def __init__(self, name, description):
        self.__id = str(uuid.uuid4())
        self.__roadtrips = [] # list of roadtrip id
        self.__name = name
        self.__description = description

    def set_name(self, name: str):
        self.__name = name

    def set_description(self, text: str):
        self.__description = text

    def get_roadtrips(self):
        return self.__roadtrips

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_id(self):
        return self.__id