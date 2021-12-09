from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from userextend.forms import UserExtendForm

#folosim clasa CreateVIew pentru a crea formul care ne va ajuta sa



class CreateUser(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    success_url = reverse_lazy('create_user')
    form_class = UserExtendForm

