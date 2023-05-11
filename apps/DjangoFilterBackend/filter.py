import django_filters
from apps.GinzaAuthUser.models import CustomUser
from .models import Product
from django.db.models import Q

class ProductFilterset(django_filters.FilterSet):
    price = django_filters.NumberFilter(lookup_expr='exact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields =[ 'price', 'price_min', 'price_max']



class CustomFilterset(django_filters.FilterSet):
    pass


# custom filterset class
class UserFilterset(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            'username': ['exact', 'icontains'],
            'privaligies': ['exact', 'icontains'],
            'is_active': ['exact', 'icontains'],
            'is_staff': ['exact', 'icontains'],
            'is_superuser': ['exact', 'icontains'],
        }
