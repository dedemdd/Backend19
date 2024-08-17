#Aca irán todas las rutas relacionadas a la aplicacion gestion
from django.urls import path
from .views import (paginaPrueba, CategoriasAPIView, 
                    CrearCategoriasAPIView, CrearListarCategoriasAPIView, DevolverActualizaEliminarCategoriaAPIView, GolosinasAPIView)



urlpatterns = [
    path('prueba', paginaPrueba),    
    path('categorias', CategoriasAPIView.as_view()),
    path('crear-categoria', CrearCategoriasAPIView.as_view()), 
    path('listar-crear-categoria', CrearListarCategoriasAPIView.as_view()), 
    #una vista generica que sea Retrive, Update, Destroy o la combinaciones de ellas
    path('categoria/<id>', DevolverActualizaEliminarCategoriaAPIView.as_view()),  
    path('golosinas', GolosinasAPIView.as_view()),  
    
]

