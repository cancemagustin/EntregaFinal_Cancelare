from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import seguir_usuario, dejar_de_seguir_usuario, lista_seguidos, lista_seguidores, mi_red

app_name = "Friends"

urlpatterns = [
    path("seguir/<int:usuario_id>/", seguir_usuario, name="seguir_usuario"),
    path("dejar_de_seguir/<int:usuario_id>/", dejar_de_seguir_usuario, name="dejar_de_seguir"),
    path("seguidos/<str:username>/", lista_seguidos, name="lista_seguidos"),
    path('seguidores/<str:username>/', lista_seguidores, name='lista_seguidores'),
    path('mi_red/<str:username>/', mi_red, name='mi_red'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)