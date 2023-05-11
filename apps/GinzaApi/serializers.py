from rest_framework import serializers
from . import models


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    class Meta:
        model = models.Course
        fields = [
            'id',
            'name',
            'description',
            'price',
            'image',
            'type',
            'date',
            'token_course',
            'video_count',
            'teacher_name',
        ]

    video_count = serializers.SerializerMethodField()
    def get_video_count(self, obj):
        return models.Videos.objects.filter(course_id=obj.id).count()



class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Videos
        fields = [
            'id',
            'title',
            'link',
            'course'
        ]
