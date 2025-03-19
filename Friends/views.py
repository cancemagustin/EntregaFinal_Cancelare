from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import seguidos
from Series.models import Opinion_serie
from django.contrib.auth import get_user_model

User = get_user_model()
@login_required
def seguir_usuario(request, usuario_id):
    User = get_user_model()
    usuario_a_seguir = get_object_or_404(User, id=usuario_id)
    if request.user != usuario_a_seguir:  
        seguidos.objects.get_or_create(seguidor=request.user, sigue=usuario_a_seguir)
    return redirect(request.META.get('HTTP_REFERER', request.path))


@login_required
def dejar_de_seguir_usuario(request, usuario_id):
    User = get_user_model()
    usuario_a_dejar = get_object_or_404(User, id=usuario_id)

    seguimiento = seguidos.objects.filter(seguidor=request.user, sigue=usuario_a_dejar)
    if seguimiento.exists():
        seguimiento.delete()

    return redirect(request.META.get('HTTP_REFERER', request.path))


@login_required
def lista_seguidores(request, username):
    usuario_perfil = get_object_or_404(User, username=username)  # Usuario del perfil
    usuario_actual = request.user  # Usuario logueado

    # Obtener quiénes siguen al usuario del perfil (lista de objetos)
    seguidores_qs = seguidos.objects.filter(sigue=usuario_perfil).select_related('seguidor')

    # Lista de nombres de usuarios que siguen al usuario del perfil
    seguidores_list = seguidores_qs.values_list('seguidor__username', flat=True)

    # Obtener todos los usuarios, excluyendo al usuario del perfil
    todos_usuarios = User.objects.exclude(id=usuario_perfil.id)

    # Filtrar sugeridos (usuarios que no están en seguidores_list)
    sugeridos = todos_usuarios.exclude(username__in=seguidores_list)
    
    seguidores_usuario_actual = seguidos.objects.filter(seguidor=usuario_actual).values_list('sigue__id', flat=True)

    # Verificar si el usuario actual sigue al usuario del perfil
    sigue = seguidos.objects.filter(seguidor=usuario_actual, sigue=usuario_perfil).exists()

    return render(request, 'Friends/seguidores.html', {
        'usuario_perfil': usuario_perfil, 
        'seguidores': seguidores_qs,  # QuerySet con los objetos seguidores
        'seguidores_list': seguidores_list,  # Lista de nombres de usuario que siguen al perfil
        'todos_usuarios': todos_usuarios,
        'sugeridos': sugeridos,  # Lista de usuarios sugeridos
        'sigue': sigue,  # True si el usuario logueado sigue al usuario del perfil
        'seguidores_usuario_actual': seguidores_usuario_actual 
    })

@login_required
def lista_seguidos(request, username):
    usuario_perfil = get_object_or_404(User, username=username)  # Usuario del perfil
    usuario_actual = request.user  # Usuario logueado

    # Obtener a quién sigue el usuario del perfil (lista de objetos)
    seguidos_qs = seguidos.objects.filter(seguidor=usuario_perfil).select_related('sigue')

    # Lista de nombres de usuarios seguidos
    seguidos_list = seguidos_qs.values_list('sigue__username', flat=True)

    # Obtener todos los usuarios, excluyendo al usuario del perfil
    todos_usuarios = User.objects.exclude(id=usuario_perfil.id)

    # Filtrar sugeridos (usuarios que no están en seguidos_list)
    sugeridos = todos_usuarios.exclude(username__in=seguidos_list)
    
    seguidos_usuario_actual = seguidos.objects.filter(seguidor=usuario_actual).values_list('sigue__id', flat=True)


    # Verificar si el usuario actual sigue al usuario del perfil
    sigue = seguidos.objects.filter(seguidor=usuario_actual, sigue=usuario_perfil).exists()

    return render(request, 'Friends/seguidos.html', {
        'usuario_perfil': usuario_perfil, 
        'seguidos': seguidos_qs,  # QuerySet con los objetos seguidos
        'seguidos_list': seguidos_list,  # Lista de nombres de usuario seguidos
        'todos_usuarios': todos_usuarios,
        'sugeridos': sugeridos,  # Lista de usuarios sugeridos
        'sigue': sigue,  # True si el usuario logueado sigue al usuario del perfil
        'seguidos_usuario_actual': seguidos_usuario_actual 
    })



def mi_red(request, username):
    usuario_perfil = get_object_or_404(User, username=username)
    usuario_actual = request.user 

    if not usuario_actual.is_authenticated:
        return redirect('login') 

    seguidos_list = seguidos.objects.filter(seguidor=usuario_perfil).select_related('sigue')

    # Obtener las opiniones del usuario del perfil
    opiniones_list = Opinion_serie.objects.filter(usuario=usuario_perfil)

    # Obtener la lista de usuarios a los que sigue
    usuarios_seguidos = [s.sigue for s in seguidos_list]

    # Obtener opiniones de los usuarios seguidos
    opiniones_seguidos = Opinion_serie.objects.filter(usuario__in=usuarios_seguidos)

    # Verificar si el usuario actual sigue al usuario del perfil
    sigue = seguidos.objects.filter(seguidor=usuario_actual, sigue=usuario_perfil).exists()

    return render(request, 'Friends/red.html', {
        'usuario_perfil': usuario_perfil, 
        'seguidos': seguidos_list,
        'sigue': sigue,
        'opiniones': opiniones_list,  # Opiniones del usuario del perfil
        'opiniones_seguidos': opiniones_seguidos  # Opiniones de los que sigue
    })