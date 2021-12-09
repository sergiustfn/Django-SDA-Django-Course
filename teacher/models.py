from django.db import models


class Teacher(models.Model):
    specialization = (('Geography', 'Geography'),
                      ('Math', 'Math'),
                      ('History', 'History'),)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=40, choices=specialization)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
