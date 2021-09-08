import googlemaps
from geocode import *

gm = googlemaps.Client(key = getKey(0))

def get_distance(location1, location2):
    origin = str(getGeocode(location1)[0]) + "," + str(getGeocode(location1)[1])
    destination = str(getGeocode(location2)[0]) + "," + str(getGeocode(location2)[1])
    try:
        dist = gm.distance_matrix(origin, destination)['rows'][0]['elements'][0]['distance']['value']
        return dist
    except KeyError:
        return
