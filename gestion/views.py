from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    # Permite que cualquier usuario tenga o no de la token de acceso pueda acceder al endpoint
    AllowAny,
    # Validara que en la peticion se de una token valida y que tenga tiempo de vida
    IsAuthenticated,
    # A parte de la validacion solamente pasara si el usuario es ADMIN (is_superuser = True)
    IsAdminUser,
    # Si el metodo a acceder es GET no sera necesaria la token, caso contrario sera obligatoria (x ejemplo para un post , put, delete)
    IsAuthenticatedOrReadOnly
)

from .models import Usuario, ListaNovio
from .serializer import RegistroSerializer, UsuarioSerializer, ListaNoviosCreacionSerializer, ListaNoviosSerializer
from .permisions import EsAdministrador
from django.db import transaction
from cloudinary import utils
from os import environ
from datetime import datetime


@api_view(http_method_names=['POST'])
def crearUsuario(request):
    body = request.data
    serializador = RegistroSerializer(data=body)

    if serializador.is_valid():
        nuevo_usuario = Usuario(nombre=serializador.validated_data['nombre'],
                                apellido=serializador.validated_data['apellido'],
                                correo=serializador.validated_data['correo'],
                                numeroTelefonico=serializador.validated_data['numeroTelefonico'],
                                tipoUsuario=serializador.validated_data['tipoUsuario'])

        nuevo_usuario.set_password(serializador.validated_data['password'])

        #Solo si estamos utilizando el panel administrativo haremos la siguiente validacion
        if serializador.validated_data['tipoUsuario'] =='ADMIN':
            nuevo_usuario.is_superuser = True
        
        nuevo_usuario.save()

        return Response(data={
            'message': 'Usuario creado exitosamente'
        }, status=status.HTTP_201_CREATED)

    else:
        return Response(data={
            'message': 'Error al crear el usuario',
            'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])

def perfilUsuario(request):

    print(request.user)
    print(request.auth)

    #Cuando queremos pasar una instancia a nuestro serializador, usaremos el parametro instance, sin embargo, si queremos pasarle informacion para que la valide usaremos el parametro data
    serializador = UsuarioSerializer(instance = request.user)


    return Response(data={
        'message': serializador.data
    })

class ListaNoviosAPIView(APIView):
    #Primero validará que el usuario este autenticado y luego validara que sea administrador
    permission_classes = (IsAuthenticated, EsAdministrador)
    def post(self, request):
        serializador = ListaNoviosCreacionSerializer(data=request.data)
        
        if serializador.is_valid():
            print(serializador.validated_data)

            with transaction.atomic():
                # todo lo que hagamos tiene que completarse exitosamente, si algo falla entonces todas las inserciones, actualizaciones y eliminaciones quedaran sin efecto
                nuevoNovio = Usuario(nombre=serializador.validated_data.get('novio').get('nombre'),
                                     apellido=serializador.validated_data.get(
                                         'novio').get('apellido'),
                                     correo=serializador.validated_data.get(
                                         'novio').get('correo'),
                                     tipoUsuario='NOVIO',
                                     numeroTelefonico=serializador.validated_data.get('novio').get('numeroTelefonico'))
                                     

                nuevoNovio.set_password(
                    serializador.validated_data.get('novio').get('password'))

                nuevoNovia = Usuario(nombre=serializador.validated_data.get('novia').get('nombre'),
                                     apellido=serializador.validated_data.get(
                                         'novia').get('apellido'),
                                     correo=serializador.validated_data.get(
                                         'novia').get('correo'),
                                     tipoUsuario='NOVIO',
                                     numeroTelefonico=serializador.validated_data.get(
                                         'novia').get('numeroTelefonico'))


                nuevoNovia.set_password(
                    serializador.validated_data.get('novia').get('password'))

                nuevoNovio.save()
                nuevoNovia.save()

                nuevaLista = ListaNovio(
                    novio=nuevoNovio, novia=nuevoNovia)
                nuevaLista.save()

            return Response(data={
                'message': 'lista creada exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear la lista',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        resultado = ListaNovio.objects.all()
        serializador = ListaNoviosSerializer(instance=resultado, many=True)
        #Si al parametro instance le vamos a pasar una lista entonces tenemos que indicarle al serializador para que pueda hacer la iteracion de la lista y transformar cada uno de los elementos
        return Response(data={
            'content': serializador.data
        })
        

class RegalosAPIView(APIView):
    #Crear un serializador para tener la siguiente informacion de crear un regalo
    #en el campo de la imagen, enviar la url que clouddinary nos brinda, la segura
    #solamente los novios pueden agregar regalos y buscar la lista de novios del novio o novia el cual se quiere agregar el regalo
    def post(self, request):
        
        return Response(data={
            'message': 'Regalo creado exitosamente'
        }, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        #retornar todos los regalos del novio que actualmente esta logueados

        #Select * from lista_novios where novio_id =1 limit 1;
        listaNovioEncontrado = ListaNovio.objects.filter(novio = 1).first()
        #regalos = Regalo.objects.filter(listaNovio = listaNovioEncontrado.id).all()

        return Response(data={
            'message': ''
        })

@api_view(http_method_names=['POST'])
def generarCloudinaryUrl(request):
    timestamp = datetime.now().timestamp()
    signature = utils.api_sign_request(
        {'timestamp': timestamp}, environ.get('CLOUDINARY_API_SECRET'))

    url = f'https://api.cloudinary.com/v1_1/{environ.get('CLOUDINARY_NAME')}/image/upload?api_key={environ.get('CLOUDINARY_API_KEY')}&timestamp={timestamp}&signature={signature}'
    return Response({
        'content': url
    })















