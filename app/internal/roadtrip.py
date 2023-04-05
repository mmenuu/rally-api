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

    def add_waypoint(self, new_waypoint: Waypoint):
        '''Add a waypoint to the roadtrip'''
        self.__waypoints.append(new_waypoint)

    def get_waypoint_by_id(self, waypoint_id: str):
        '''Get a waypoint from the roadtrip'''
        for waypoint in self.get_waypoints():
            if waypoint.get_id() == waypoint_id:
                return waypoint

        return None  # Waypoint ID has not been found.
    
    def remove_waypoint_by_id(self, waypoint_id: str):
        '''Remove a waypoint from the roadtrip'''
        waypoint = self.get_waypoint_by_id(waypoint_id)

        if waypoint is not None:
            self.__waypoints.remove(waypoint)
            return True

        return False  # Waypoint ID has not been found.