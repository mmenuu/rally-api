from ..internal.landmark import Landmark


class Waypoint(Landmark):
    def __init__(self, id: str, name: str, amenity: str, location: list, opening_hours: str, note: str, description: str):
        super().__init__(id, name, amenity, location, opening_hours)
        self.__note = note
        self.__description = description

    def get_note(self):
        return self.__note

    def get_description(self):
        return self.__description

    def set_note(self, note: str):
        self.__note = note

    def set_description(self, description: str):
        self.__description = description
