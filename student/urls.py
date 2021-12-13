from django.urls import path, include
from rest_framework import routers

from student import views
from student.views import StudentViewSet

router = routers.DefaultRouter()
router.register('api-student', StudentViewSet)

urlpatterns = [
    path('create_student/', views.StudentCreateView.as_view(), name='create-student'),
    path('list_of_students/', views.StudentListView.as_view(), name='list_of_students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete_Student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('detailed_student/<int:pk>/', views.StudentDetailView.as_view(), name='detail_student'),
    path('', include(router.urls))
]
