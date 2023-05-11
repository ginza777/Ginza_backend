from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework.throttling import UserRateThrottle
from rest_framework import filters, status
from .serializers import *
from .filter import *
from apps.GinzaAuthUser.models import CustomUser as User
from .models import Product
# Create your views here.
from django.db.models import Q


class ProductFilterView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        price = request.query_params.get('price')
        print("get: ", price)
        product = Product.objects.filter(
            Q(price__exact=price) | Q(price_min__gte=price) | Q(price_max__gte=price) | Q(price__gte=price)).order_by(
            'id')

        serializer = self.serializer_class(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        price = request.query_params.get('price')
        print("post: ", price)
        product = Product.objects.filter(
            Q(price__exact=price) | Q(price_min__gte=price) | Q(price_max__gte=price) | Q(price__gte=price)).order_by(
            'id')
        serializer = self.serializer_class(product, many=True)

        return Response(serializer.data)


# product
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilterset


class CustomFilter(APIView):
    def get(self, request, user_id=None):
        print(user_id)
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                data = {'username': user.username, 'email': user.email}
                return Response(data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            data = [{'username': user.username, 'email': user.email} for user in users]
            return Response(data)

    def post(self, request):
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)
            comment = f"user topildi {user.username} {user.privaligies}"
            data = {'username': user.username,
                    'privaligies': user.privaligies,
                    'comment': comment
                    }

            return Response(data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            comment = {'error': 'user not found'}
            return Response(comment, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)
            user.delete()
            comment = {'comment': 'user deleted'}
            return Response(comment, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            comment = {'error': 'user not found'}
            return Response(comment, status=status.HTTP_404_NOT_FOUND)


class UserFilter(ListAPIView):
    serializer_class = UserFilterSerializer
    queryset = CustomUser.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = UserFilterset


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
