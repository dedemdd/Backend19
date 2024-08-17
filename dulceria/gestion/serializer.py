from rest_framework.serializers import ModelSerializer
from .models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        #espedificar que atributos (columnas)vamos a utlizar para la de/serializacion
        #fields = ¨'id','nombre']
        #si queremos utilizar todos los atributos del modelo (tabla)
        fields = '__all__'  
        #si queremos utilizar la mayoria de los atributos pero obviar unos cuanto
        #exclude = ['id']

        # NOTA: no se puede utilizart el fields y el exclude al mismo tiempo, es uno o el otro

