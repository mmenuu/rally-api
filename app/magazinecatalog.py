from magazine import Magazine

class MagazineCatalog:
    def __init__(self):
        self._magazine_list = []

    def get_magazine(self, magazine_id: str):
        for magazine in self._magazine_list:
            if magazine.id == magazine_id: # if there is magazine_id return that magazine
                return magazine
        return None # ERROR : magazine not found
        
    def add_magazine(self, magazine):
        self._magazine_list.append(magazine) # add magazine to list
    
    def remove_magazine(self, id):
        magazine = get_magazine(id)
        if magazine is not None:
           return self._magazine_list.remove(magazine) # if there is that magazine remove magazine from magazine list
        return None
        
    
                

