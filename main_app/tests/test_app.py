from django.test import TestCase
import requests


class ApiTestCase(TestCase):

    def test_can_make_api_call(self):
        """Can make an API call and expect specific attributes"""
        data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        # import code; code.interact(local=dict(globals(), **locals()))
        self.assertEqual(str(type(data)), "<class 'dict'>")
        self.assertEqual(data['userId'], 1)
        self.assertEqual(str(data.keys()), "dict_keys(['userId', 'id', 'title', 'completed'])")

    def test_can_reformat_json_object(self):
        """Can make an API call and expect specific attributes"""
        data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        # import code; code.interact(local=dict(globals(), **locals()))
        self.assertEqual(type(data), dict)
        self.assertEqual(data['userId'], 1)
        self.assertEqual(str(data.keys()), "dict_keys(['userId', 'id', 'title', 'completed'])")

    def test_can_return_error(self):
        """Can return an error when entering incorrect coordinate format"""
        data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        self.assertEqual(type(data), dict)
        self.assertEqual(data['userId'], 1)
            self.assertEqual(str(data.keys()), 'Error': "Input is incorrect. Please enter either coordinates as '132.5543,-204.5566' or 'city,state'")
