class Landmark:
    def __init__(self, id: str, name: str, amenity: str, location: list, opening_hours=str):
        self.__id = id
        self.__name = name
        self.__amenity = amenity
        self.__location = location
        self.__opening_hours = opening_hours

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_amenity(self):
        return self.__amenity

    def get_location(self):
        return self.__location

    def get_opening_hours(self):
        return self.__opening_hours

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_amenity(self, amenity):
        self.__amenity = amenity

    def set_location(self, location):
        self.__location = location

    def set_opening_hours(self, opening_hours):
        self.__opening_hours = opening_hours