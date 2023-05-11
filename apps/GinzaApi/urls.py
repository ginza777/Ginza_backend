from django.urls import path
from . import views

urlpatterns = [

    path('api/courses/', views.CourseSerializer.as_view()),
    path('api/courses/<int:pk>', views.CourseDestroyApiView.as_view()),
    path('api/courses/<int:pk>/videos/', views.VideosByCourseAPIViewSingle.as_view(), ),
]
