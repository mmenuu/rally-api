from account import Account

class Admin(Account):
    def __init__(self, id, email, password, login_status):
        super().__init__(id, email, password, login_status)
        self.__role = "admin"
    
    def edit_magazine(self, Magazine, section):
        pass

    def create_magaine(self, name, Roadtrip):
        pass
    
    def remove_user(self, user):
        pass