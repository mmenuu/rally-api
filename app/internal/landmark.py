class Landmark:
    '''
    Landmark class

    Attributes:
        id (str): The id of the landmark
        name (str): The name of the landmark
        amenity (str): The amenity of the landmark
        location (list): The location of the landmark
        opening_hours (str): The opening hours of the landmark
    '''

    def __init__(self, id: str, name: str, amenity: str, location: list, opening_hours: str):
        self.__id = id
        self.__name = name
        self.__amenity = amenity
        self.__location = location
        self.__opening_hours = opening_hours

    def get_id(self):
        '''Get the ID of the landmark'''
        return self.__id

    def get_name(self):
        '''Get the name of the landmark'''
        return self.__name

    def get_amenity(self):
        '''Get the amenity of the landmark'''
        return self.__amenity

    def get_location(self):
        '''Get the location of the landmark'''
        return self.__location

    def get_opening_hours(self):
        '''Get the opening hours of the landmark'''
        return self.__opening_hours

    def set_id(self, id):
        '''Set the ID of the landmark'''
        self.__id = id

    def set_name(self, name):
        '''Set the name of the landmark'''
        self.__name = name

    def set_amenity(self, amenity):
        '''Set the amenity of the landmark'''
        self.__amenity = amenity

    def set_location(self, location):
        '''Set the location of the landmark'''
        self.__location = location

    def set_opening_hours(self, opening_hours):
        '''Set the opening hours of the landmark'''
        self.__opening_hours = opening_hours
