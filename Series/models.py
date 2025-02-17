from django.db import models
from multiselectfield import MultiSelectField  
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Serie(models.Model):
    GENERO_CHOICES = [
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('accion', 'Acción'),
        ('terror', 'Terror'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('romance', 'Romance'),
        ('documental', 'Documental'),
        ('Fantasía', 'Fantasía'),
        ('misterio', 'Misterio'),
        ('aventura', 'Aventura'),
        ('política', 'Política'),
    ]

    titulo = models.CharField(max_length=200)  
    descripcion = models.TextField()  
    fecha_lanzamiento = models.DateTimeField(auto_now_add=True)  
    genero = MultiSelectField(choices=GENERO_CHOICES) 
    reparto = models.CharField(max_length=255, default="Desconocido")
    temporada = models.IntegerField()  
    imagen = models.ImageField(upload_to='series_images/', null=True, blank=True)  
    
    def __str__(self):
        return self.titulo

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