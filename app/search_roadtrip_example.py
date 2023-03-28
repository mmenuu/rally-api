# from roadtrip import Roadtrip
# from roadtripcatalog import RoadtripCatalog

# from user import User
# from user_list import UserList
# from waypoint import Waypoint

# non = User("nonza", "nonnon123", "nonza123@gmail.com")
# kla = User("nonza", "nonnon123", "nonza123@gmail.com")

# users = UserList()
# users.add_user(non)
# users.add_user(kla)

# bkk_waypoint = Waypoint("Bangkok")
# rayong_waypoint = Waypoint("Rayong")

# roadtrip_waypoints = [bkk_waypoint, rayong_waypoint]

# non_roadtrip = Roadtrip("BKK Roadtrip by NON", roadtrip_waypoints, "NON", "Capital")
# non_roadtrip2 = Roadtrip("BKK Roadtrip 2 by NON", roadtrip_waypoints, "NON", "Capital")
# kla_roadtrip = Roadtrip("RAYONG Roadtrip by KLA", roadtrip_waypoints, "KLA", "SEA")

# watprook_waypoint = Waypoint("Wat Prook")
# kla_roadtrip.add_waypoint(watprook_waypoint)

# roadtrip_catalog = RoadtripCatalog()
# roadtrip_catalog.add_roadtrip(non_roadtrip)
# roadtrip_catalog.add_roadtrip(kla_roadtrip)

# search_result = roadtrip_catalog.search("non")
# if not search_result:
#     print("404 Not found")
# else:
#     print("Search result: ")
#     for item in search_result:
#         print(item.title)