from django.http import JsonResponse
import requests

def get_parks(self, pk):
    info = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    data = {
    'This is the ridiculous thing you sent to the BE. Dont waste our time': pk
    }
    return JsonResponse(data)
