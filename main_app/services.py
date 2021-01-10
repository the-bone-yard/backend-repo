from django.http import JsonResponse
import requests
import json
from decouple import config
import code
import re

def get_parks(self, coordinates=''):
    KEY = config('KEY')
    radius = 2000
    if len(coordinates.split(',')[0]) > 1 and float(coordinates.split(',')[0]):
        endpoint_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key={KEY}&keyword=dog+park&location={coordinates}&radius=2000"
        data = format_data(requests.get(endpoint_url).json())
    elif re.match(r'^-?\d+(?:\.\d+)?$', coordinates.split(',')[0]) is None:
        info = {'info': "geocode_api"}
        data = format_directions(requests.get(endpoint_url).json())
    else:
        data = {'Error': "Input is incorrect. Please enter either coordinates as '132.5543,-204.5566' or 'city,state'"}

    return JsonResponse(data, safe=False)

def format_data(info):
    parks = []
    for park in info['results']:
        # code.interact(local=dict(globals(), **locals()))
        data = {
            'formatted_address': park['vicinity'],
            'geometry': park['geometry'],
            'name': park['name'],
            'opening_hours': park['opening_hours'] if 'opening_hours' in park else 'CLOSED',
            'photos': park['photos'],
            'rating': park['rating']}
        parks.append(data)
    return parks

def format_directions(info):
    'dude'
