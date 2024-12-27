from django.db import models

class Serie(models.Model):
    # Definir los campos del modelo
    titulo = models.CharField(max_length=200)  # Título de la serie
    descripcion = models.TextField()  # Descripción detallada de la serie
    fecha_lanzamiento = models.DateTimeField(auto_now_add=True)  # Fecha de lanzamiento
    genero = models.CharField(max_length=100)  # Género de la serie
    temporada = models.IntegerField()  # Número de temporadas
    imagen = models.ImageField(upload_to='series_images/', null=True, blank=True)  # Imagen de la serie (opcional)
    
    # Método para mostrar el título de la serie en el panel de administración de Django
    def __str__(self):
        return self.titulo
