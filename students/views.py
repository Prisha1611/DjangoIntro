from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def classes(request):
    return render(request, 'classes.html')