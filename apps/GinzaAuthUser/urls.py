from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

urlpatterns = [
    path('register/', CustomUserRegister.as_view(), name='registration'),
    path('delete/', DeleteUser.as_view(), name='delete'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('token/', MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
