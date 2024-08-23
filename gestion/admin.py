from django.contrib import admin
from .models import Usuario


#Si queremos hacer una configuracion adicional a los modelos, esntonces usaremos una clase

class UsuarioAdmin(admin.ModelAdmin):
    #Mensaje en el caso que en una columna no exista valor
    empty_value_display = 'NO HAY'
    
    #Como queremos mostrar los registros de nuestro modelo
    list_display = ['nombre', 'apellido', 'correo']

    #Lista de atrbutos en las cuales queremos exluir para ya sea crear o actualizar nuestro registro
    exclude = ['nombre']


    #Indicar en que columnas yo puedo seleccionar al usuario para su informacion o editarlos
    list_display_links = ['nombre', 'apellido']

    #Sirve para poder agregar un filtrado en nuestro modelo y esto servira para una busqeuda mas rapidad
    list_filter = ['nombre', 'apellido']

    #Agrega un buscador y se la coloca los atributis que tiene que buscar, no es sensible a mayuscullas o minusculas
    search_fields = ['nombre']

admin.site.register(Usuario, UsuarioAdmin)


