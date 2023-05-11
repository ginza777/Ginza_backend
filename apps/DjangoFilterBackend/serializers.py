from rest_framework import serializers
from apps.GinzaAuthUser.models import CustomUser
from .models import Product



#product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'







class CustomFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserbyIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UsernameSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
