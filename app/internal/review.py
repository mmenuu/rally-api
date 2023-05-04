import uuid

class Review:
    def __init__(self, review_text:str , reviewer:str, rating: float):
        self.__id = str(uuid.uuid4())
        self.__review_text = review_text
        self.__reviewer = reviewer
        self.__rating = rating

    # Getters
    def get_id(self) -> str:
        return self.__id 
    
    def get_review_text(self) -> str:
        return self.__review_text
    
    def get_reviewer(self) -> str:
        return self.__reviewer
    
    def get_rating(self) -> float:
        return self.__rating
    
    # Setters
    def set_review_text(self, text: str) -> None:
        self.__review_text = text 

    def set_reviewer(self, reviewer: str) -> None:
        self.__reviewer = reviewer
    
    def set_rating(self, rating: float) -> None:
        self.__rating = rating  

    def to_dict(self) -> dict:
        return {
            'id': self.get_id(),
            'review_text': self.get_review_text(),
            'reviewer': self.get_reviewer(),
            'rating': self.get_rating()
        }