from main_app.models import Park
from rest_framework import serializers

class ParkSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = Park
        fields = '__all__'

    def create(self, validated_data):
        # is used to create the json object, need to check if this works properly also, needs to be tested
        """Create a new park and return it"""
        return Park.objects.create(**validated_data)
