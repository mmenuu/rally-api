from user import User

class Profile(User):
    def __init__(self, id, email, password, login_status, username, address, bio, profile_image,name):
        super().__init__(id, email, password, login_status, username, address)
        self.__name = name
        self.__bio = bio
        self.__profile_image = profile_image