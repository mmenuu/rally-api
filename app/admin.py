from user import User
from magazine import Magazine
from magazine_catalog import MagazineCatalog
class Admin(User):
    def __init__(self, email, password, login_status):
        super().__init__(id, email, password, login_status)
        self.__role = "admin"
    
    def edit_magazine_roadtrip(self, id, roadtrip):
        edit_magazine = MagazineCatalog.get_magazine(id)
        edit_magazine.edit_roadtrip(roadtrip)
    
    def edit_magazine_description(self, id, text):
        edit_magazine = MagazineCatalog.get_magazine(id)
        edit_magazine.edit_description(text)

    def edit_magazine_name(self, id, name):
        edit_magazine = MagazineCatalog.get_magazine(id)
        edit_magazine.edit_magazine_name(name)

    def create_magazine(self, name, Roadtrip, description):
        new_magazine = Magazine(id, roadtrip, name, description)
        MagazineCatalog.add_magazine(new_magazine)
    
    def delete_magazine(self, id):
        MagazineCatalog.remove_magazine(id)
    
    def remove_user(self, user):
        pass