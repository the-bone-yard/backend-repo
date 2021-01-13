from django.test import TestCase
from django.contrib.auth import get_user_model
from main_app.models import Park

class ModelTests(TestCase):
    def test_create_park_with_name_and_address(self):
        """Test creating a new park with name and address"""
        name = 'park'
        formatted_address = '123 main st'
        opening_hours = '9AM - 10PM'
        photo = 'www.pic.com'
        rating = '3'
        email = '123@emails.com'
        lat = 23.4432
        lng = -104.19801
        park = Park.objects.create(
            name=name,
            formatted_address=formatted_address,
            opening_hours=opening_hours,
            photo=photo,
            rating=rating,
            email=email,
            lat=lat,
            lng=lng
        )

        self.assertEqual(park.name, name)
        self.assertEqual(park.formatted_address, formatted_address)
        self.assertEqual(park.opening_hours, opening_hours)
        self.assertEqual(park.photo, photo)
        self.assertEqual(park.rating, rating)
        self.assertEqual(park.email, email)

        self.assertEqual(park.lat, lat)
        self.assertEqual(type(park.lat), float)
        self.assertEqual(park.lng, lng)
        self.assertEqual(type(park.lng), float)
