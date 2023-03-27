import re
class RoadtripCatalog:
    def __init__(self, roadtrips = None | list):
        self.roadtrips = []

    def add_roadtrip(self, roadtrip):
        self.roadtrips.append(roadtrip)

    def search(self, keyword):
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = [item for item in self.roadtrips \
            if regex.search(item.title) or \
                regex.search(item.author) or \
                regex.search(item.category) or \
                [waypoint for waypoint in item.waypoints if regex.search(waypoint.title)]]

        return search_result
