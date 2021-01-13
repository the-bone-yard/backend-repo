from django.http import JsonResponse
import requests
import json
from decouple import config
import code
import re
from main_app.serializer import Serializer
from main_app.models import Park
from django.http import HttpResponse

class Services:

    @staticmethod
    def get_parks(self, coordinates=''):
        KEY = config('KEY')
        radius = 48000
        if re.match(r'^-?\d+(?:\.\d+)?$', coordinates.split(',')[0]) is None:
            coords = Services.get_coordinates(coordinates)
            endpoint_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key={KEY}&keyword=dog+park&location={coords['lat']},{coords['lng']}&radius={radius}"
            data = Serializer.format_data(requests.get(endpoint_url).json())
        elif len(coordinates.split(',')[0]) > 1 and float(coordinates.split(',')[0]):
            endpoint_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key={KEY}&keyword=dog+park&location={coordinates}&radius={radius}"
            data = Serializer.format_data(requests.get(endpoint_url).json())
        else:
            data = {'Error': "Input is incorrect. Please enter either coordinates as '132.5543,-204.5566' or 'city,state'"}

        return JsonResponse(data, safe=False)

    @staticmethod
    def get_directions(self, current='', to=''):
        KEY = config('MAP_Q')
        endpoint_url = f"https://www.mapquestapi.com/directions/v2/route?key={KEY}&from={current}&to={to}&routeType=fastest"
        data = requests.get(endpoint_url).json()

        info = {"narratives": Serializer.format_directions(data)}
        return JsonResponse(info, safe=False)

    @staticmethod
    def get_coordinates(info):
        endpoint = f"https://www.mapquestapi.com/geocoding/v1/address?key={config('MAP_Q')}&location={info}"
        response = requests.get(endpoint).json()
        return Serializer.format_coordiantes(response)

    @staticmethod
    def get_all_parks(self):
        info = Park.objects.all()
        parks = []
        for park in info:
            data = {
                'name': park.name,
                'address': park.formatted_address,
                'opening_hours': park.opening_hours,
                'photos': park.photo,
                'rating': park.rating,
                'email': park.email,
                'lat': park.lat,
                'lng': park.lng
                }
            parks.append(data)
        return JsonResponse(parks, safe=False)
