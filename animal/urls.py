from django.urls import path
from animal import views

urlpatterns = [
    path('animals/', views.AnimalView.as_view(), name='animal')
]