from django import forms
from django.forms import TextInput, Select

from animal.models import Animal
from student.models import Student
from teacher.models import Teacher


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'date_of_birth',
                  'olympic', 'gender', 'teacher']  # campurile pe care le vrem in formular
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'date_of_birth': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'placeholder': 'Please your gender', 'class': 'form-control'}),
            'teacher': Select(attrs={'placeholder': 'Please select your specialization', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Prenume'
        self.fields['last_name'].required = False


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'specialization', 'active']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class':'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'specialization': Select(attrs={'placeholder': 'Please select your specialization', 'class': 'form-control'}),

        }


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['animal_type', 'animal_name', 'animal_age', 'pure_breed', 'student']

        widgets = {
            'animal_type': TextInput(attrs={'placeholder': 'What type of pet do you have ?', 'class':'form-control'}),
            'animal_name': TextInput(attrs={'placeholder': 'Please enter your pet`s name', 'class':'form-control'}),
            'animal_age': TextInput(attrs={'placeholder': 'Please enter your pet`s age', 'class': 'form-control'}),
            'pure_breed': Select(attrs={'placeholder': 'Is your pet pure breed?', 'class': 'form-control'}),
            'student': Select(attrs={'placeholder': 'Please select the owner of this pet', 'class': 'form-control'})
        }


