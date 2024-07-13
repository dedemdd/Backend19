# todos los valores ingresados por teclados serán string
informacion =input('Por favor ingresa un numero:  ')

try:
    informacion_numeros = int(informacion)
    print(informacion_numeros +10)
    print(informacion)
except TypeError:
    #Solo cuando el error sea de tipo TypeError en
    print('Hubo un error!!')
except ZeroDivisionError:
    print('No se puede dividir entre ')
#except:
#    print('Hubo un error desconocido')
except Exception as e:
    print(type(e))
    print('Ocurrio un error')