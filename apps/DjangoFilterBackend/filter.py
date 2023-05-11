import django_filters
from apps.GinzaAuthUser.models import CustomUser


# custom filterset class
class CustomFilterset(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            'username': ['exact', 'icontains'],
            'privaligies': ['exact', 'icontains'],
            'is_active': ['exact', 'icontains'],
            'is_staff': ['exact', 'icontains'],
            'is_superuser': ['exact', 'icontains'],
        }
