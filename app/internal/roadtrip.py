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
        '''Get the ID of the roadtrip'''
        return self.__id

    def get_waypoints(self):
        '''Get all waypoints from the roadtrip'''
        return self.__waypoints

    def get_author(self):
        '''Get the author of the roadtrip'''
        return self.__author

    def get_title(self):
        '''Get the title of the roadtrip'''
        return self.__title

    def get_sub_title(self):
        '''Get the sub title of the roadtrip'''
        return self.__sub_title

    def get_description(self):
        '''Get the description of the roadtrip'''
        return self.__description

    def get_category(self):
        '''Get the category of the roadtrip'''
        return self.__category

    def get_summary(self):
        '''Get the summary of the roadtrip'''
        return self.__summary

    def set_author(self, user_id: str):
        '''Set the author of the roadtrip'''
        self.__author = user_id

    def set_title(self, title: str):
        '''Set the title of the roadtrip'''
        self.__title = title

    def set_sub_title(self, sub_title: str):
        '''Set the sub title of the roadtrip'''
        self.__sub_title = sub_title

    def set_description(self, description: str):
        '''Set the description of the roadtrip'''
        self.__description = description

    def set_waypoints(self, waypoints: list):
        '''Set all waypoints from the roadtrip'''
        self.__waypoints = waypoints

    def set_category(self, category: str):
        '''Set the category of the roadtrip'''
        self.__category = category

    def set_summary(self, summary: str):
        '''Set the summary of the roadtrip'''
        self.__summary = summary

    def get_magazines_id(self):
        '''Get the magazines ID'''
        return self.__magazines_id
    
    def set_magazines_id(self, magazines_id: list):
        '''Set the magazines ID'''
        self.__magazines_id = magazines_id

    def add_magazine_id(self, magazine_id: str):
        '''Add a magazine ID'''
        self.__magazines_id.append(magazine_id)

    def remove_magazine_id(self, magazine_id: str):
        '''Remove a magazine ID'''
        self.__magazines_id.remove(magazine_id)