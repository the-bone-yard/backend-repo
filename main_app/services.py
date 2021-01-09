from django.http import JsonResponse
import requests
import json
from decouple import config

def get_parks(self, coordinates=''):
    API_KEY = config('KEY')
    radius = 2000
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key=%s&keyword=dog+park&location=%s&radius=2000" % (API_KEY,coordinates)

    data = format_data(requests.get(endpoint_url).json())

    return JsonResponse(data, safe=False)

def format_data(info):
    parks = []
    for park in info['results']:
        # if 'opening_hours' in park:
        data = {
            'formatted_address': park['vicinity'],
            'geometry': park['geometry'],
            'name': park['name'],
            'opening_hours': park['opening_hours'] if 'opening_hours' in park else 'CLOSED',
            'photos': park['photos'],
            'rating': park['rating']}
        parks.append(data)
    return parks
