class Landmark:
    def __init__(self, id: str, name: str, amenity: str, position: list, opening_hours: str):
        self.__id = id
        self.__name = name
        self.__amenity = amenity
        self.__position = position
        self.__opening_hours = opening_hours

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_amenity(self):
        return self.__amenity

    def get_position(self):
        return self.__position

    def get_opening_hours(self):
        return self.__opening_hours