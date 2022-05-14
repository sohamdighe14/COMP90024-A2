import folium

MELB_LAT = 	"-37.840935"
MELB_LONG = "144.946457"

location = MELB_LAT, MELB_LONG
m = folium.Map(location=location,zoom_start=6)
m.save("./map.html")