from django.urls import path
from userextend import views


urlpatterns = [

    path('create_user', views.CreateUser.as_view(), name='create_user'),

]


