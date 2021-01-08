from django.http import JsonResponse
import requests
import code
from decouple import config
import re


#my progress
def get_parks(self, location):
    API_KEY = config('KEY')
    endpoint_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key=%s&input=dog park&location=%s&radius=2000' % (API_KEY, location)

    info = requests.get(endpoint_url).json()
    # code.interact(local=dict(globals(), **locals()))

    data = {
    'test': info["results"]
    }
    # import code; code.interact(local=dict(globals(), **locals()))
    return JsonResponse(data)
