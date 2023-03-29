from app.internal.user import User

class UserCatalog:
    '''
    This class is responsible for managing the users in the catalog.

    Attributes:
        __users (list): A list of users in the catalog.
    
    Methods:
        - add_user(user: User): Add a user to the catalog.
        - get_users(): Get all users in the catalog.
        - get_user_by_email(email: str): Get a user by email.
        - get_user_by_username(username: str): Get a user by username.
        - get_user_by_id(user_id: str): Get a user by id.
        - remove_user_by_id(user_id: str): Remove a user by id.
    '''
    def __init__(self):
        self.__users = []
    
    def add_user(self, user: User):
        '''
        Add a user to the catalog.
        '''
        self.__users.append(user)

    def get_users(self):
        '''
        Get all users in the catalog.
        '''
        return self.__users

    def get_user_by_email(self, email: str):
        '''
        Get a user by email.
        '''
        for user in self.get_users():
            if user.get_email() == email:
                return user

        return None

    def get_user_by_username(self, username: str):
        '''
        Get a user by username.
        '''
        for user in self.get_users():
            if user.get_username() == username:
                return user

        return None

    def get_user_by_id(self, user_id: str):
        '''
        Get a user by id.
        '''
        for user in self.get_users():
            if user.get_id() == user_id:
                return user

        return None
    
    def remove_user_by_id(self, user_id: str):
        '''
        Remove a user by id.
        '''
        user = self.get_user_by_id(user_id)

        if user is not None:
            self.__users.remove(user)
            return True
        
        return False
