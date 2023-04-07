from app.internal.magazine import Magazine


class MagazineCatalog:
    def __init__(self):
        self.__magazines = []

    def get_magazines(self):
        return self.__magazines

    def get_magazine_by_id(self, magazine_id: str):
        for magazine in self.get_magazines():
            if magazine.get_id() == magazine_id:
                return magazine

        return None

    def add_magazine(self, new_magazine: Magazine):
        self.__magazines.append(new_magazine)

    def remove_magazine(self, magazine_id: str):
        magazine = self.get_magazine_by_id(magazine_id)
        if magazine is not None:
            return self.__magazines.remove(magazine)
        return None

    def update_magazine_by_id(self, magazine_id: str, magazine: Magazine):
        magazine_exists = self.get_magazine_by_id(magazine_id)

        if magazine_exists is not None:
            magazine_exists.set_name(magazine.get_name())
            magazine_exists.set_description(magazine.get_description())
            return True

        return False
