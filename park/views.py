from rest_framework import generics
from park.serializers import ParkSerializer


class CreateParkView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = ParkSerializer

