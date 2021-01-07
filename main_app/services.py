from django.http import JsonResponse
import requests

def get_parks(self, pk):
    info = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    data = {
    'name': info['title']
    }
    return JsonResponse(data)
