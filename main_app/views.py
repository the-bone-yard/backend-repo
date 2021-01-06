import requests
from django.shortcuts import render


def home(request):
   # get the list of todos
   response = requests.get('https://jsonplaceholder.typicode.com/todos')
   # transfor the response to json objects
   todos = response.json()
   return render(request, "main_app/home.html", {"billy": todos})

def index(request):
   return render(request, "main_app/index.html")