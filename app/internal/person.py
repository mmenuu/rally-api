import uuid

class Person:
    def __init__(self, email, username, password):
        self.__id = str(uuid.uuid4())
        self.__email = email
        self.__username = username
        self.__password = password

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_email(self) -> str:
        return self.__email

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    # Setters
    def set_email(self, email) -> None:
        self.__email = email

    def set_username(self, username) -> None:
        self.__username = username

    def set_password(self, password) -> None:
        self.__password = password

    def to_dict(self) -> dict:
        return {
            'id': self.__id,
            'email': self.__email,
            'username': self.__username,
            'password': self.__password
        }