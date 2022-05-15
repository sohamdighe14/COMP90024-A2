# COMP90024 - Assignment 2 - team 60
#
#  Junhong Liu         - Student ID: 1084997 - Melbourne
#  Justin Beaconsfield - Student ID: 761885  - Melbourne
#  Callum Dowling      - Student ID: 1009257 - Palmwoods
#  Soham Swapnil Dighe - Student ID: 1219439 - Melbourne
#  Samy Allouache      - Student ID: 1210426 - Melbourne

import folium

MELB_LAT = 	"-37.840935"
MELB_LONG = "144.946457"

location = MELB_LAT, MELB_LONG
m = folium.Map(location=location,zoom_start=6)
m.save("./map.html")