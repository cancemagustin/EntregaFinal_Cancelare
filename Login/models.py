from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    enlace = models.URLField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cumpleanos = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

