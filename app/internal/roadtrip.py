from .waypoint import Waypoint
from .magazine import Magazine
import uuid


class Roadtrip: 
    '''A roadtrip is a collection of waypoints'''

    def __init__(self, author: str):
        self.__id = str(uuid.uuid4())
        self.__author = author
        self.__title = ''
        self.__sub_title = ''
        self.__description = ''
        self.__waypoints = list()
        self.__distance_between_waypoints = list()
        self.__total_distance = 0
        self.__total_time = 0
        self.__magazines = list() # pointer to magazines
        self.__category = ''
        self.__summary = ''

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_waypoints(self) -> list[Waypoint]:
        return self.__waypoints

    def get_total_distance(self) -> float:
        return self.__total_distance

    def get_total_time(self) -> float:
        return self.__total_time

    def get_author(self) -> str:
        return self.__author

    def get_title(self) -> str:
        return self.__title

    def get_sub_title(self) -> str:
        return self.__sub_title

    def get_description(self) -> str:
        return self.__description

    def get_distance_between_waypoints(self) -> list:
        return self.__distance_between_waypoints

    def get_category(self) -> str:
        return self.__category

    def get_summary(self) -> str:
        return self.__summary

    def get_magazines(self) -> list[Magazine]:
        return self.__magazines

    # Setters
    def set_title(self, title: str) -> None:
        self.__title = title

    def set_sub_title(self, sub_title: str) -> None:
        self.__sub_title = sub_title

    def set_description(self, description: str) -> None:
        self.__description = description

    def set_waypoints(self, waypoints: list) -> None:
        self.__waypoints = waypoints

    def set_distance_between_waypoints(self, distance_between_waypoints: list) -> None:
        self.__distance_between_waypoints = distance_between_waypoints

    def set_total_distance(self, total_distance: int) -> None:
        self.__total_distance = total_distance

    def set_total_time(self, total_time: int) -> None:
        self.__total_time = total_time

    def set_category(self, category: str) -> None:
        self.__category = category

    def set_summary(self, summary: str) -> None:
        self.__summary = summary

    def add_magazine(self, magazine: Magazine) -> None:
        self.__magazines.append(magazine)

    def remove_magazine(self, magazine: Magazine) -> None:
        self.__magazines.remove(magazine)

    # Utility methods
    def get_magazine_by_id(self, magazine_id: str) -> Magazine | None:
        return next((magazine for magazine in self.__magazines if magazine.get_id() == magazine_id), None)

    def to_dict(self) -> dict:
        return {
            'id': self.__id,
            'author': self.__author,
            'title': self.__title,
            'sub_title': self.__sub_title,
            'description': self.__description,
            'waypoints': [waypoint.to_dict() for waypoint in self.__waypoints],
            'distance_between_waypoints': self.__distance_between_waypoints,
            'total_distance': self.__total_distance,
            'total_time': self.__total_time,
            'category': self.__category,
            'magazines': [magazine.to_dict() for magazine in self.__magazines],
            'summary': self.__summary,
        }