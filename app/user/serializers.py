from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # Serliazer is where json data does before db
    def create(self, validated_data):
        """Override create function"""
        return get_user_model().objects.create_user(**validated_data)
