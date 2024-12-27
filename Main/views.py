from django.shortcuts import render
from django.shortcuts import render
from Series.models import Serie

# Create your views here.

def index(request):
    return render(request, 'Main/index.html')

def home(request):
    
    series = Serie.objects.all()[:5]  
    return render(request, 'Main/home.html', {'series': series})


