from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","dob"]


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    class Meta:
        model = User
        fields = ("email", "password")