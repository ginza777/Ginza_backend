from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserSerializerLogin(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
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
        fields = ['username', 'email', 'phone', 'password', 'is_active']

    def create(self, validated_data):
        # Retrieve the password from validated_data
        password = validated_data.pop('password')

        # Hash and encrypt the password using Django's make_password function
        hashed_password = make_password(password)

        # Create the user using the remaining validated_data and the hashed password
        user = CustomUser.objects.create(password=hashed_password, **validated_data)
        return user


class CustomUserSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
