from django.contrib import admin
from apps.GinzaApi.models import Course, Teacher, Videos

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'age', 'user', 'created_at']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'type', 'teacher', 'date_joined']
    list_editable = ['price', 'type']

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'course', 'link']
    list_editable = ['title', 'course', 'link']
