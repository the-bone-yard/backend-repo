from django.http import JsonResponse
import requests
import code

#my progress
def get_parks(self, input):
    code.interact(local=dict(globals(), **locals()))
    coordinates = location
    endpoint_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAb6K8lFSR2jjUv5GwqKvTMgdumdWPh-FE&input=%s&location=%s&radius=49999' % (input, coordinates)

    # endpoint_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?input=%s&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAb6K8lFSR2jjUv5GwqKvTMgdumdWPh-FE' % input
    # variables = {
    #     'input' : input,
    #     'inputtye' : 'textquery',
    #     'fields' : 'photos,formatted_address,name,rating,geometry',
    #     'key': 'AIzaSyAb6K8lFSR2jjUv5GwqKvTMgdumdWPh-FE'
    # }
    info = requests.get(endpoint_url).json()
    data = {
    'test': info["candidates"]
    }
    return JsonResponse(data)

# def get_parks(self, pk):
#     info = requests.get(
#         'https://jsonplaceholder.typicode.com/todos/1').json()
#     data = {
#     'name': info['title']
#     }
#     return JsonResponse(data)
# Copy for reference, in case i fuck the top one up
