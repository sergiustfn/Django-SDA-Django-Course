from django.db import models
from teacher.models import Teacher


class Course(models.Model):

    name = models.CharField(max_length=20)
    lenght = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

