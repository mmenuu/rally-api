class Waypoint(Landmark):
    def __init__(self, order, name, description, latitude, longitude, address, image, type):
        super().__init__(name, description, latitude, longitude, address, image, type)
        self._order = order

    
    def edit_waypoint_detail(self, text):
        pass