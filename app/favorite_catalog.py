from favorite_landmark import FavoriteLandmark

class FavoriteCatalog:
    def __init__(self):
        self.favorite_landmarks = []
    
    def add_favorite_landmark(self, favorite_landmark):
        self.landmarks.append(favorite_landmark)

    def get_favorite_landmark_by_user_id(self, user_id: str):
        for favorite_landmark in self.favorite_landmarks:
            if favorite_landmark.user_id == user_id:
                return favorite_landmark
            
        return None

    def add_landmark_by_user_id(self, new_landmark, user_id: str):
        favorite_landmark = self.get_favorite_landmark_by_user_id(user_id)
        
        if favorite_landmark is not None:
            favorite_landmark.add_landmark(new_landmark)
        else:
            new_favorite_landmark = FavoriteLandmark(user_id)
            new_favorite_landmark.add_landmark(new_landmark)
            self.favorite_landmarks.append(new_favorite_landmark)            
        

    def remove_landmark_by_user_id(self, user_id: str, landmark_id:str):
        favorite_landmark = self.get_favorite_landmark_by_user_id(user_id)
        
        if favorite_landmark is not None:
            favorite_landmark.remove_landmark_by_landmark_id(landmark_id)