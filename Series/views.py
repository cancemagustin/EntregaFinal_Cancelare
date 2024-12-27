from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Serie
from .forms import SerieForm
from django.views.generic import ListView, DetailView
from django.contrib import messages

# Create your views here.

class SerieListView(ListView):
    model = Serie
    template_name = "Series/serie_list.html"
    context_object_name = "serie"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

    
class SerieDetailView(DetailView):
    model = Serie
    template_name = 'Series/serie_detail.html'
    context_object_name = 'serie'
    
    def get_object(self):
        return get_object_or_404(Serie, id=self.kwargs['id'])
    

@login_required
def serie_create(request):
    if request.method == "POST":
        form = SerieForm(request.POST, request.FILES)
        if form.is_valid():
            serie = form.save(commit=False)
            serie.save()
            return redirect('Series:serie_list')
        else:
            # Si el formulario no es válido, mostrar mensaje de error genérico
            messages.error(request, "Ha ocurrido un error al guardar la serie.")
    else:
        form = SerieForm()

    return render(request, 'Series/serie_create.html', {'form': form})