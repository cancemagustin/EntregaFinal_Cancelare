from django.db import models
from multiselectfield import MultiSelectField  
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Generos(models.Model):
    genero = models.CharField(max_length=200)

    def __str__(self):
        return self.genero


class Serie(models.Model):
    PLATAFORMA_CHOICES = [
        ('flow', 'Flow'),
        ('disney_plus', 'Disney Plus'),
        ('max', 'Max'),
        ('amazon_prime', 'Amazon Prime'),
        ('paramount', 'Paramount'),
        ('apple_tv', 'Apple TV'),
        ('netflix', 'Netflix'),
        ('Youtube TV', 'Youtube TV'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)  
    generos = models.ManyToManyField('Generos', through='SerieGenero', blank=True)  
    fecha_lanzamiento = models.DateTimeField(auto_now_add=True)  
    reparto = models.CharField(max_length=255, default="Desconocido", blank=True, null=True)  
    temporada = models.IntegerField(blank=True, null=True) 
    plataformas = MultiSelectField(choices=PLATAFORMA_CHOICES, blank=True, null=True) 
    imagen = models.ImageField(upload_to='Series/', blank=True, null=True) 
    
    def __str__(self):
        return self.titulo

class SerieGenero(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('serie', 'genero')  # Evita duplicados

class SerieGuardada(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('usuario', 'serie')

class Opinion_serie(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    serie = models.ForeignKey('Serie', on_delete=models.CASCADE)
    opinion = models.CharField(max_length=1000)
    estrellas = models.IntegerField()
    

    def save(self, *args, **kwargs):
        print(f"Guardando opinión de {self.usuario} sobre {self.serie}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario} - {self.serie} - {self.estrellas} estrellas"