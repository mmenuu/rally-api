from account import Account

class Admin(Account):
    def __init__(self, id, email, password, login_status):
        super().__init__(id, email, password, login_status)
        self.__role = "admin"