from flask import Flask
from instancias import conexion
from dotenv import load_dotenv
from os import environ
from models import *
from flask_migrate import Migrate

#busca el archivo .env y cargara las variables como si fueran variables de entorno
load_dotenv()

app = Flask(__name__)
print(environ.get("DATABASE_URL"))
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

#Ahora aca le paso la configuración de flask a SQLAlchemy
conexion.init_app(app)

Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)




