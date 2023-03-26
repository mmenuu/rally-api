class Roadtrip:
    def __init__(self, title, waypoints, author, category):
        self.title = title
        self.waypoints = []
        self.author = author
        self.category = category

    def add_waypoint(self, new_waypoint):
        self.waypoints.append(new_waypoint)

