from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.index ,name='index'), 
    path('clientes/', views.clientes, name='clientes'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('consultas/', views.consultas, name='consultas'),
    path('medicos/', views.medicos, name='medicos'),
    path('peluqueria/', views.pelu, name='pelu'),
    path('contacto/', views.contacto, name='contacto'),
    path('vacunacion/', views.vacunacion, name='vacunacion'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('crearmascota/', views.crear, name='crear'),
    path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('modificar/<id>', views.modificar, name='modificar'),
    path('categoria/', views.categoria, name='categoria'),
    ]   
