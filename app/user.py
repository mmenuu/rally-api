from app.account import Account
import uuid

class User(Account):
    def __init__(self, email, username, password):
        super().__init__(email, username, password)