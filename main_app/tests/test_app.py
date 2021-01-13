from django.test import TestCase
import requests
import code
from main_app import services
from rest_framework.test import APIRequestFactory
import json


class ApiTestCase(TestCase):

    def test_can_make_api_call(self):
        """Can make an API call and expect specific attributes"""
        data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        self.assertEqual(str(type(data)), "<class 'dict'>")
        self.assertEqual(data['userId'], 1)
        self.assertEqual(str(data.keys()), "dict_keys(['userId', 'id', 'title', 'completed'])")

    def test_can_reformat_json_object(self):
        """Can make an API call and expect specific attributes"""
        data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        self.assertEqual(type(data), dict)
        self.assertEqual(data['userId'], 1)
        self.assertEqual(str(data.keys()), "dict_keys(['userId', 'id', 'title', 'completed'])")

    def test_can_make_map_API_call_with_city_state(self):
        """Can make an API call and expect specific attributes (run local server first)"""
        data = requests.get('http://localhost:8000/api/coordinates="miami,fl"').json()
        self.assertEqual(type(data), list)

        self.assertIn('formatted_address', data[0])
        self.assertIn('geometry', data[0])
        self.assertIn('name', data[0])
        self.assertIn('opening_hours', data[0])
        self.assertIn('photos', data[0])
        self.assertIn('rating', data[0])
        # code.interact(local=dict(globals(), **locals()))

    def test_can_make_map_API_call_with_coordinates(self):
        """Can make an API call and expect specific attributes (run local server first)"""
        data = requests.get('http://localhost:8000/api/coordinates="39.7392, -104.9903"').json()
        self.assertEqual(type(data), list)

        self.assertIn('formatted_address', data[0])
        self.assertIn('geometry', data[0])
        self.assertIn('name', data[0])
        self.assertIn('opening_hours', data[0])
        self.assertIn('photos', data[0])
        self.assertIn('rating', data[0])

    def test_can_make_map_API_call_and_save_a_park(self):
        """Can make an API call and expect specific attributes (run local server first)"""
        params = {
        "name": "Fake Park",
        "formatted_address": "1234 Fake Street",
        "opening_hours": "never",
        "photo": "too good for photos",
        "rating": "100 mofo"
        }
        data = requests.post('http://localhost:8000/api/park/create/', params)
        self.assertEqual(type(data), requests.models.Response)

        result = requests.get('http://localhost:8000/api/park/all')
