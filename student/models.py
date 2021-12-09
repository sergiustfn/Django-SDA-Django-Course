from django.db import models
from teacher.models import Teacher


class Student(models.Model):
    gender_choices = (('Male', 'Male'),
                      ('Female', 'Female'),
                      ('Other', 'Other'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    olympic = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




