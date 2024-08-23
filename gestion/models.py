from django.db import models
#Si queremos usar las columnas existentes en la tabla authuser y agregar algunas otras columnas que necesitemos, entonces usaremos las clase AbstractUser
#Si queremos eliiminar todas las columnas y crear nuestro modelo aut_user a nuestro antojo entonces usaresmos la clase AbstracBaseUser
#Permisionmixin > es la clase que nos brindará 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4
from cloudinary.models import CloudinaryField

class UsuarioManager(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, password):
        #Este metodo es el que se llamara cuando queramos crear el usuario desde la terminal

        if not correo:
            raise ValueError('El usuario debe tener un correo')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        if not apellido:
            raise ValueError('El usuario debe tener un apellido')
        
        #normalize_email > quita los espacios al comiendo y al final y pone todo a minuscularaspara evitar errores

        correo_normalizado =  self.normalize_email(correo)
        nuevo_usuario = self.model(
            correo = correo_normalizado, nombre = nombre, apellido = apellido)
        
        #set_password > genera el hash del password usando bcrypt como en Flask y lo guarda en la columna password del modelo
        nuevo_usuario.set_password(password)
        
        #is_supervisor > le da a todos los permisos en el panel administrativo a este usuario
        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        #creamos el nuevo usuario en la base de datos
        nuevo_usuario.save()


class Usuario(AbstractBaseUser, PermissionsMixin):
    #Al crear un enum en la base de datos tenemos que indicar cuales son su opcopnes con una lista de listas

    #La primera será usada para guardar en la base de datos
    #mientras que la segunda sera para como lo mostratra´al retornar la informacion de la base de datos
    opcionesTipoUsuario = (['NOVIO', 'NOVIO'], ['INVITADO', 'INVITAD'], ['ADMIN', 'ADMIN'])
    opcionesTipoUsuario = {
            'NOVIO': 'NOVIO', 
            'INVITADO': 'INVITAD', 
            'ADMIN': 'ADMIN'
            }

    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    #emailField > crea una columna de tipo teto pero al momento de crear el registro hace una validacion para que sea un correo
    correo = models.EmailField(null=False, unique=True)
    numeroTelefonico = models.TextField(db_column='numero_telefonico')
    password = models.TextField(null=False)
    tipoUsuario = models.TextField(
        choices=opcionesTipoUsuario, db_column='tipo_usuario')

    #Opcionalmemnte agregaremos las columnas para que funcione el panel administrativo
    #Sirve para ver si el usuario creado pertenece al equipo que peude acceder al panel administrativo porque tambien podemos tener usuarios que no trabajan en la aplicacion osea clientes
    is_staff = models.BooleanField(default=False) 

    #Sirve para ver si el usuario esta activo o no, aperte si no esta activo no podrá ingresar al panel administrativo pero no implica que este sea o no un trabajadaointerno de la empresa
    #Puede darse el caso de que tengamos un trabajados que no trabaja (lo despidieeron)
    is_active = models.BooleanField(default=True) 


    #Sirve para ver si el usuario esta activo o no, aparte si no esta activo no podrá ingresar al penal administrativo pero no implica que esta sea o no un trabajador interno de la empresa
    is_superuser = models.BooleanField(default=False)
    #Para poder realiar el login en el panel administrativo hay que indicar que columna va a utilizar para poder realizar el login
    # esta columna debe ser unica ya que al hacer el login podremos tener problemas si no loes 
    USERNAME_FIELD = 'correo' 

    #Indicar que campos se tienen que solicitar al momento de crear un super usaurio en la terminal nova el USERNAME_FIELD y el password porque ya es implicito
    REQUIRED_FIELDS = ['nombre', 'apellido']

    #Como se va comportar el momento de crear el usuario por la terminal
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'


class ListaNovio(models.Model):
    id = models.AutoField(primary_key=True)
    #Relaciones
    #related_name > es el nombre de la relacion al momento de hacer una FK y sirve para poder acceder desde mi usuario hacia mi lista_novios es decir, servira para cuando realicemos los jpins
    novio = models.ForeignKey(
        to = Usuario, on_delete=models.RESTRICT, db_column='novio_id', null=False, related_name='usuario_novio')
    novia = models.ForeignKey(
        to = Usuario, on_delete=models.RESTRICT, db_column='novia_id', null=False, related_name='usuario_novia')
    
    #Generará automaticamente UUID´s en version 4
    codigo = models.UUIDField(default=uuid4)

    class Meta:
        db_table = 'lista_novios'



class Regalo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo =  models.TextField(null=False)
    descripcion = models.TextField()
    precio = models.FloatField()
    url = models.URLField()

    #Si queremos usar cloud dinaty en una columna podemos usar su clase apara deifnir la columna en el modelo
    imagen = CloudinaryField('imagen') 
    ubicacion = models.TextField()
    cantidad = models.IntegerField(null=False)
    habilitado = models.BooleanField(default=True)
    listaNovio = models.ForeignKey(
        to=ListaNovio, on_delete=models.RESTRICT, db_column='lista_novio_id', null=False)
    
    class Meta:
        db_table ='regalos'

class Reservacion(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(null=False)

    regalo = models.ForeignKey(
        to=Regalo, on_delete=models.RESTRICT, db_column='regalo_id', null=False)
    
    usuario = models.ForeignKey(
        to=Usuario, on_delete=models.RESTRICT, db_column='usuario_id', null=False)
    
    #auto_now_add > cuando se cree un registro se agregue su valor automaticamente a esta columna sin necesidad de pasarle uno
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'reservaciones'