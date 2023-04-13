from app.internal.user import User


class UserCatalog:
    def __init__(self):
        self.__users = []

    # Getters
    def get_users(self):
        return self.__users

    def get_user_by_email(self, email: str):
        return next((user for user in self.get_users() if user.get_email() == email), None)

    def get_user_by_username(self, username: str):
        return next((user for user in self.get_users() if user.get_username() == username), None)

    def get_user_by_id(self, user_id: str):
        return next((user for user in self.get_users() if user.get_id() == user_id), None)

    # Setters
    def add_user(self, user: User):
        self.__users.append(user)

    def remove_user(self, user: User):
        self.__users.remove(user)