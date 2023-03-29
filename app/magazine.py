from roadtrip import Roadtrip
class Magazine:
    def __init__(self, id: str, roadtrip: Roadtrip, name, description):
        self._id = id
        self._roadtrip = roadtrip
        self._name = name
        self._description = description

    def set_magazine_roadtrip(self, roadtrip: Roadtrip):
        self._roadtrip = roadtrip
    
    def set_magazine_name(self, name: str):
        self._name = name
        
    def set_magazine_description(self, text: str):
        self._description = text

    def get_magazine_id(self):
        return self._id

