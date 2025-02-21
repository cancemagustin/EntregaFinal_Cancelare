from django.shortcuts import render
from django.shortcuts import render
from Series.models import Serie, Generos

# Create your views here.

def index(request):
    return render(request, 'Main/index.html')

def home(request):
    series = Serie.objects.all().order_by('?')  # Mezcla las series aleatoriamente
    ultimas_5_series = Serie.objects.all().order_by('-fecha_lanzamiento')[:5] 
    generos = Generos.objects.prefetch_related('seriegenero_set').all()


    
    print("Últimas 5 series:")
    for s in ultimas_5_series:  
        print(s.titulo, s.fecha_lanzamiento)



    return render(request, 'Main/home.html', {'series': series, 'ultimas_5_series': ultimas_5_series, 'generos': generos})
