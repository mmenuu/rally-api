class FavoriteLandmark:
    def __init__(self, user_id):
        self.user_id = user_id
        self.landmarks = [] # list of landmark object
        
    def add_landmark(self, landmark):
        self.landmarks_list.append(landmark)
        
    def get_landmarks(self):
        return self.landmarks

    def get_landmark_by_landmark_id(self, landmark_id: str):
        for landmark in self.landmarks:
            if landmark.id == landmark_id:
                return landmark

        return None
        
    def remove_landmark_by_landmark_id(self, landmark_id: str):
        landmark = self.get_landmark_by_landmark_id(landmark_id)
        
        if landmark is not None:
            self.landmarks.remove(landmark)
        
        return False