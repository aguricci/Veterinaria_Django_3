from django.urls import path
from . import views
urlpatterns = [
    path('', views.mascotas, name='mascotas'),
    path('mascota/<id>', views.metodos, name='metodos'),
]
