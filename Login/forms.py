
from django.contrib.auth.models import User
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2','email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'enlace', 'descripcion', 'cumpleanos', 'avatar']