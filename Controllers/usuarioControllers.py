from models import UsuarioModel
from instancias import conexion
from flask_restful import Resource, request
from serializers import RegistroSerializer, LoginSerializer
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class RegistroController(Resource):
    def post(self):
        data = request.get_json()
        serializador = RegistroSerializer()
        
        try:
            dataValidada = serializador.load(data)
            print(dataValidada)
            #Proceso de hashing del password 
            salt = gensalt() #un texto aleatorio que seracombinado con la contraseña para generaar el hash de la misma
            password = dataValidada.get('password')
            #convertimos el password a bytes
            passwordBytes= bytes(password, 'utf-8')

            #generara el hash de nuestro password
            hash = hashpw(passwordBytes, salt)
            #decode > convierte los bytes a texto
            hashString = hash.decode('utf-8')

            print(hashString)

            #Ahora modificamos el valor del password por el hash generado
            dataValidada['password'] = hashString

            nuevoUsuario = UsuarioModel(**dataValidada)

            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            resultado = serializador.dump(nuevoUsuario)

            return {
                'message': 'Usuario creado existosamente',
                'content': resultado
            },201
        
        except ValidationError as error:
            return {
                'message': 'Error al crear el usuario',
                'content' : error.args
            }, 400
        
        except IntegrityError as error:
            #Esta es la excepcion cuando el correo en la bd existe
            return {
                'message': 'Error al crear el usuarioe',
                'content' : 'El usuario con correo {} ya existe'.format(data.get('correo'))
            }, 409 #Conflicto (ya existe el recurso)
        

class LoginController(Resource):
    def post(self):
        data = request.get_json()
        serializador = LoginSerializer()
        try:
            dataSerializada = serializador.load(data)
            print(dataSerializada)
            
            #Bsuqen el usuario en la base de datos
            usuarioEncontrado = conexion.session.query(UsuarioModel).where(UsuarioModel.correo == dataSerializada.get('correo')).first()            
                      
            #Sino existe retornar un mensajeque usuario no existe

            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe'
                }, 404
            print(usuarioEncontrado)
            password = usuarioEncontrado.password

            #Converwtimos el passsword a bytes
            passwordBytes = bytes(password, 'utf-8')
            passwordEntranteBytes = bytes(dataSerializada.get('password'),'utf-8')
            validacionPassword = checkpw(passwordEntranteBytes, passwordBytes)

            if validacionPassword == False:
                return {
                    'message': 'Credenciales incorrectas'
                }, 400
            
            informacionAdicional = {
                'correo' : usuarioEncontrado.correo
            }
            jwt = create_access_token(identity=usuarioEncontrado.id, additional_claims=informacionAdicional)
            
            return {
                'message': 'Bienvenido',
                'content': jwt
            }
        
        except ValidationError as error:
            return {
                'message': 'Error al hacer el login',
                'content' : error.args
            }


class PerfilController(Resource):
    #indica que ahora este metodo le enemos quw pasar de manera obligatoria el token y este metodo validará que el token sea correcto y que tenga tiempo de vida y sino no podremos ingresar al mentod
    @jwt_required()
    def get(self):
        #devuelve el identificador del token (id de usuario)
        identificador = get_jwt_identity()
        print(identificador)
        usaurioEncontrado = conexion.session.query(UsuarioModel).where(UsuarioModel.id == identificador).first()
        serializador = RegistroSerializer()
        resultado = serializador.dump(usaurioEncontrado)    

        return {
            'content' : resultado
        }