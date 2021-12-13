from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'age', 'date_of_birth', 'gender',
        ]
