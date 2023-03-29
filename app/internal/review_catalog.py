class ReviewCatalog:
    def __init__(self, reviews):
        self.__reviews = [] 

    def get_reviews(self):
        return self.__reviews
    
    def get_review(self, user_id: str, landmark_id: str):
        for review in self.get_reviews():
            if review.get_reviewer() == user_id and review.get_landmark_id() == landmark_id:
                return review

        return None
    
    def get_reviews_by_landmark(self, landmark_id: str):
        return [review for review in self.get_reviews() if review.get_landmark_id() == landmark_id]

    def get_reviews_by_user(self, user_id: str ):
        return [review for review in self.get_reviews() if review.get_reviewer() == user_id]
    
    def add_review(self, review):
        self.__reviews.append(review)

    def remove_review(self, user_id: str, landmark_id: str):
        review = self.get_review(user_id, landmark_id)

        if review is not None:
            return self.__reviews.remove(review)
        
        return None