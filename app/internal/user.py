from .account import Account
from .landmark import Landmark


class User(Account):
    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.__favorite_landmarks = []

    # Getters
    def get_favorite_landmarks(self):
        return self.__favorite_landmarks

    def get_favorite_landmark_by_id(self, landmark_id: str):
        return next((landmark for landmark in self.__favorite_landmarks if landmark == landmark_id), None)

    # Setters
    def add_favorite_landmark(self, landmark_id: str):
        self.__favorite_landmarks.append(landmark_id)

    def remove_favorite_landmark(self, landmark_id: str):
        self.__favorite_landmarks.remove(landmark_id)
