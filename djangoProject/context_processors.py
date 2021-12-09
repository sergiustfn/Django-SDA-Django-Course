from course.models import Course
from teacher.models import Teacher


def get_all_teachers(request):
    all_teachers = Teacher.objects.all()
    return {'teachers': all_teachers}


def get_all_courses(request):
    all_courses = Course.objects.all()
    return {'courses': all_courses}







