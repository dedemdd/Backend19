from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import Categoria
from .serializer import CategoriaSerializer

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
    queryset = Categoria.objects
    serializer_class = CategoriaSerializer