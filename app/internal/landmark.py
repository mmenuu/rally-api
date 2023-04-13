class Landmark:
    def __init__(self, id: str, name: str, amenity: str, position: list, opening_hours: str):
        self.__id = id
        self.__name = name
        self.__amenity = amenity
        self.__position = position
        self.__opening_hours = opening_hours
        self.__reviews = []

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

    def get_reviews_by_user_id(self, user_id: str):
        for review in __reviews:
            if review.get_reviewer() == user_id:
                return review
        return None
    
    def add_review(self, review: Review):
        self.__reviews.append(review)
    
    def remove_review(self, review: Review):
        self.__reviews.remove(review)
