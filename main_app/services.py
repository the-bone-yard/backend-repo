from django.http import JsonResponse
import requests

def get_parks(self, input):
    endpoint_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    params = {
        'input' = input,
        'inputtye' = 'textquery',
        'fields' = 'photos,formatted_address,name,rating,geometry',
        'key' = self.apiKey
    }
    info = requests.get(
        'https://maps.googleapis.com/maps/api/place/findplacefromtext/json').json()
    data = {
    'This is the ridiculous thing you sent to the BE. Dont waste our time': pk
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
