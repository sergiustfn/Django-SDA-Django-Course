from django.shortcuts import render

from course.models import Course
from teacher.models import Teacher


def get_all_courses_per_teacher(request, pk):

    all_courses_per_teacher = Course.objects.filter(teacher_id=pk)

    context = {'courses_per_teacher': all_courses_per_teacher}
    return render(request, 'courses/get_all_courses_per_teacher.html', context)

def get_all_teachers_per_course(request, pk):

    all_teachers_per_course = Teacher.objects.filter(id=pk)
    context = {'teachers_per_course': all_teachers_per_course}
    return render(request, 'courses/get_all_teachers_per_course.html', context)





