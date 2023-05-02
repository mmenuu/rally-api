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
        return next((landmark for landmark in self.__favorite_landmarks if landmark.get_id() == landmark_id), None)

    # Setters
    def add_favorite_landmark(self, new_favorite_landmark: Landmark):
        self.__favorite_landmarks.append(new_favorite_landmark)

    def remove_favorite_landmark(self, landmark: Landmark):
        self.__favorite_landmarks.remove(landmark)


    def to_dict(self):
        return {
            'id': self.get_id(),
            'email': self.get_email(),
            'username': self.get_username(),
            'favorite_landmarks': [landmark.to_dict() for landmark in self.get_favorite_landmarks()]
        }