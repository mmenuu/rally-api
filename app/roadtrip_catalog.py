from roadtrip import Roadtrip

import re

class RoadtripCatalog:
    def __init__(self, roadtrips: None = None | list(Roadtrip)):
        self.__roadtrips = []

    def add_roadtrip(self, roadtrip: Roadtrip):
        '''Add a roadtrip to the catalog'''
        self.__roadtrips.append(roadtrip)

    def get_roadtrips(self):
        '''Get all roadtrips from the catalog'''
        return self.__roadtrips

    def get_roadtrip(self, roadtrip_id: str):
        '''Get a roadtrip by roadtrip id from the catalog'''
        for roadtrip in self.get_roadtrips():
            if roadtrip.get_id() == roadtrip_id:
                return roadtrip

        return None  # Roadtrip ID has not been found.

    def remove_roadtrip(self, roadtrip_id: str):
        '''Remove a roadtrip by roadtrip id from the catalog'''
        roadtrip = self.get_roadtrip(roadtrip_id)

        if roadtrip is not None:
            self.roadtrips.remove(roadtrip)
            return self.roadtrips

        return None

    def get_roadtrips_by_user(self, user_id: str):
        '''Get all roadtrips from a user id'''
        return [roadtrip for roadtrip in self.get_roadtrips() if roadtrip.get_author() == user_id]

    def get_roadtrips_by_category(self, category: str):
        '''Get all roadtrips from a category'''
        return [roadtrip for roadtrip in self.get_roadtrips() if roadtrip.get_category() == category]

    def get_roadtrips_by_keyword(self, keyword: str):
        '''Get all roadtrips from a keyword'''
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = [item for item in self.get_roadtrips()
                         if regex.search(item.get_title()) or
                         regex.search(item.get_author()) or
                         regex.search(item.get_category()) or
                         [waypoint for waypoint in item.get_waypoints() if regex.search(waypoint.title)]]

        return search_result
