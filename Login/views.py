from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import CustomUser
from Series.models import Opinion_serie
from Friends.models import seguidos

class UserLoginView(LoginView):
    template_name = 'Login/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Main:home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'Login/register.html', {'form': form})

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('Main:home')

def about_me(request):
    return render(request, 'Login/about_me.html')

@login_required
def perfil(request, username=None):
    if username:
        usuario = get_object_or_404(CustomUser, username=username)
    else:
        usuario = request.user 
    
    opiniones = Opinion_serie.objects.filter(usuario=usuario)
    sigue = seguidos.objects.filter(seguidor=request.user, sigue=usuario).exists()
    return render(request, 'Login/perfil.html', {'usuario': usuario, 'opiniones': opiniones, 'sigue': sigue})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)  
        if form.is_valid():
            form.save()
            return redirect('Login:perfil')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'Login/perfil_edit.html', {'form': form})


def mi_vista(request):
    return render(request, 'tu_template.html', {
        'profile': request.user.profile
        
    })



