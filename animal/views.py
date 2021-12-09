from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView
from animal.models import Animal
from student.forms import AnimalForm



class AnimalView(CreateView):
    template_name = 'animal/animal.html'
    model = Animal
    success_url = reverse_lazy('animal')
    form_class = AnimalForm
