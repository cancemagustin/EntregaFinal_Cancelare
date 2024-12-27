from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

class UserLoginView(LoginView):
    template_name = 'Login/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            login(request, user)  # Autentica al usuario automáticamente después de registrarse
            return redirect('Main:home')  # Redirige al usuario a la página principal después del registro
    else:
        form = CustomUserCreationForm()

    return render(request, 'Login/register.html', {'form': form})

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('Main:home')

