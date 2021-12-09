from home import views
from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage, name='home'),
    path('all_students/', views.home, name='list_of_students'),
    path('cars/', views.brands, name='cars'),
    path('', views.HomeTemplateView.as_view(), name='homepage'),
]




