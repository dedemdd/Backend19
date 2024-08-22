from django.db import models
#Si queremos usar las columnas existentes en la tabla authuser y agregar algunas otras columnas que necesitemos, entonces usaremos las clase AbstractUser
#Si queremos eliiminar todas las columnas y crear nuestro modelo aut_user a nuestro antojo entonces usaresmos la clase AbstracBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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


class Usuario(AbstractBaseUser):
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
    tipoUsuario = models.TextField(choices=opcionesTipoUsuario)

    #Opcionalmemnte agregaremos las columnas para que funcione el panel administrativo
    #Sirve para ver si el usuario creado pertenece al equipo que peude acceder al panel administrativo porque tambien podemos tener usuarios que no trabajan en la aplicacion osea clientes
    is_staff = models.BooleanField(default=False) 

    #Sirve para ver si el usuario esta activo o no, aperte si no esta activo no podrá ingresar al panel administrativo pero no implica que este sea o no un trabajadaointerno de la empresa
    #Puede darse el caso de que tengamos un trabajados que no trabaja (lo despidieeron)
    is_active = models.BooleanField(default=True) 

    #Para poder realiar el login en el panel administrativo hay que indicar que columna va a utilizar para poder realizar el login
    # esta columna debe ser unica ya que al hacer el login podremos tener problemas si no loes 
    USERNAME_FIELD = 'correo' 

    #Indicar que campos se tienen que solicitar al momento de crear un super usaurio en la terminal nova el USERNAME_FIELD y el password porque ya es implicito
    REQUIRED_FIELDS = ['nombre', 'apellido']

    #Como se va comportar el momento de crear el usuario por la terminal
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'