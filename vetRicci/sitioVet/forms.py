from django.db.models import fields
from django.forms import ModelForm
from .models import Mascota, Animal

class Agregamascota(ModelForm):
    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombre', 'telefonoDuenio', 'idAnimal']


class Agregacategoria(ModelForm):
    class Meta:
        model = Animal
        fields = ['idAnimal', 'nombreAnimal']