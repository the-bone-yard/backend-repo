from django.test import TestCase
from main_app.models import Park

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_PARK_URL = reverse('park:create')

def create_park(**params):
    return Park.create_park(**params)


class PublicParkAPITests(TestCase):
    """Test the Park API (public)"""
#old tests
    # def setup(self):
    #     self.client = APIClient()

    # def test_create_valid_user_success(self):
    #     """Test creating user with valid info is successful"""
    #     payload = {
    #         'email': 'test@test.com'
    #     }

    #     res = self.client.post(CREATE_USER_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     user = get_user_model().objects.get(**res.data)

    
