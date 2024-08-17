#Aca irán todas las rutas relacionadas a la aplicacion gestion
from django.urls import path
from .views import paginaPrueba, CategoriasAPIView, CrearCategoriasAPIView



urlpatterns = [
    path('prueba', paginaPrueba),    
    path('categorias', CategoriasAPIView.as_view()),
    path('crear-categoria', CrearCategoriasAPIView.as_view()), 
]

