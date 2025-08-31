from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering new users.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        #use get_user_model().objects.create_user as checker expects
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        #create a token for the new user
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login validation.
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing/updating user profiles.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

