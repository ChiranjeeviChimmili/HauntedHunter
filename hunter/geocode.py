import requests
import json

def getKey(number):
    api_file = open("C:\\Users\\Akash\\Documents\\Python Scripts\\api-key.txt", "r")
    keys = []
    for line in api_file.readlines():
        keys.append(line)
    api_file.close()
    return keys[number]

def getGeocode(location):
    parameters = {
        "key" : getKey(1),
        "location" : location
    }
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)
    data = json.loads(response.text)['results']
    lat = data[0]['locations'][0]['latLng']['lat']
    lng = data[0]['locations'][0]['latLng']['lng']
    return [lat, lng]
