from rest_framework import serializers
from .models import Usuario, ListaNovio


#ModelSerializar > sirve para crear un serializar Pero basandonos en un moldeo de nuestro Models, es decir, utilizara todos los atributos (Coolumnas) del modelo para hacer las validaciones 


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #fields = '__all__'
        
        exclude = ['password', 'is_staff', 'is_superuser', 'is_active','groups', 'user_permissions']

        #Sirve para agregar configuracion adicional a los atributos de la clase
        extra_kwargs = {
            #write_only > sea utilizado cuando se quiera agreagar un valor a la bs (escritura)
            #read_only > sea utilizado cuando se quiera leer el valor y devolcerlo de la bd
            'last_login': {'write_only': True}
        }

class NovioSerializer(serializers.Serializer):
    #https://www.django-rest-framework.org/api-guide/fields/
    nombre =serializers.CharField(required=True)
    apellido = serializers.CharField(required=True)
    correo = serializers.EmailField(required=True)
    numeroTelefonico = serializers.CharField(required=True)
    password = serializers.CharField()

class ListaNoviosCreacionSerializer(serializers.Serializer):
    novio = NovioSerializer(required=True)
    novia = NovioSerializer(required=True)

class ListaNoviosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaNovio
        fields = '__all__'

        #Si en nuestro modelo actual tenemos llaves foraneas (FK) podemos acceder a su informacion adyacente mediante la profunidad, en base al nuemero que pongamos ingresaremos a cuentos veinos tengamas
        #depth = 1 ingresara la lista de novios y a los novios
        #depth = 2 ingresara la lista de novios y a los novios y a cada novia tendra la lista de novios
        depth = 1

      






