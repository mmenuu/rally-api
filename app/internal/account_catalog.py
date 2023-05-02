from .user import User
from .admin import Admin
import re

class AccountCatalog:
    def __init__(self):
        self.__users = []

    # Getters
    def get_accounts(self):
        return self.__users

    def get_account_by_email(self, email: str):
        return next((user for user in self.get_accounts() if user.get_email() == email), None)

    def get_account_by_username(self, username: str):
        return next((user for user in self.get_accounts() if user.get_username() == username), None)

    def get_account_by_id(self, user_id: str):
        return next((user for user in self.get_accounts() if user.get_id() == user_id), None)

    # Setters
    def add_account(self, user: User | Admin):
        self.__users.append(user)

    def remove_account(self, user: User | Admin):
        self.__users.remove(user)
    
    def get_accounts_by_keyword(self, keyword: str):
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = set(item for item in self.__users if any(regex.search(attr) for attr in [item.get_email(), item.get_username(), item.get_id()]))

        return search_result