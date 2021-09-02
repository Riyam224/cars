from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Car

def index(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return  render(request , 'index.html', context)


def car_details(request , id):
    car  = get_object_or_404(Car , id=id)
    context = {
        'car': car,
    }
    return render(request , 'details.html', context)