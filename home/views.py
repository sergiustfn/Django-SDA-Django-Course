from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def homepage(request):
    return render(request, 'home/homepage.html')


def home(request):
    context = {'all_students': [
        {'first_name': 'Sergiu',
         'last_name': 'Manta',
         'age': 27
         },
        {
            'first_name': 'Mircea',
            'last_name': 'Popovici',
            'age': 32
        }
    ]
    }
    return render(request, 'home/home.html', context)


def brands(request):
    context = {'cars':
        [
        {'car_name': 'Ferrarri',
         'car_year': 1994,
         'previous_owners': 2
         },

        {'car_name': 'Lamborghini',
         'car_year': 2019,
         'previous_owners': 4
         },

        {'car_name': 'Dacia',
         'car_year': 2021,
         'previous_owners': 20
         },

    ]
    }

    return render(request, 'home/cars.html', context)


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'















