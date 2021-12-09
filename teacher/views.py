from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from student.forms import TeacherForm
from student.models import Student
from teacher.filters import TeacherFilter
from teacher.models import Teacher


class TeacherCreateView(CreateView):
    template_name = 'teacher/teacher.html'
    model = Teacher
    success_url = reverse_lazy('teacher')
    form_class = TeacherForm


class TeacherListView(PermissionRequiredMixin, ListView):
    template_name = 'teacher/teacher_list.html'
    model = Teacher
    context_object_name = 'teacher_list'
    permission_required = 'teacher.view_teacher'

    def get_context_data(self, **kwargs):
        data = super(TeacherListView, self).get_context_data(**kwargs)
        all_teachers = Teacher.objects.all()
        my_filter = TeacherFilter(self.request.GET, queryset=all_teachers)
        all_teachers = my_filter.qs
        data['teacher_list'] = all_teachers
        data['my_filter'] = my_filter
        return data


class TeacherUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/teacher_update.html'
    model = Teacher
    success_url = reverse_lazy('all_teachers')
    form_class = TeacherForm
    permission_required = 'teacher.change_teacher'


class TeacherDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('all_teachers')
    permission_required = 'teacher.delete_teacher'


class TeacherDetailsView(PermissionRequiredMixin, DetailView):
    template_name = 'teacher/details_teacher.html'
    model = Teacher
    permission_required = 'teacher.view_teacher'


def get_all_students_per_teacher(request, id_teacher):

    all_students_per_teacher = Student.objects.filter(teacher_id=id_teacher)
    context = {'students': all_students_per_teacher}

    return render(request, 'student/get_all_students_per_teacher.html', context)
