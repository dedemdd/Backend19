from flask import Flask
from instancias import conexion
from dotenv import load_dotenv
from os import environ
from models import *
from flask_migrate import Migrate
from Controllers import *
#API > Aplication Program Interface
from flask_restful import Api
#busca el archivo .env y cargara las variables como si fueran variables de entorno
load_dotenv()

app = Flask(__name__)

#Definimos la API de nuestra aplicacion de Flask
api = Api(app)
print(environ.get("DATABASE_URL"))
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

#Ahora aca le paso la configuración de flask a SQLAlchemy
conexion.init_app(app)

Migrate(app, conexion)

#Agregamos los recursos (controladores)
api.add_resource(CategoriasController, '/categorias')
api.add_resource(CategoriaController, '/categoria/<int:id>')
api.add_resource(ProductosController, '/productos')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')


if __name__ == '__main__':
    app.run(debug=True)


