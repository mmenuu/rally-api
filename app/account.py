import uuid

class Account:
    def __init__(self, email, username, password):
        self.id = str(uuid.uuid4())
        self.email = email
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.__password = password