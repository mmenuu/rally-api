from ..internal.landmark import Landmark


class Waypoint(Landmark):
    '''Class for a waypoint in a roadtrip'''

    def __init__(self, id: str, name: str, amenity: str, location: list, opening_hours: str, note: str, description: str):
        super().__init__(id, name, amenity, location, opening_hours)
        self.__note = note
        self.__description = description

    def get_note(self):
        '''Get the note of the waypoint'''
        return self.__note

    def get_description(self):
        '''Get the description of the waypoint'''
        return self.__description

    def set_note(self, note: str):
        '''Set the note of the waypoint'''
        self.__note = note

    def set_description(self, description: str):
        '''Set the description of the waypoint'''
        self.__description = description
