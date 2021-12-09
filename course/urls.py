from django.urls import path

from course import views

urlpatterns = [

    path('course_teacher/<int:pk>/', views.get_all_courses_per_teacher, name='course_per_teacher'),
    path('teacher_course/<int:pk>', views.get_all_teachers_per_course, name='teacher_per_course'),
]

