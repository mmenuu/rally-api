from .waypoint import Waypoint
import uuid

class Roadtrip:
    '''A roadtrip is a collection of waypoints'''

    def __init__(self, user_id: str):
        self.__id = str(uuid.uuid4())
        self.__author = user_id
        self.__title = ''
        self.__sub_title = ''
        self.__description = ''
        self.__waypoints = list()
        self.__magazines_id = list()
        self.__category = ''
        self.__summary = ''

    def get_id(self):
        return self.__id

    def get_waypoints(self):
        return self.__waypoints

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_sub_title(self):
        return self.__sub_title

    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category

    def get_summary(self):
        return self.__summary

    def set_author(self, user_id: str):
        self.__author = user_id

    def set_title(self, title: str):
        self.__title = title

    def set_sub_title(self, sub_title: str):
        self.__sub_title = sub_title

    def set_description(self, description: str):
        self.__description = description

    def set_waypoints(self, waypoints: list):
        self.__waypoints = waypoints

    def set_category(self, category: str):
        self.__category = category

    def set_summary(self, summary: str):
        self.__summary = summary

    def get_magazines_id(self):
        return self.__magazines_id

    def get_magazine_by_id(self, magazine_id: str):
        for magazine in self.get_magazines_id():
            if magazine == magazine_id:
                return magazine

        return None

    def add_magazine_id(self, magazine_id: str):
        self.__magazines_id.append(magazine_id)

    def remove_magazine_id(self, magazine_id: str):
        self.__magazines_id.remove(magazine_id)