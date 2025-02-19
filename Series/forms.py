from django import forms
from .models import Serie

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["titulo", "descripcion", "genero", "temporada", "reparto", "imagen"]
