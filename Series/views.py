from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Serie
from .forms import SerieForm
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib import messages

# Create your views here.

def serie_update(request, id):
    serie = Serie.objects.get(id=id)
    if request.method == "POST":
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect("Series:serie_list")
    else:
        form = SerieForm(instance=serie)
    return render(request, 'Series/serie_update.html', context={"form": form, "serie": serie})

def serie_delete(request,id):
    serie = get_object_or_404(Serie, id=id)
    if request.method=="POST":
        serie.delete()
        return redirect("Series:serie_list")
    return render(request, 'Series/serie_delete.html', {"serie":serie})


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
    
@login_required  # Asegúrate de que el usuario esté autenticado
def serie_create(request):
    if request.method == "POST":
        form = SerieForm(request.POST, request.FILES)  # Asegúrate de pasar 'request.FILES' para manejar imágenes
        if form.is_valid():
            # Si el formulario es válido, lo guardamos
            serie = form.save(commit=False)
            serie.save()  # Guardamos la instancia de la serie
            return redirect('Series:serie_list')  # Redirige a la lista de series
        else:
            # Si hay errores, los mostramos
            return render(request, 'Series/serie_create.html', {'form': form})
    else:
        form = SerieForm()
    
    return render(request, 'Series/serie_create.html', {'form': form})