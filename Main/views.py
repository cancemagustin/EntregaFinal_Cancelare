from django.shortcuts import render
from django.shortcuts import render
from Series.models import Serie, Generos
from django.db.models import Avg
import random

# Create your views here.

def home(request):
    series = Serie.objects.all()


    top_5_series = Serie.objects.annotate(promedio_estrellas=Avg('opinion_serie__estrellas')) \
    .order_by('-promedio_estrellas')[:5]

    generos = Generos.objects.prefetch_related('seriegenero_set').all()

    for genero in generos:
        series_genero = list(genero.seriegenero_set.all())  # me devuelve todas las series de tal genero
        random.shuffle(series_genero)  
        genero.series_aleatorias = random.sample(series_genero, min(10, len(series_genero)))


    return render(request, 'Main/home.html', {
        'series': series,
        'top_5_series': top_5_series,
        'generos': generos
    })