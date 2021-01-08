from django.http import JsonResponse
import requests

def get_parks(self, coordinates='', query=''):

    radius = 2000
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAb6K8lFSR2jjUv5GwqKvTMgdumdWPh-FE&keyword=%s&location=%s&radius=2000" % (query,coordinates)

    info = requests.get(endpoint_url).json()

    data = {
    'test': info["results"]
    }
    # import code; code.interact(local=dict(globals(), **locals()))
    return JsonResponse(data)
