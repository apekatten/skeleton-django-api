from rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from rest_auth.registration.serializers import RegisterSerializer as BaseRegisterSerializer
from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'last_name')


class LoginSerializer(BaseLoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})


class RegisterSerializer(BaseRegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})
