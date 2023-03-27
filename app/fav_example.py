from favorite_landmark import FavoriteLandmark
from favorite_catalog import FavoriteCatalog
from landmark import Landmark

lm1 = Landmark('place1','nice','1','11','111','1111','11111')
lm2 = Landmark('place2','nice','2','22','222','2222','22222')
lm3 = Landmark('place3','nice','3','33','333','3333','33333')

lms = ['eiei1','eiei2']
menu_fav = FavoriteLandmark('menu',lms)
print(menu_fav.landmarks_list)

menu_fav.add_favorite_landmark('eiei3')
print(menu_fav.landmarks_list)

menu_fav.remove_favorite_landmark('eiei3')
print(menu_fav.landmarks_list)


print(menu_fav.get_favorite_landmark('menu'))