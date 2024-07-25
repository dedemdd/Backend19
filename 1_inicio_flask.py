from flask import Flask, request
from psycopg import connect


conexion =connect(conninfo = 'postgresql://postgres:Alberto123@localhost:5432/bd_flask')

app = Flask(__name__)

@app.route('/')
def manejar_ruta_inicio():
    return 'Bienvenido a mi API de Flask!'

@app.route('/registrar-usuario', methods=['POST'])
def manejar_registro_usuario():
    print(request.get_json()) #Convierte el json a un diccionario
    data = request.get_json() 
    cursor = conexion.cursor() #PODEMOS INTERACTUAR CON LA BASE DE DATOS(ESCRIBIR Y LEER INFORMACION DE LA BASE DE DATOS)
    cursor.execute("INSERT INTO usuarios (nombre, apellido, correo) VALUES(%s, %s, %s)",(data['nombre'],data['apellido'],data['correo']))

    conexion.commit()
    cursor.close() #CERRAMOS LA INTERACCION CON LA TABAL PARA EVITAR BLOQUES INNECESARIOS

    return {
        'message': 'Usuario registrado exitosamente'
    }


@app.route('/listar-usuarios', methods=['GET'])
def devolver_usuarios():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    #fetchall > retorna todos los registro leidos
    #fetchone() > retorna el primer registro
    #fetchmany(NUM_REGISTROS) > cuantos registros quieres leer
    usuarios = cursor.fetchall() 
    print(usuarios)
    #convertir la información de los usuarios a un diccionario
    #[(1, 'Denys','Jaramillo','denysjaramillo30@gmail.com')]
    #[
    #    {'id': 1, 
    #     'nombre': 'Denys', 
    #     'apellido': 'Jaramillo', 
    #     'correo': 'denysjaramillo30@gmail.com'
    #}
    #]
    resultado = []
    for usuario in usuarios:
        usuario_dic = {
            'id': usuario[0],
            'nombre': usuario[1],
            'apellido': usuario[2],
            'correo': usuario[3]
        }

        resultado.append(usuario_dic)
    return {
        'content': resultado
    }


if __name__ == '__main__':
    #estamos en el archivo principal

    #levanta mi servidor de flask
    #Si configuramos el parametro en TRUE, cada vez que hagamos algun cambio y guardamos se reiniciará el servidor
    app.run(debug=True)