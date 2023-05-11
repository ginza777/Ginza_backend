from django.db import models
from django.utils import timezone
import uuid
from apps.GinzaAuthUser.models  import CustomUser

class Teacher(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True,limit_choices_to={'is_active': True})
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    token_teacher = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='teachers/images', blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(default='Bepul', max_length=200)
    image = models.ImageField(upload_to='courses/images', blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True, choices=(
        ('Faster', 'Faster'), ('Practice', 'Practice'), ('Special', 'Special'), ('SpecialPractice', 'SpecialPractice')))
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    date_joined = models.DateTimeField(default=timezone.now)
    token_course = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Videos(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title
