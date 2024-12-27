from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    enlace = models.URLField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cumpleanos = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)