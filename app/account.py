import uuid

class Account:
    def __init__(self, email, username, password):
        self.__id = str(uuid.uuid4())
        self.__email = email
        self.__username = username
        self.__password = password