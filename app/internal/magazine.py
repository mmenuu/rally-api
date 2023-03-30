from app.internal.roadtrip import Roadtrip
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

    def get_roadtrip_by_id(self, roadtrip_id: str):
        for roadtrip in self.get_roadtrips():
            if roadtrip == roadtrip_id:
                return roadtrip

        return None

    def add_roadtrip(self, roadtrip_id: str):
        self.__roadtrips.append(roadtrip_id)

    def remove_roadtrip(self, roadtrip_id: str):
        roadtrip = self.get_roadtrip_by_id(roadtrip_id)
        if roadtrip is not None:
            self.__roadtrips.remove(roadtrip)

        return False
