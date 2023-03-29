class Waypoint:
    '''Class for a waypoint in a roadtrip'''

    def __init__(self, id: str, name: str, description: str, position: list(float), note: str, amenity: str):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__position = position
        self.__note = note
        self.__amenity = amenity

    def get_id(self):
        '''Get the ID of the waypoint'''
        return self.__id

    def get_name(self):
        '''Get the name of the waypoint'''
        return self.__name

    def get_description(self):
        '''Get the description of the waypoint'''
        return self.__description

    def get_position(self):
        '''Get the position [lag, long] of the waypoint'''
        return self.__position

    def get_note(self):
        '''Get the note of the waypoint'''
        return self.__note

    def get_amenity(self):
        '''Get the amenity of the waypoint'''
        return self.__amenity

    def set_id(self, id: str):
        '''Set the ID of the waypoint'''
        self.__id = id

    def set_name(self, name: str):
        '''Set the name of the waypoint'''
        self.__name = name

    def set_description(self, description: str):
        '''Set the description of the waypoint'''
        self.__description = description

    def set_position(self, position: list(float)):
        '''Set the position [lag, long] of the waypoint'''
        self.__position = position

    def set_note(self, note: str):
        '''Set the note of the waypoint'''
        self.__note = note

    def set_amenity(self, amenity: str):
        '''Set the amenity of the waypoint'''
        self.__amenity = amenity

    def __str__(self):
        return f'Waypoint: {self.get_id()}\n name: {self.get_name()}\n description: {self.get_description()}\n pos: {self.get_position()}\n note: {self.get_note()}\n amenity: {self.get_amenity()}'