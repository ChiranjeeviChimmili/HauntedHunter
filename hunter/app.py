from flask import Flask, render_template, request
import requests, json
from main import*
from haunted import *
from geocode import *
from googlemap import *

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        your_city = request.form['city']
        state = request.form['state']

        n = 1
        if state == 'texas':
            n = 2
        if state == 'california':
            n = 3

        def nearby(your_city, state):
            all_cities_list = []
            nearby_cities = []
            for x in range(n, 0, -1):
                state_search = state + str(x)
                for c in find_all_cities(state_info(state_search)):
                    all_cities_list.append(c)
            for city in all_cities_list:
                x = get_distance((your_city + ',' + state), (city + ',' + state))
                if x is not None and x < 30000:
                    nearby_cities.append(city)
            return list(dict.fromkeys(nearby_cities))


        def haunted_locations(nearby_cities, state):
            hl = []
            for x in range(n, 0, -1):
                state_search = state + str(x)
                for city in nearby_cities:
                    hl.append(find_city(city, state_search))
            return hl

        final_list = []
        for location in haunted_locations(nearby(your_city, state), state):
            for place in location:
                final_list.append(get_name(place) + '\n' + get_description(place) + '\n\n')

        return render_template("result.html", city = your_city, results = final_list)
    
    return render_template("index.html")
