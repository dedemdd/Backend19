from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def manejar_ruta_inicio():
    return 'Bienvenido a mi API de Flask!'

@app.route('/registrar-usuario', methods=['POST'])
def manejar_registro_usuario():
    print(request.get_json()) #Convierte el json a un diccionario
    return {
        'message': 'Usuario registrado exitosamente'
    }

if __name__ == '__main__':
    #estamos en el archivo principal

    #levanta mi servidor de flask
    #Si configuramos el parametro en TRUE, cada vez que hagamos algun cambio y guardamos se reiniciará el servidor
    app.run(debug=True)