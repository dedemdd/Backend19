from flask import Flask
from instancias import conexion
from dotenv import load_dotenv
from os import environ
from models import *
from flask_migrate import Migrate
from Controllers import *
#API > Aplication Program Interface
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS

#busca el archivo .env y cargara las variables como si fueran variables de entorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=10, seconds=5)


#Origin > desde que dominios pueden consultar mi API
#headers = que cabeceras pueden enviarme el cliente a mi API
#http methods los metodos permitidos que pueden consultar a mi API
CORS(app, origins='*', allow_headers='*',
     methods=['GET', 'POST','PUT', 'DELETE'])
    
#Esta linea crea una nueva sesion en la base de datos
#El JWTManager utiliz la aplicacion de Flask para leer las variables JWT_SECRET_KEY que esta en la firma para la generacion de token
JWTManager(app)

#Definimos la API de nuestra aplicacion de Flask
api = Api(app)
print(environ.get("DATABASE_URL"))


#Ahora aca le paso la configuración de flask a SQLAlchemy
conexion.init_app(app)

Migrate(app, conexion)

#Agregamos los recursos (controladores)
api.add_resource(CategoriasController, '/categorias')
api.add_resource(CategoriaController, '/categoria/<int:id>')
api.add_resource(ProductosController, '/productos')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(PerfilController, '/perfil')
api.add_resource(CambiarPasswordController, '/cambiar-password')
api.add_resource(ResetearPasswordController, '/reset-password')
api.add_resource(ConfirmarResetTokenController, '/validar-token')


if __name__ == '__main__':
    app.run(debug=True)


