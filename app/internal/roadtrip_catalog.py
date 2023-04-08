from .roadtrip import Roadtrip

import re


class RoadtripCatalog:
    def __init__(self):
        self.__roadtrips = []

    def get_roadtrips(self):
        return self.__roadtrips

    def get_roadtrip_by_id(self, roadtrip_id: str):
        for roadtrip in self.get_roadtrips():
            if roadtrip.get_id() == roadtrip_id:
                return roadtrip

        return None

    def get_roadtrips_by_user_id(self, user_id: str):
        return [roadtrip for roadtrip in self.get_roadtrips() if roadtrip.get_author() == user_id]

    def get_roadtrips_by_category(self, category: str):
        return [roadtrip for roadtrip in self.get_roadtrips() if roadtrip.get_category() == category]

    def get_roadtrips_by_keyword(self, keyword: str):
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = set(item for item in self.get_roadtrips() if
                            any(regex.search(attr) for attr in [item.get_title(), item.get_author(), item.get_category()]) or
                            any(regex.search(waypoint.title) for waypoint in item.get_waypoints()))

        return search_result
    
    # loop each roadtrip to check magazine
    # return list of roadtrip that have magazine_id
    def get_roadtrips_by_magazine(self, magazine_id: str):
        result = []
        for roadtrip in self.get_roadtrips():
            each_roadtrip = roadtrip.get_roadtrip_by_magazine(magazine_id)
            if each_roadtrip is None:
                continue
            else:
                result.append(each_roadtrip)
        return result

    def add_roadtrip(self, roadtrip: Roadtrip):
        self.__roadtrips.append(roadtrip)

    def remove_roadtrip(self, roadtrip: Roadtrip):
        self.__roadtrips.remove(roadtrip)
