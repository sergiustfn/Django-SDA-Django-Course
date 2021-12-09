import django_filters
from django.db import models

from student.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student

        # fields = {
        #     'first_name': ['icontains'],
        #     'last_name': ['icontains'],
        #     'gender': ['icontains'],
        # }

        fields = ['first_name', 'last_name', 'gender']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains'},
            }
        }

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        self.filters['gender'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control'})
