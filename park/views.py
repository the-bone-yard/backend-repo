from rest_framework import generics
from park.serializers import ParkSerializer
from main_app.models import Park


class CreateParkView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = ParkSerializer
