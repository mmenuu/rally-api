from app.internal.roadtrip import Roadtrip

import re


class RoadtripCatalog:
    def __init__(self):
        self.__roadtrips = []

    def get_roadtrips(self):
        '''Get all roadtrips from the catalog'''
        return self.__roadtrips

    def get_roadtrip_by_id(self, roadtrip_id: str):
        '''Get a roadtrip by roadtrip id from the catalog'''
        for roadtrip in self.get_roadtrips():
            if roadtrip.get_id() == roadtrip_id:
                return roadtrip

        return None  # Roadtrip ID has not been found.

    def get_roadtrips_by_user_id(self, user_id: str):
        '''Get all roadtrips from a user id'''
        return [roadtrip for roadtrip in self.get_roadtrips() if roadtrip.get_author() == user_id]

    def get_roadtrips_by_category(self, category: str):
        '''Get all roadtrips from a category'''
        return [roadtrip for roadtrip in self.get_roadtrips() if roadtrip.get_category() == category]

    def get_roadtrips_by_keyword(self, keyword: str):
        '''Get all roadtrips from a keyword'''
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = set(item for item in self.get_roadtrips() if
                            any(regex.search(attr) for attr in [item.get_title(), item.get_author(), item.get_category()]) or
                            any(regex.search(waypoint.title) for waypoint in item.get_waypoints()))

        return search_result

    def add_roadtrip(self, roadtrip: Roadtrip):
        '''Add a roadtrip to the catalog'''
        self.__roadtrips.append(roadtrip)

    def update_waypoints_by_id(self, roadtrip_id: str, waypoints: list):
        '''Update all waypoints from a roadtrip by roadtrip id'''
        roadtrip = self.get_roadtrip_by_id(roadtrip_id)

        if roadtrip is not None:
            roadtrip.set_waypoints(waypoints)
            return True
        
        return False
        
    def remove_roadtrip_by_id(self, roadtrip_id: str):
        '''Remove a roadtrip by roadtrip id from the catalog'''
        roadtrip = self.get_roadtrip_by_id(roadtrip_id)

        if roadtrip is not None:
            self.__roadtrips.remove(roadtrip)
            return True

        return False
