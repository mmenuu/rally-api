from account import Account

class User(Account):
    def __init__(self, id, email, password, login_status, username, address):
        super().__init__(id, email, password, login_status)
        self.__username = username
        self.__address = address
        self.__role = "user"
    
    def new_roadtrip(self, landmark, landmark): # for marking start and and endpoint of roadtrip
        pass

    def create_roadtrip(self, roadtrip, landmark): # for pulling or create new roadtrip from zero
        pass

    def add_favorite_landmark(self, landmark):
        pass

    def remove_favorite_landmark(self, landmark):
        pass
    
    def change_waypoint_order(self, waypoint01, waypoint02):
        pass
    
    def edit_waypoint_detail(self, roadtrip, waypoint, text):
        pass

    def get_favoritelandmark(self):
        pass

    def get_userroadtrip(self):
        pass

    def edit_user(self, section):
        pass