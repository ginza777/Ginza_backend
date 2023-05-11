from django.urls import path
from .views import *

urlpatterns = [
    path("user/", UserListView.as_view()),  # list all users
    path("user/<int:pk>", UserbyID.as_view()),  # find user by id
    path("user_search/", UsernameListSearch.as_view()),  # find user by username
    path("user_search/<str:username>", UsernameSearch.as_view()),  # user search by username retriveview
    path("userl/filter/", UserFilter.as_view()),  # user search by custom filterset class
    path("custom/", CustomFilter.as_view()),  # custom dynamic filter
    # product section
    path("product/list", ProductListView.as_view()),  # list all products and filter
    path("product/price/", ProductFilterView.as_view()),  # list all products

]
