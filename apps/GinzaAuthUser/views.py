from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create local imports
from . import serializers
from . import models
from django.utils import timezone


# Create your views here.
class CustomUserRegister(CreateAPIView):
    serializer_class = serializers.CustomUserSerializer
    # serializer_class = serializers.UserSerializer
    queryset = models.CustomUser.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeleteUser(APIView):

    serializer_class = serializers.CustomUserSerializerDelete
    queryset = models.CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request)
        print(self.request.user)
        user = models.CustomUser.objects.get(username=self.request.user)
        date_now = f"{timezone.now().strftime('%Y-%m-%d %H:%M')}"
        user.username = f"{date_now}_deleted_{user.username}"
        user.email = f"{date_now}_deleted_{user.email}"
        user.phone = f"{date_now}_deleted_{user.phone}"
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.user_permissions_set = ['DjangoModelPermissionsOrAnonReadOnly']
        user.save()
        comment = "User deleted"

        return Response(status=status.HTTP_200_OK)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        # ...
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class CustomAuthToken(TokenObtainPairView):
    queryset = models.CustomUser.objects.all()
    serializers_class = serializers.CustomUserSerializerLogin


