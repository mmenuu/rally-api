from typing import List
from .magazine import Magazine

class MagazineCatalog:
    def __init__(self):
        self.__magazines: List[Magazine] = []

    # Getters
    def get_magazines(self) -> List[Magazine]:
        return self.__magazines

    def get_magazine_by_id(self, magazine_id: str) -> Magazine | None:
        return next((magazine for magazine in self.get_magazines() if magazine.get_id() == magazine_id), None)

    # Setters
    def add_magazine(self, new_magazine: Magazine) -> None:
        self.__magazines.append(new_magazine)

    def remove_magazine(self, magazine: Magazine) -> None:
        self.__magazines.remove(magazine)
