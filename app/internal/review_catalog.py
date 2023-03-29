class ReviewCatalog:
    def __init__(self, reviews):
        self.__reviews = [] 

    def get_reviews_by_landmark(self, landmark_id: str):
        return [review for review in self.__reviews if review.__landmark_id == landmark_id]

    def get_reviews_by_userid(self, user_id: str ):
        return [review for review in self.__reviews if review.__reviewer == user_id]

    def get_review_by_userid(self, user_id: str, landmark_id: str):
        for review in self.get_reviews_by_userid(user_id):
            if review.__landmark_id == landmark_id:
                return review    
        return None 

    def add_review(self, review):
        self.__reviews.append(review)

    def remove_review(self, user_id: str, landmark_id: str):
        review = self.get_review_by_userid(user_id, landmark_id)
        if review is not None:
            return self.__reviews.remove(review)
        return None

      
   