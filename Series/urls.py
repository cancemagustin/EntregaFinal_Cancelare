from django.urls import path
from . import views

app_name = 'Series'

urlpatterns = [
    path('serie/', views.SerieListView.as_view(), name='serie_list'), 
    path('serie/<int:id>/', views.SerieDetailView.as_view(), name='serie_details'),
    path('serie/create',views.serie_create, name="serie_create"),
    path('serie/update/<int:id>/', views.serie_update, name='serie_update'),
    path('serie/delete/<int:id>/', views.serie_delete, name='serie_delete'),


]