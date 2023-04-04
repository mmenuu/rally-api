class FavoriteLandmark:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__landmarks = [] # list of landmark id
    
    def get_user_id(self):
        return self.__user_id
    
    def add_landmark(self, landmark):
        self.__landmarks.append(landmark)
        
    def get_landmarks(self):
        return self.__landmarks

    def get_landmark_by_id(self, landmark_id: str):
        for landmark in self.get_landmarks():
            if landmark.id == landmark_id:
                return landmark

        return None
        
    def remove_landmark_by_id(self, landmark_id: str):
        landmark = self.get_landmark_by_id(landmark_id)
        
        if landmark is not None:
            self.__landmarks.remove(landmark)
            return True
        
        return False