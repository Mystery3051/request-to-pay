from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "first_name", "last_name", "last_login",
         "date_joined")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        if not instance.is_active:
            representation['active'] = False
        return representation


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("user", "user_type")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.user_type == 'C':
            representation['address'] = instance.address
        return representation
