from .landmark import Landmark
import re

class LandmarkCatalog:
    def __init__(self):
        self.__landmarks = []

    # Getters
    def get_landmarks(self):
        return self.__landmarks

    def get_landmark_by_id(self, landmark_id: str):
        return next((landmark for landmark in self.__landmarks if landmark.get_id() == landmark_id), None)

    def get_landmark_by_review_id(self, review_id: str):
        return next((landmark for landmark in self.__landmarks if landmark.get_review_by_id(review_id) is not None), None)

    # Setters
    def add_landmark(self, landmark: Landmark):
        self.__landmarks.append(landmark)

    def remove_landmark(self, landmark: Landmark):
        self.__landmarks.remove(landmark)

    def get_landmarks_by_keyword(self, keyword: str):
        regex = re.compile(keyword, re.IGNORECASE)
        search_result = set(item for item in self.__landmarks if any(regex.search(attr) for attr in [item.get_name(), item.get_position()]))

        return search_result