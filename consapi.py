import re
import requests
from requests.api import post
URL = 'http://127.0.0.1:8000/api/'
opcion = 0
while opcion != 6:
    
    
    
    print("Opcion 1: Obtener todas las mascotas")
    print("Opcion 2: Obtener solamente una mascota")
    print("Opcion 3: Crear una mascota")
    print("Opcion 4: Modificar una mascota")
    print("Opcion 5: Eliminar una mascota")
    print ("Opcion 6: Salir\n")
    opcion =int(input("Ingrese una opcion:"))

    if opcion == 1:
        response = requests.get(URL)
        for i in response.json():
            print(i)

    elif opcion == 2:
        id = 0
        id = input("Ingrese el id de su mascota:")
        response = requests.get(URL + 'mascota/' + id)
        if response.status_code == 404:
            print("Datos no encontrados")
        else:
            print(response.json())
    elif opcion == 3:

        idMascota = 0
        nombre = ''
        telefonoDuenio = ''
        idAnimal = 0

        idMascota = int(input("Ingrese el id de su macota:  ")) 
        nombre = input("Ingrese el nombre de su mascota:  ")
        telefonoDuenio = input("Ingrese su numero de telefono incluyendo el codigo de pais (+56):  ")
        idAnimal = int(input("Ingrese id animal:  "))
        contenido = {'idMascota' : idMascota, 'nombre' : nombre, 'telefonoDuenio' : telefonoDuenio, 'idAnimal' : idAnimal}
        response = requests.post(URL, data=contenido )
        if response.status_code == 201:
            print("Mascota creada correctamente")
        else:
            print("Id no disponible")
        
    elif opcion == 4:
        idMascota = 0
        nombre = ''
        telefonoDuenio = ''
        idAnimal = 0
        idMascota = int(input("Ingrese el id de la mascota que desea modificar:  "))
        response = requests.get(URL + 'mascota/' + str(idMascota))
        if response.status_code == 404:
            print("Error al buscar mascota")
        else:
            info = response.json()
            nombre = input("Ingrese el nuevo nombre:  ")
            telefonoDuenio = input("Ingrese el nuevo numero de telefono: ")
            idAnimal = info['idAnimal']
            contenido = {'idMascota' : idMascota, 'nombre' : nombre, 'telefonoDuenio' : telefonoDuenio, 'idAnimal' : idAnimal}
            actualizar = requests.put(URL + 'mascota/' + str(idMascota), data=contenido )
            print("Mascota actualizada correctamente")
    
    elif opcion == 5:
        idMascota = input("Ingrese el id de la mascota que desea eliminar:  ")
        eliminar = requests.delete(URL + 'mascota/' + idMascota)
        if eliminar.status_code == 204:
            print("Mascota eliminada exitosamente!!!")
        else:
            print("La mascota no existe")
    
    else: 
        print("Opcion invalida")
