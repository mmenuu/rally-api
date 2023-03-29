class Review:
    def __init__(self, id: str, review_text: str , user_id:str , landmark_id: str, rating: float):
        self.__id = id
        self.__review_text = review_text
        self.__reviewer = user_id
        self.__landmark_id = landmark_id
        self.__rating = rating

    def edit_review_text(self, text):
        self.__review_text = text 

    def edit_rating(self, rating):
        self.__rating = rating

    

