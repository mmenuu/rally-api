class FavoriteLandmark:
    def __init__(self, user_id, landmarks = None | list):
        self.landmarks_list = landmarks # list of landmark object
        self.user_id = user_id
    
    def add_favorite_landmark(self, landmark):
        self.landmarks_list.append(landmark)

    def remove_favorite_landmark(self, landmark):
        self.landmarks_list.remove(landmark)
    
    def get_favorite_landmark(self,user_id:str):
        return [landmark for landmark in self.landmarks_list if self.user_id == user_id]
