from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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

def perfil(request):
    return render(request, 'Login/perfil.html')

def about_me(request):
    return render(request, 'Login/about_me.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)  # Asegúrate de pasar 'request.FILES'
        if form.is_valid():
            form.save()
            return redirect('Login:perfil')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'Login/perfil_edit.html', {'form': form})

