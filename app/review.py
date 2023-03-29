class Review:
    def __init__(self, id: str, review_text: str , user_id:str , landmark_id: str, rating: float):
        self.__id = id
        self.__review_text = review_text
        self.__reviewer = user_id
        self.__landmark_id = landmark_id
        self.__rating = rating

    def set_review_text(self, text: str):
        self.__review_text = text 

    def set_rating(self, rating: float):
        self.__rating = rating
    
    def get_review_text(self):
        return self.__review_text
    
    def get_rating(self):
        return self.__rating

    

