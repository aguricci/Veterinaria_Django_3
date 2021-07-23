from sitioVet.models import Mascota
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from vetAPI.serializers import MascotaSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def mascotas(request):
    if request.method == 'GET':
        info = Mascota.objects.all()
        serial = MascotaSerializer(info, many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = MascotaSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def metodos(request, id):
    try: 
        info = Mascota.objects.get(idMascota=id)
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = MascotaSerializer(info)
        return Response(serial.data)

    elif request.method == 'PUT':
        serial = MascotaSerializer(info, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

