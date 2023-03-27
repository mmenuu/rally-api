from magazine import Magazine

class MagazineCatalog:
    def __init__(self):
        self._magazine_list = []

    def get_magazine(self, magazine_id: str):
        for magazine in self._magazine_list:
            if magazine.id is not None: # if there is magazine_id return that magazine
                return magazine
        return None
        
    def add_magazine(self, magazine):
        self._magazine_list.append(magazine) # add magazine to list
    
    def remove_magazine(self, id):
        magazine = get_magazine(id)
        if magazine is not None:
            self._magazine_list.remove(magazine) # if there is that magazine remove magazine from magazine list
        
    
                

