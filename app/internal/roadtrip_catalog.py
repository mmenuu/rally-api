import re


class RoadtripCatalog:
    def __init__(self):
        self.__roadtrips = []

    # Getters
    def get_roadtrips(self):
        return self.__roadtrips

    # Setters
    def add_roadtrip(self, roadtrip):
        self.__roadtrips.append(roadtrip)

    def remove_roadtrip(self, roadtrip):
        self.__roadtrips.remove(roadtrip)

    # Utility methods
    def get_roadtrip_by_id(self, roadtrip_id: str):
        return next((roadtrip for roadtrip in self.__roadtrips if roadtrip.get_id() == roadtrip_id), None)

    def get_roadtrips_by_user_id(self, user_id: str):
        return [roadtrip for roadtrip in self.__roadtrips if roadtrip.get_author() == user_id]

    def get_roadtrips_by_category(self, category: str):
        return [roadtrip for roadtrip in self.__roadtrips if roadtrip.get_category() == category]

    def get_roadtrips_by_keyword(self, keyword: str):
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = set(item for item in self.__roadtrips if
                            any(regex.search(attr) for attr in [item.get_title(), item.get_author(),
                                                                item.get_category()]) or
                            any(regex.search(waypoint.title) for waypoint in item.get_waypoints()))

        return search_result

    def get_roadtrips_by_magazine_id(self, magazine_id: str):
        return [roadtrip for roadtrip in self.__roadtrips if magazine_id in roadtrip.get_magazines_id()]
