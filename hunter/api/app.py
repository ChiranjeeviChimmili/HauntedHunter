from haunted import *
from geocode import *
from googlemap import *
from testing import *
from flask import Flask, send_from_directory,  render_template, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

class HauntedList(Resource):

    def get(self): 
        return {'': ""}, 200
    def post(self):
        json_data = request.get_json(force=True)
        your_city = json_data['city']
        state = json_data['state']

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
        return {
            'hauntedList' : final_list
        }, 200

api.add_resource(HauntedList, '/')

app.run(debug=True)


