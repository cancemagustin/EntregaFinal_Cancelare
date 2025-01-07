from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from .models import Serie, SerieGuardada
from .forms import SerieForm
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib import messages


from django.shortcuts import render
from .models import Serie


def is_superuser(user):
    return user.is_superuser

def serie_update(request, id):
    serie = Serie.objects.get(id=id)
    if request.method == "POST":
        form = SerieForm(request.POST, request.FILES, instance=serie)
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Obtener IDs de series guardadas por el usuario
            context['series_guardadas_ids'] = list(
                SerieGuardada.objects.filter(usuario=self.request.user).values_list('serie_id', flat=True)
            )
        else:
            context['series_guardadas_ids'] = []
        return context
    

    
class SerieDetailView(DetailView):
    model = Serie
    template_name = 'Series/serie_detail.html'
    context_object_name = 'serie'
    
    def get_object(self):
        return get_object_or_404(Serie, id=self.kwargs['id'])
    
@user_passes_test(is_superuser)    
@login_required  
def serie_create(request):
    if request.method == "POST":
        form = SerieForm(request.POST, request.FILES)  
        if form.is_valid():
            serie = form.save(commit=False)
            serie.save()  
            return redirect('Series:serie_list')  
        else:
            return render(request, 'Series/serie_create.html', {'form': form})
    else:
        form = SerieForm()
    
    return render(request, 'Series/serie_create.html', {'form': form})

@login_required
def serie_save(request, id):
    serie = get_object_or_404(Serie, id=id)
    guardado = SerieGuardada.objects.filter(usuario=request.user, serie=serie)

    if guardado.exists():
        guardado.delete()
        messages.success(request, "La serie ha sido desguardada.")
    else:
        SerieGuardada.objects.create(usuario=request.user, serie=serie)
        messages.success(request, "La serie ha sido guardada.")

    return redirect('Series:serie_list')

def serie_saved_list(request):
    series_guardadas = SerieGuardada.objects.filter(usuario=request.user)
    return render(request, 'Series/serie_saved_list.html', {'series_guardadas': series_guardadas})
