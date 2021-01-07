from django.test import TestCase
import requests


class AnimalTestCase(TestCase):

    def test_can_make_api_call(self):
        """Can make an API call and expect specific attributes"""
        data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
        # import code; code.interact(local=dict(globals(), **locals()))
        self.assertEqual(str(type(data)), "<class 'dict'>")
        self.assertEqual(data['userId'], 1)
        self.assertEqual(str(data.keys()), "dict_keys(['userId', 'id', 'title', 'completed'])")