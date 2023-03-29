from app.internal.roadtrip import Roadtrip
import uuid

class Magazine:
    def __init__(self, id: str, roadtrip: Roadtrip, name, description):
        self.__id = str(uuid.uuid4())
        self.__roadtrip = roadtrip
        self.__name = name
        self.__description = description

    def set_magazine_roadtrip(self, roadtrip: Roadtrip):
        self.__roadtrip = roadtrip
    
    def set_magazine_name(self, name: str):
        self.__name = name
        
    def set_magazine_description(self, text: str):
        self.__description = text

    def get_magazine_roadtrip(self):
        return self.__roadtrip
    
    def get_magazine_name(self):
        return self.__name

    def get_magazine_id(self):
        return self.__id

