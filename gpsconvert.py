from math import sin, cos, sqrt, atan2, radians
from os import system, name

#
## Define the clear function
#
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#
##  Approximate radius of earth in km
#
R = 6373.0

#
## Note that Python deals with radians by default, so degrees of
## measure need to be calculated. REB 09/2018
#

#
## GPS Coordinates For Vandenberg AFB Launch Complex SLC-2W
#
lat1 = radians(34.7552778)
lon1 = radians(120.6222222)

#
## GPS Coordinates For Vandenberg AFB Weather Station (Corral Rd)
#
lat2 = radians(34.76855)
lon2 = radians(120.530156)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c
distancemi = distance / 1.60934

#
## Clear the screen of junk.
#
clear()

print("Results from GPS coordinates:", distance, "km")
print("Calculated by sound, it should be:", 8.52952, "km")
print("")
print("Sound distance in miles", 5.310181818, "miles")
print("Calculated GPS coordinates in miles: ", distancemi, "miles")
