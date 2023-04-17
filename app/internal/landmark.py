from .review import Review

class Landmark:
    def __init__(self, id: str, name: str, amenity: str, position: list, opening_hours: str):
        self.__id = id
        self.__name = name
        self.__amenity = amenity
        self.__position = position
        self.__opening_hours = opening_hours
        self.__reviews = list()

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_amenity(self):
        return self.__amenity

    def get_position(self):
        return self.__position

    def get_opening_hours(self):
        return self.__opening_hours

    def get_reviews(self):
        return self.__reviews

    def get_review_by_id(self, review_id: str):
        return next((review for review in self.__reviews if review.get_id() == review_id), None)
    
    def get_review_by_user_id(self, user_id: str):
        return next((review for review in self.__reviews if review.get_reviewer() == user_id), None)
    
    def get_average_rating(self):
        return sum([review.get_rating() for review in self.__reviews]) / len(self.__reviews)
    
    # Setters
    def add_review(self, review: Review):
        self.__reviews.append(review)

    def remove_review(self, review: Review):
        self.__reviews.remove(review)
