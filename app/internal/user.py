from .account import Account
from .landmark import Landmark


class User(Account):
    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.__favorite_landmarks = []

    def add_favorite_landmark(self, landmark: Landmark):
        self.__favorite_landmarks.append(landmark)

    def get_favorite_landmarks(self):
        return self.__favorite_landmarks

    def get_favorite_landmark_by_id(self, landmark_id: str):
        for landmark in self.get_favorite_landmarks():
            if landmark.get_id() == landmark_id:
                return landmark
        return None

    def remove_favorite_landmark_by_id(self, landmark_id: str):
        self.__favorite_landmarks.remove(landmark_id)
        return self.__favorite_landmarks
