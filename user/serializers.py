from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = '__all__'
        # fields = "_all_"

    def create(self, validated_data):
        """Create a new user and return it"""
        return get_user_model().objects.create_user(**validated_data)
