from typing import List
from .user import User
from .admin import Admin
import re


class PersonCatalog:
    def __init__(self):
        self.__users: List[User | Admin] = []

    # Getters
    def get_persons(self) -> List[User | Admin]:
        return self.__users

    def get_person_by_email(self, email: str) -> User | Admin | None:
        return next((user for user in self.get_persons() if user.get_email() == email), None)

    def get_person_by_username(self, username: str) -> User | Admin | None:
        return next((user for user in self.get_persons() if user.get_username() == username), None)

    def get_person_by_id(self, user_id: str) -> User | Admin | None:
        return next((user for user in self.get_persons() if user.get_id() == user_id), None)

    # Setters
    def add_person(self, user: User | Admin) -> None:
        self.__users.append(user)

    def remove_person(self, user: User | Admin) -> None:
        self.__users.remove(user)

    def get_persons_by_keyword(self, keyword: str) -> set[User | Admin]:
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = set(item for item in self.__users if any(regex.search(
            attr) for attr in [item.get_email(), item.get_username(), item.get_id()]))

        return search_result
