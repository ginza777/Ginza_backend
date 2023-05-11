from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import filters
from .serializers import *
from .filter import *


# Create your views here.


class CustomFilter(ListAPIView):
    serializer_class = CustomFilterSerializer
    queryset = CustomUser.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CustomFilterset


class UsernameListSearch(ListAPIView):
    serializer_class = UsernameSearchSerializer
    queryset = CustomUser.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'privaligies', 'is_active', 'is_staff', 'is_superuser']


class UsernameSearch(RetrieveAPIView):
    serializer_class = UsernameSearchSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        return CustomUser.objects.all()


class UserbyID(RetrieveAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [AllowAny]
    serializer_class = UserbyIDSerializer

    def get_queryset(self):
        return CustomUser.objects.all()


class UserListView(ListAPIView):
    serializer_class = UsersSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
