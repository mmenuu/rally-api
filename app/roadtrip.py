class Roadtrip:
    def __init__(self, title, start, end, waypoint, total_waypoint, distance):
        self._title = title
        self._start = start
        self._end = end
        self._waypoint = waypoint
        self._total_waypoint = total_waypoint
        self._distance = distance
    
    def add_waypoint(self, landmark):
        pass

    def remove_waypoint(self, waypoint):
        pass

    def change_waypoint_order(self, waypoint01, waypoint02):
        pass
    
    def edit_waypoint_detail(self, waypoint, text):
        pass