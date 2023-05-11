from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny

from . import serializers
from . import models


def HomePageView(request):
    pass


# Create your views here.
class CourseSerializer(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CourseSerializer

    def get_queryset(self):
        return models.Course.objects.all()


class CourseDestroyApiView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CourseSerializer

    def get_queryset(self):
        return models.Course.objects.all()


class VideosByCourseAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.VideosSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return models.Videos.objects.filter(course_id=course_id)


class VideosByCourseAPIViewSingle(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.VideosSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return models.Videos.objects.filter(course_id=course_id)
