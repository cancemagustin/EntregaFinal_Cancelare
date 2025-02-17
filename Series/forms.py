from django import forms
from .models import Serie, Opinion_serie
from django.core.validators import MinValueValidator, MaxValueValidator

ESTRELLAS_CHOICES = [
        (1, "⭐ 1"),
        (2, "⭐ 2"),
        (3, "⭐ 3"),
        (4, "⭐ 4"),
        (5, "⭐ 5"),
    ]
class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["titulo", "descripcion", "genero", "temporada", "reparto", "imagen"]
class OpinionSerieForm(forms.ModelForm):
  

    class Meta:
        model = Opinion_serie
        fields = ['opinion', 'estrellas']
        widgets = {
            'opinion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu opinión aquí...'
            }),
            'estrellas': forms.Select(choices=ESTRELLAS_CHOICES, attrs={'class': 'form-select'})
        }

    estrellas = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        widget=forms.Select(choices=ESTRELLAS_CHOICES, attrs={'class': 'form-select'})
    )