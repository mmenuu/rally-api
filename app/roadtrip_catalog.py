from roadtrip import Roadtrip

import re


class RoadtripCatalog:
    def __init__(self, roadtrips=None | list(Roadtrip)):
        self.roadtrips = []

    def add_roadtrip(self, roadtrip: Roadtrip):
        self.roadtrips.append(roadtrip)

    def get_roadtrip(self, roadtrip_id: str):
        for roadtrip in self.roadtrips:
            if roadtrip.id == roadtrip_id:
                return roadtrip

        return None  # ERROR: Roadtrip not found

    def remove_roadtrip(self, roadtrip_id):
        roadtrip = self.get_roadtrip(roadtrip_id)

        if roadtrip is not None:
            self.roadtrips.remove(roadtrip)
            return self.roadtrips

        return None

    def get_all_roadtrips(self):
        return self.roadtrips

    def get_roadtrips_by_user(self, user_id: str):
        return [roadtrip for roadtrip in self.roadtrips if roadtrip.user_id == user_id]
    
    def get_roadtrips_by_category(self, category: str):
        return [roadtrip for roadtrip in self.roadtrips if roadtrip.category == category]
    
    def get_roadtrips_by_keyword(self, keyword: str):
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = [item for item in self.roadtrips
                         if regex.search(item.title) or
                         regex.search(item.author) or
                         regex.search(item.category) or
                         [waypoint for waypoint in item.waypoints if regex.search(waypoint.title)]]

        return search_result
