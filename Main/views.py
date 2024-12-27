from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Main/index.html')

def home(request):
    return render(request, 'Main/home.html')


