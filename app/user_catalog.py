from user import User

class UserCatalog:
    def __init__(self):
        self.__users = [User]
    
    def add_user(self, user: User):
        self.__users.append(user)

    def get_users(self):
        return self.__users

    def get_user_by_email(self, email: str):
        for user in self.get_users():
            if user.get_email() == email:
                return user

        return None

    def get_user_by_username(self, username: str):
        for user in self.get_users():
            if user.get_username() == username:
                return user

        return None

    def get_user_by_id(self, user_id: str):
        for user in self.get_users():
            if user.get_id() == user_id:
                return user

        return None
    
    def remove_user_by_id(self, user_id: str):
        user = self.get_user_by_id(user_id)

        if user is not None:
            self.__users.remove(user)
            return True
        
        return False
