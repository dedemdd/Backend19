from django.db import models

# Create your models here.
#http://docs.djangoproject.com/en/5.1/topics/db/models/

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True, null=False)

    class Meta:
        #http://docs.djangoproject.com/en/5.1/ref/models/options/
        db_table = 'categorias'

        #Ordena > si cuenta con un -nombre le ordenará de la z a la a, sin el guion lo ordena de la a a la z
        ordering = ['nombre']

class Golosinas(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='/imagenes', null=True)
    habilitado = models.BooleanField(default=True)

    #Relacion con Categoria
    # on_delete > que va a suceder con los registros que tengan relacion con la categoria eliminada
    # CASCADE > elimina la categoria y elimina las golosinas
    # PROTECT > evita la eliminacion de la categoria y lanza un error de tipo ProtectError
    # RESTRICT > similar al PROTECT pero lanzara un error de tipo RestrictedError
    # SET_NULL > elimina la categoria y cambia el valor de la columna categoria_id de sus golosinas a null
    # SET_DEFAULT > elimina la categoria y cambia el valor a un valor por defecto
    # DO_NOTHING > JAMAS USAR ESTO! elimina la categoria y deja como esta el valor de la columna generando incongruencia de datos
    categoria = models.ForeignKey(
        to=Categoria, db_column='categoria_id', on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'golosinas'
        ordering = ['nombre', 'precio']
        #Sirve para crear unicidad enrte dos o mas columnas
        #jamas el nombre y el precio pueden tener el mismo valor juntos
        
        unique_together = ('nombre', 'precio')