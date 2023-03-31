from app.internal.magazine import Magazine

class MagazineCatalog:
    def __init__(self):
        self.__magazines = [] # list of magazine object

    def get_magazines(self):
        return self.__magazines

    def get_magazine_by_id(self, magazine_id: str):
        for magazine in self.get_magazines():
            if magazine.get_id() == magazine_id:  # if there is magazine_id return that magazine
                return magazine

        return None

    def get_roadtrips_by_id(self, magazine_id: str):
        magazine = self.get_magazine_by_id(magazine_id)
        if magazine is not None:
            return magazine.get_roadtrips()
        return None

    def add_magazine(self, new_magazine: Magazine):
        self.__magazines.append(new_magazine)  # add magazine to list

    def add_roadtrip(self, magazine_id: str, roadtrip: dict):
        magazine = self.get_magazine_by_id(magazine_id)
        if magazine is not None:
            magazine.add_roadtrip(roadtrip)
            return True
        return False

    def remove_roadtrip(self, magazine_id: str, roadtrip_id: str):
        magazine = self.get_magazine_by_id(magazine_id)
        if magazine is not None:
            magazine.remove_roadtrip(roadtrip_id)
            return True
        return False

    def remove_magazine(self, magazine_id: str):
        magazine = self.get_magazine_by_id(magazine_id)
        if magazine is not None:
            return self.__magazines.remove(magazine)
        return None
