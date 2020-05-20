import geocoder
import reverse_geocoder as rg 
import pprint 
from math import sin, cos, sqrt, atan2, radians

g = geocoder.ipinfo('me')
coordinates = g.latlng
result = rg.search(coordinates)
pprint.pprint(result)
R = 6373.0

lat1 = radians(18.51957)
lon1 = radians(73.85535)

lat2 = radians(19.095207)
lon2 = radians(74.749596)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c
print("\n")
print("This is distance from Pune to Ahmednagar Maharashtra")
print("Result:", distance)


