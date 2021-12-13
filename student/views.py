from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets
from student.filters import StudentFilter
from student.forms import StudentForm
from student.models import Student
from student.serializers import StudentSerializer


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'  #calea catre fisierul html unde va fi afisat forumlarul
    model = Student  # modelul pe care il folosim in generarea formularului nostru
    # fields = '__all__' # returneaza toate field-urile din model
    success_url = reverse_lazy('create-student') #redirectionarea dupa ce formularul a fost validat.
    form_class = StudentForm
    permission_required = 'student.add_student'


class StudentListView(PermissionRequiredMixin, ListView):
    template_name = 'student/list_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_student'

    def get_context_data(self, **kwargs):
        data = super(StudentListView, self).get_context_data(**kwargs)
        all_students = Student.objects.all()
        my_filter = StudentFilter(self.request.GET, queryset=all_students)
        all_students = my_filter.qs
        data['all_students'] = all_students
        data['my_filter'] = my_filter
        return data


class StudentUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    form_class = StudentForm
    permission_required = 'student.change_student'


class StudentDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    form_class = StudentForm
    permission_required = 'student.delete_student'


class StudentDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'student/detail_student.html'
    model = Student
    permission_required = 'student.view_student'


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

