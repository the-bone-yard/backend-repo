from django.http import JsonResponse
import requests
import json
from decouple import config
import code
import re

def get_parks(self, coordinates=''):
    KEY = config('KEY')
    radius = 48000
    if re.match(r'^-?\d+(?:\.\d+)?$', coordinates.split(',')[0]) is None:
        coords = get_coordinates(coordinates)
        endpoint_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key={KEY}&keyword=dog+park&location={coords['lat']},{coords['lng']}&radius={radius}"
        data = format_data(requests.get(endpoint_url).json())
    elif len(coordinates.split(',')[0]) > 1 and float(coordinates.split(',')[0]):
        endpoint_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key={KEY}&keyword=dog+park&location={coordinates}&radius={radius}"
        data = format_data(requests.get(endpoint_url).json())
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
            'photos': park['photos'] if 'photos' in park else 'NO PHOTOS',
            'rating': park['rating']}
        parks.append(data)
    return parks

def get_directions(self, current='', to=''):
    KEY = config('MAP_Q')
    endpoint_url = f"https://www.mapquestapi.com/directions/v2/route?key={KEY}&from={current}&to={to}&routeType=fastest"
    data = requests.get(endpoint_url).json()

def get_coordinates(info):
    endpoint = f"https://www.mapquestapi.com/geocoding/v1/address?key={config('MAP_Q')}&location={info}"
    response = requests.get(endpoint).json()
    return format_coordiantes(response)
    # code.interact(local=dict(globals(), **locals()))

def format_coordiantes(info):
    return info['results'][0]['locations'][0]['latLng']



def format_directions(info):
    'dude'
