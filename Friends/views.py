from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import seguidos
from django.contrib.auth import get_user_model

User = get_user_model()
@login_required
def seguir_usuario(request, usuario_id):
    User = get_user_model()
    usuario_a_seguir = get_object_or_404(User, id=usuario_id)

    if request.user != usuario_a_seguir:  # Evita que un usuario se siga a sí mismo
        seguidos.objects.get_or_create(seguidor=request.user, sigue=usuario_a_seguir)

    return redirect('Login:perfil', username=usuario_a_seguir.username)  # ✅ Redirige a 'perfil'


@login_required
def dejar_de_seguir_usuario(request, usuario_id):
    User = get_user_model()
    usuario_a_dejar = get_object_or_404(User, id=usuario_id)

    seguimiento = seguidos.objects.filter(seguidor=request.user, sigue=usuario_a_dejar)
    if seguimiento.exists():
        seguimiento.delete()

    return redirect('Login:perfil', username=usuario_a_dejar.username)  # ✅ Corrige la redirección


@login_required
def lista_seguidores(request):
    usuario = request.user
    seguidores = seguidos.objects.filter(sigue=usuario).select_related('seguidor')  # Quiénes te siguen
    seguidos_list = seguidos.objects.filter(seguidor=usuario).select_related('sigue')  # A quiénes sigues

    # Obtener todos los usuarios del sistema, excluyendo al usuario actual
    todos_usuarios = User.objects.exclude(id=usuario.id)

    # Filtrar los que NO están en seguidores ni seguidos
    sugeridos = todos_usuarios.exclude(id__in=[s.seguidor.id for s in seguidores]).exclude(id__in=[s.sigue.id for s in seguidos_list])

    return render(request, 'Friends/seguidores.html', {
        'seguidores': seguidores,
        'sugeridos': sugeridos  # Lista de usuarios sugeridos
    })

@login_required
def lista_seguidos(request):
    usuario = request.user
    seguidos_list = seguidos.objects.filter(seguidor=usuario).select_related('sigue')  # A quiénes sigues

    # Obtener todos los usuarios del sistema, excluyendo al usuario actual
    todos_usuarios = User.objects.exclude(id=usuario.id)

    # Filtrar los que NO están en seguidos
    sugeridos = todos_usuarios.exclude(id__in=[s.sigue.id for s in seguidos_list])

    return render(request, 'Friends/seguidos.html', {
        'seguidos': seguidos_list,
        'sugeridos': sugeridos  # Lista de usuarios sugeridos
    })