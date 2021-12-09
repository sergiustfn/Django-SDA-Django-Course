from django.db import models

from student.models import Student


class Animal(models.Model):
    is_pure = (('Yes', 'Yes'), ('No', 'No'))

    animal_type = models.CharField(max_length=50)
    animal_name = models.CharField(max_length=50)
    animal_age = models.IntegerField()
    pure_breed = models.CharField(max_length=50, choices=is_pure)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.animal_name} {self.animal_type}"






