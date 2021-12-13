from django.urls import path, include
from rest_framework import routers

from teacher import views
from teacher.views import TeacherViewSet

router = routers.DefaultRouter()
router.register('api-teacher', TeacherViewSet)

urlpatterns = [
    path('teacher/', views.TeacherCreateView.as_view(), name='teacher'),
    path('teacher_list/', views.TeacherListView.as_view(), name='all_teachers'),
    path('teacher_update/<int:pk>/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete_teacher'),
    path('teacher_details/<int:pk>/', views.TeacherDetailsView.as_view(), name='teacher_details'),
    path('student_per_teacher/<int:id_teacher>/', views.get_all_students_per_teacher, name='students_per_teacher'),
    path('', include(router.urls))
]







