from enum import Enum

class Account:
    def __init__(self, id, email, password, login_status):
        self.__user_id = id
        self.__email = email
        self.__password = password
        self.__login_status = login_status

class User(Account):
    def __init__(self, id, email, password, login_status, username, address):
        super().__init__(id, email, password, login_status)
        self.__username = username
        self.__address = address
        self.__role = "user"
        
class Profile(User):
    def __init__(self, id, email, password, login_status, username, address, bio, profile_image,name):
        super().__init__(id, email, password, login_status, username, address)
        self.__name = name
        self.__bio = bio
        self.__profile_image = profile_image
    
class Admin(Account):
    def __init__(self, id, email, password, login_status):
        super().__init__(id, email, password, login_status)
        self.__role = "admin"
        

class Review:
    def __init__(self, rating, review_text, reviewer_name):
        self._rating = rating
        self._review_text = review_text
        self._reviewer_name = reviewer_name

class Landmark:
    def __init__(self, name, description, latitude, longitude, address, image, type):
        self._name = name
        self._description = description
        self._latitude = latitude
        self._longtitude = longitude
        self._address = address
        self._image = image
        self._type = type
    
    
# มี class ที่มี arttibute เหมือนกัน
class Search:
    def __init__(self):
        pass

class LandmarkCatalog:
    def __init__(self, landmarks):
        self._landmarks = [] # list of landmark object
class FavoriteCatalog:
    def __init__(self, landmarks):
        self._landmarks = [] # list of landmark object

class Waypoint(Landmark):
    def __init__(self, order, name, description, latitude, longitude, address, image, type):
        super().__init__(name, description, latitude, longitude, address, image, type)
        self._order = order

class Roadtrip:
    def __init__(self, title, start, end, waypoint, total_waypoint, distance):
        self._title = title
        self._start = start
        self._end = end
        self._waypoint = waypoint
        self._total_waypoint = total_waypoint
        self._distance = distance

class RoadtripCatalog:
    def __init__(self, roadtrips):
        self._roadtrips = [] # list of roadtrip objects

class RoadtripPage:
    def __init__(self, subtitle, introduction_text, ending_text, waypoints):
        self._subtitle = subtitle
        self._introduction_text = introduction_text
        self._ending_text = ending_text
        self._waypoints = [] # list of waypoints in that roadtrip

class WaypointDetail:
    def __init__(self, waypoint_id, text):
        self._waypoint_id = waypoint_id
        self._text = text

class Magazine:
    def __init__(self, roadtrip, name):
        self._roadtrip = roadtrip
        self._name = name
        
class LandmarkType(Enum):
    outdoor, restaurants, camp, activity, shopping, transportation_service, sport_and_wellness, fuel_and_rest_stop\
    = 1, 2, 3, 4, 5, 6, 7, 8

class Role(Enum):
    user,admin\
    = 0, 1