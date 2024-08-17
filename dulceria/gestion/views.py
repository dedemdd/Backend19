from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Categoria, Golosinas
from .serializer import CategoriaSerializer, GolosinaSerializer
from rest_framework import status


# Create your views here.
def paginaPrueba(request):
    print(request)
    data = [{
        "id": 1,
        "nombre": "Importados",
        "habilitado": True
    }, {
        "id": 2,
        "nombre": "Nacionales",
        "habilitado": False
    }]

    usuario = 'Eduardo'
    return render(request, 'prueba.html', {"data" : data, "usuario" : usuario})


class CategoriasAPIView(APIView):
    def get(self, request):
        return Response(data = {
            'message' : 'ok'
        }, status = 200)
    
    def post(self, request):
        return Response(data = {
            'message' : 'me hiciste el POST'
        }, status = 201)

class CrearCategoriasAPIView(CreateAPIView):
    #los atributos necesarios 
    # SELECT * FROM CATEGORIAS
    queryset = Categoria.objects
    serializer_class = CategoriaSerializer

class CrearListarCategoriasAPIView(ListCreateAPIView):
    #los atributos necesarios 
    # SELECT * FROM CATEGORIAS
    queryset = Categoria.objects
    serializer_class = CategoriaSerializer


class DevolverActualizaEliminarCategoriaAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #Si queremos cambiar el valor del parametro por la URL de pk a uno personalizado usaremos el atributo lookup_field
    lookup_field_name ='id'


class GolosinasAPIView(APIView):
    def post(self, request):
        #Obtener la informacion del boy del parent
        data = request.data #Conveirete a un dic

        serializador = GolosinaSerializer(data = data)
        validacion = serializador.is_valid()

        if validacion:
            #en los serializadores se pueden guardar en la base de datos diretamente
            nuevaGolosinaCreada = serializador.save()

                        # nuevaGolosina = Golosina(nombre=serializador.validated_data.get('nombre'),
            #                          precio=serializador.validated_data.get(
            #                              'precio'),
            #                          habilitado=serializador.validated_data.get(
            #                              'habilitado'),
            #                          categoria=serializador.validated_data.get('categoria'))
            
            #nuevaGolosina =  Golosinas(**serializador.validate_data)
            #nuevaGolosina.save()

            #Si queremos validar que la informacion a guardar o actializar es correcta usaremos el pararemtro data caso contrario si queremos converstir una instancia a una dicciona (deserializar)
            
            resultado = GolosinaSerializer(instance = nuevaGolosinaCreada)
            return Response(data= {
                'message':'Golosina creada exitosamente',
                'content': resultado.data
            }, status=status.HTTP_201_CREATED)
            
        else:
            #Si la data no es valida (is_valid()), entonces los errores se almacenaran en el diccionario error
            return Response(data = {
                'message':'Error al crear la golosina',
                'content':serializador.errors
                }, status=status.HTTP_400_BAD_REQUEST)















