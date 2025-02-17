from django.db import models
from django.conf import settings

# Create your models here.

class seguidos(models.Model):
    seguidor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sigue")
    sigue = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seguidores")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seguidor', 'sigue')