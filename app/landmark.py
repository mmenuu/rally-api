class Landmark:
    def __init__(self, name, description, latitude, longitude, address, image, type):
        self._name = name
        self._description = description
        self._latitude = latitude
        self._longtitude = longitude
        self._address = address
        self._image = image
        self._type = type

    def create_landmarkpage(self):
        pass

    def get_landmarkpage(self, landmark): # maybe call from landmark catalog to landmark and ask for landmarkpage
        pass
