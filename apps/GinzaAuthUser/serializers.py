from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializerLogin(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [ 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=9, write_only=True)
    phone = serializers.CharField(max_length=20, min_length=13, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validated_password(self, value):
        validate_password(value)
        return value




class CustomUserSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
