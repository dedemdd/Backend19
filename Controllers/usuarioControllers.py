from models import UsuarioModel
from instancias import conexion
from flask_restful import Resource, request
from serializers import (RegistroSerializer, 
                         LoginSerializer, 
                         ActualizarUsuarioSerializer, 
                         CambiarPasswordSerializer, ResetearPasswordSerializer)
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utilitarios import enviarCorreo


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
        usuarioEncontrado = conexion.session.query(UsuarioModel).where(UsuarioModel.id == identificador).first()
        serializador = RegistroSerializer()
        resultado = serializador.dump(usuarioEncontrado)    

        return {
            'content' : resultado
        }
    
    @jwt_required()
    def put(self):
        identificador = get_jwt_identity()
        usuarioEncontrado = conexion.session.query(UsuarioModel).where(UsuarioModel.id == identificador).first()
        data = request.get_json()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario no se encuentra en la base de datos'
            }, 400
        
        try:
            serializador = ActualizarUsuarioSerializer()
            dataValidada = serializador.load(data)

            #Si queremos actualizar un campo o varios campos con modificalos en la instancia y luego guardarlo en la BD
            usuarioEncontrado.nombre = dataValidada.get('nombre')
            
            conexion.session.commit()
            serializadorUsuario = RegistroSerializer()
            resultado = serializadorUsuario.dump(usuarioEncontrado)
            print(resultado)
            return {
                'message': 'Usuario actualizado exitosamente',
                'content' : resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error al actualizar el usuario',
                'content' : error.args
            }
    
class CambiarPasswordController(Resource):
    @jwt_required()
    def put(self):
        data = request.get_json()
        identificador = get_jwt_identity()
        serializador = CambiarPasswordSerializer()

        try:
            dataValidada = serializador.load(data)
            usuarioEncontrado = conexion.session.query(UsuarioModel).where(UsuarioModel.id == identificador).first()
            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }
        #Validar si la contraseña antigua es la correcta del usuario, si noes retornar el mensaje Password antiguo invalida
            passworAntigua = bytes(dataValidada.get('passwordAntigua'),'utf-8')
            #Aqui realiza la comparacion del password de las BD con lo dado en el body
            validarPassword = checkpw(passworAntigua, bytes(usuarioEncontrado.password, 'utf-8'))

            if validarPassword == False:
                return {
                    'message': 'La contraseña antigua es invalidad'
                }, 400
            
            #Si es el password entonces actualizar la contraseña pero hacer el hash de la misma y luego actualizarla
            nuevaPassword = bytes(dataValidada.get('passwordNueva'),'utf-8')
            salt = gensalt()

            nuevaPasswordHash = hashpw(nuevaPassword, salt).decode('utf-8')

            #Si se logra, actualiza el password retornar mensaje exito
            usuarioEncontrado.password =  nuevaPasswordHash            
            conexion.session.commit()
    
            return {
                'message': 'Password actualizada correctamente'
            }
        

        except ValidationError as error:
            return {
                'message': 'Error al cambiar la contraseña',
                'content' : error.args
            }, 400

class ResetearPasswordController(Resource):
    def post(self):
        data = request.get_json()
        serializador = ResetearPasswordSerializer() 
        try:
            dataSerializada = serializador.load(data)
            usuarioEncontrado=conexion.session.query(UsuarioModel).where(UsuarioModel.correo == dataSerializada.get('correo')).first()
           
            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe en la base de datos'
                }, 400
                
            textoCorreo = """
Hola {},
Has solicitado el cambio de la contraseña de tu cuenta en Tienditapp, si no has sido tu omite este mensaje.

Gracias,

Atentamente.

El equipo mas chevere de todos
"""
            htmlCorreo = """
<html>
    <body>
        <p>Hola <b>{}</b>, <br>
            Has solicitado el cambio de la contraseña de tu cuenta en <b>Tienditapp</b>, si no has sido tu omite este mensaje.<br><br>
            Gracias,<br><br>
            Atentamente.<br><br>
            El equipo mas chevere de todos
        </p>
    </body>
</html>
"""
            enviarCorreo(usuarioEncontrado.correo, 'Has solicitado el cambio de tu contraseña', textoCorreo, htmlCorreo)
            return {
                  'message': 'Reset completado existosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al resetear el password',
                'content' : error.args
            }, 400




