

numero = 10

#Declaramos una funcion (definimos su comportamiento)
def incrementat_en_uno():
    print(1)

#Para llamar una funcion se tiene que poner los parametros(que van entre parentesis)
incrementat_en_uno()


def calcular_promedio(numero1: int, numero2: int):
    resultado = (numero1 + numero2) / 2
    #la función devolverá un valor
    return resultado

calcular_promedio(10, 40)


#crear la función que pase un nombre y que se retorne el salud buenas noches y el nombre
def saludar(nombre):
    saludo = 'Buenas noches, {}'.format(nombre)
    return saludo

resultado = saludar('Denys')
print(resultado)

#Funciones que pueden recibir n parametros
def numeros(*args):
    #Los argumentos son almacenados en un tupla y esta no se puede editar
    #los args generalmente sirven para almacenar una cantidad ilimitada de valores
    print(args)

numeros(1, 2, 'a', 4, 5)



#kwargs key argumentos o argumentos con llaves
def informacion(**kwargs):
    #el parametro kwargs se guardara en un dict(diccionario) cuyo parametros serán llaves
    print(kwargs)

informacion(nombre='Denys', edad=28, ocupacion='Estudiante')


#Si queremos utilizar los args y los kwargs siempre primero para van los args
def combinada(*args, **kwargs):
    print(args) #tupla
    print(kwargs) #Diccionario

combinada(10, 40, True, 0, nombre='Denys', edad=28, ocupacion='Estudiante')

