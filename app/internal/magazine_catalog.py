from app.internal.magazine import Magazine

class MagazineCatalog:
    def __init__(self):
        self.__magazines = []

    def get_magazines(self):
        return self.__magazines

    def get_magazine_by_id(self, magazine_id: str):
        return next((magazine for magazine in self.__magazines if magazine.get_id() == magazine_id), None)

    def add_magazine(self, new_magazine: Magazine):
        self.__magazines.append(new_magazine)

    def remove_magazine(self, magazine: Magazine):
        self.__magazines.remove(magazine)
