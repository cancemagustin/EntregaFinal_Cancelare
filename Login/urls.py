from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "Login"

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('user_create/', views.CreateView.as_view(), name='user_create'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),  
    path('editar/perfil/', views.edit_profile, name='edit_profile'),
    path('perfil/<str:username>/', views.perfil, name='perfil'), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)