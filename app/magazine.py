from roadtrip import Roadtrip
class Magazine:
    def __init__(self, id: str, roadtrip: Roadtrip, name, description):
        self._id = id
        self._roadtrip = roadtrip
        self._name = name
        self._description = description

    def edit_roadtrip(self, roadtrip):
        self._roadtrip = roadtrip
    
    def edit_roadtrip(self, name):
        self._name = name
        
    def edit_description(self, text):
        self._description = text

    def get_magazine_id(self):
        return self._id

