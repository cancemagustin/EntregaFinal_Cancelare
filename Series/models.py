from django.db import models

class Serie(models.Model):
    titulo = models.CharField(max_length=200)  
    descripcion = models.TextField()  
    fecha_lanzamiento = models.DateTimeField(auto_now_add=True)  
    genero = models.CharField(max_length=100)  
    reparto = models.CharField(max_length=255, default="Desconocido")
    temporada = models.IntegerField()  
    imagen = models.ImageField(upload_to='series_images/', null=True, blank=True)  
    
    
    def __str__(self):
        return self.titulo
