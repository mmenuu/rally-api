class Waypoint:
    def __init__(self, id: str, name: str, description: str, position: list(float), note: str, amenity: str):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__position = position
        self.__note = note
        self.__amenity = amenity

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_position(self):
        return self.__position
    
    def get_note(self):
        return self.__note
    
    def get_amenity(self):
        return self.__amenity
    
    def set_id(self, id: str):
        self.__id = id
    
    def set_name(self, name: str):
        self.__name = name
    
    def set_description(self, description: str):
        self.__description = description
    
    def set_position(self, position: list(float)):
        self.__position = position

    def set_note(self, note: str):
        self.__note = note

    def set_amenity(self, amenity: str):
        self.__amenity = amenity