'''
Antipode Locator - OOPs - Coded in Python
by Shahroz 'Sz' Khan
'''
#Using Folium Module to Create a Map and Pin out the antipode Co-ords
from folium import Map

#basic code
latitude=float("33.27")
longitude=float("75.34")

#antipode co-ord logic
antipode_latitude=latitude.__mul__(float("-1"))
if longitude.__le__(float("0")):
    antipode_longitude=longitude.__add__(float("180"))
else:
    antipode_longitude=longitude.__sub__(float("180"))

#making the map
antipode_location=list((antipode_latitude, antipode_longitude))
antipode_map=Map(antipode_location)
antipode_map.save(str("antipode.html"))
print("Antipode Located! \nCheck Created Html File.")