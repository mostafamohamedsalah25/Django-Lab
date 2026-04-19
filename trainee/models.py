from django.db import models
from course.models import Course

# Create your models here.
class Trainee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    track = models.CharField(max_length=100, default='Open Source')
    branch = models.CharField(max_length=50, default='Assiut')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='trainees')