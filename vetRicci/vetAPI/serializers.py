from rest_framework import serializers
from sitioVet.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Mascota
        fields=['idMascota', 'nombre', 'telefonoDuenio', 'idAnimal']

