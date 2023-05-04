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
    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_amenity(self) -> str:
        return self.__amenity

    def get_position(self) -> list:
        return self.__position

    def get_opening_hours(self) -> str:
        return self.__opening_hours

    def get_reviews(self) -> list[Review]:
        return self.__reviews

    def get_review_by_id(self, review_id: str) -> Review | None:
        return next((review for review in self.__reviews if review.get_id() == review_id), None)

    def get_review_by_username(self, username: str) -> Review | None:
        return next((review for review in self.__reviews if review.get_reviewer() == username), None)

    def get_average_rating(self) -> float:
        return sum([review.get_rating() for review in self.__reviews]) / len(self.__reviews) if len(self.__reviews) > 0 else 0

    # Setters
    def add_review(self, review: Review) -> None:
        self.__reviews.append(review)

    def remove_review(self, review: Review) -> None:
        self.__reviews.remove(review)

    def to_dict(self) -> dict:
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'amenity': self.get_amenity(),
            'position': self.get_position(),
            'opening_hours': self.get_opening_hours(),
            'reviews': [review.to_dict() for review in self.get_reviews()],
            'average_rating': self.get_average_rating()
        }