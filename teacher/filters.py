import django_filters
from django.db import models
from teacher.models import Teacher
from django.db.models import Q

class TeacherFilter(django_filters.FilterSet):

    # q = django_filters.CharFilter(method='my_custom_filter', label='Search')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'specialization', 'created_at']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains'},
            },
        }


    def __init__(self, *args, **kwargs):
        super(TeacherFilter, self).__init__(*args, **kwargs)
        self.filters['created_at'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['specialization'].field.widget.attrs.update({'class': 'form-control'})

