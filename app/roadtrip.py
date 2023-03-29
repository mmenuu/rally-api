from waypoint import Waypoint

class Roadtrip:
    def __init__(self,  id: str,user_id: str, title: str, sub_title: str, description: str, waypoints: list(Waypoint), category: str, summary: str):
        self.__id = id
        self.__author = user_id
        self.__title = title
        self.__sub_title = sub_title
        self.__description = description
        self.__waypoints = waypoints
        self.__category = category
        self.__summary = summary

    def add_waypoint(self, new_waypoint: Waypoint):
        self.waypoints.append(new_waypoint)

    def get_waypoint(self, waypoint_id: str):
        for waypoint in self.waypoints:
            if waypoint.id == waypoint_id:
                return waypoint

        return None  # ERROR: Waypoint not found

    def get_waypoints(self):
        return self.waypoints

    def update_waypoint(self, new_waypoints: list(Waypoint)):
        self.waypoints = new_waypoints

    def remove_waypoint(self, waypoint_id: str):
        waypoint = self.get_waypoint(waypoint_id)

        if waypoint is not None:
            return self.waypoints.remove(waypoint)

        return None  # ERROR: Waypoint not found