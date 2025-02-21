from django import forms
from .models import Serie, Opinion_serie, Generos
from django.core.validators import MinValueValidator, MaxValueValidator

ESTRELLAS_CHOICES = [
        (1, "⭐ 1"),
        (2, "⭐ 2"),
        (3, "⭐ 3"),
        (4, "⭐ 4"),
        (5, "⭐ 5"),
    ]
class SerieForm(forms.ModelForm):
    generos = forms.ModelMultipleChoiceField(
        queryset=Generos.objects.all(),  # Carga todos los géneros disponibles
        widget=forms.CheckboxSelectMultiple(),  # Usa checkboxes para seleccionar múltiples
        required=False  # No es obligatorio elegir un género
    )

    class Meta:
        model = Serie
        fields = ["titulo", "descripcion", "generos", "temporada", "reparto", "imagen", "plataformas"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Si la serie ya existe, preseleccionamos sus géneros
            self.fields["generos"].initial = self.instance.generos.all()
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Generos
        fields = ['genero']
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