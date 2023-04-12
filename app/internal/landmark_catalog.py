from landmark import Landmark


class LandmarkCatalog:
    def __init__(self):
        self.__landmarks = []

    def get_landmarks(self):
        return self.__landmarks

    def get_landmark_by_id(self, landmark_id: str):
        return next((landmark for landmark in self.__landmarks if landmark.get_id() == landmark_id), None)

    def add_landmark(self, landmark: Landmark):
        self.__landmarks.append(landmark)

    def remove_landmark(self, landmark: Landmark):
        self.__landmarks.remove(landmark)
