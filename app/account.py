import uuid

class Account:
    def __init__(self, email, username, password):
        self.__id = str(uuid.uuid4())
        self.__email = email
        self.__username = username
        self.__password = password

    def get_id(self):
        return self.__id
    
    def get_email(self):
        return self.__email
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def set_email(self, email):
        self.__email = email

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password