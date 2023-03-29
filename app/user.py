from account import Account

class User(Account):
    def __init__(self, email, username, password):
        super().__init__(id, email, username, password)
        self.__role = "user"