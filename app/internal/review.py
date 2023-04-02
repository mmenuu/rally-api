import uuid
class Review:
    def __init__(self, review_text: str , user_id:str , landmark_id: str, rating: float):
        self.__id = str(uuid.uuid4())
        self.__review_text = review_text
        self.__reviewer = user_id
        self.__landmark_id = landmark_id
        self.__rating = rating

    def get_id(self):
        return self.__id 
    
    def get_review_text(self):
        return self.__review_text
    
    def get_reviewer(self):
        return self.__reviewer
    
    def get_rating(self):
        return self.__rating
    
    def get_landmark_id(self):
        return self.__landmark_id
    
    def set_review_text(self, text: str):
        self.__review_text = text 

    def set_reviewer(self, reviewer: str):
        self.__reviewer = reviewer
    
    def set_landmark_id(self, landmark_id: str):
        self.__landmark_id = landmark_id
    
    def set_rating(self, rating: float):
        self.__rating = rating