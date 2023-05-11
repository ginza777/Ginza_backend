from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models


def HomePageView(request):
    return render(request, 'index.html')


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


class VideosByCourseAPIViewSingle(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.VideosSerializer

    def get(self, request, pk):
        course_id = pk
        print(course_id)
        videos = models.Videos.objects.filter(course__id=course_id)
        serializer = serializers.VideosSerializer(videos, many=True)
        return Response(serializer.data)
