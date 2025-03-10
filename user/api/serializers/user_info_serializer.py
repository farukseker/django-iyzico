from user.models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserProfile = UserProfile
        fields: str = '__all__'
