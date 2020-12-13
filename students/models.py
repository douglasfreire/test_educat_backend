from django.db import models
from lesson.models import Lesson


class Student(models.Model):
    name = models.CharField(max_length=100)
    attendance = models.BooleanField(default=False)
    lessons = models.ManyToManyField(Lesson, related_name='students')

    def __str__(self):
        return self.name
