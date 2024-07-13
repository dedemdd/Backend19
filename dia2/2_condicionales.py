numero1 = 20
numero2 = 50
numero3 = 40

#condicionales se pueden dar con resultados boolean
if numero1 > numero2:
    print('El número 1 es mayor que el número 2')
#sino cumple la primera condicion trataremos con esta nueva y si no cumple 
elif numero1 > numero3:
    print('El número 1 es mayor al número 3')
else:
    print('El número 2 es mayor que el número 1')



# Si tengo el sueldo entre S/. 500 y S/. 800, entonces puede ir a la playa
#Si tengo el sueldo mas de S/ 800 puedo ir al Inti Raymi


def calcular_actividades_vacacionales(suedo: int):
    if suedo >= 500 and suedo <= 800:
        print('Puedes ir a la playa')
    elif suedo > 800:
        print('Puedes ir al Inti Raymi')
    
#print('Ingrese su sueldo')
#sueldo = float(input())
#if sueldo >= 500 and sueldo <= 800:
#    print('Puedes ir a la playa')
#elif sueldo > 800:
#    print ('Puedes ir al Inti Raymi')

sueldo = 600
calcular_actividades_vacacionales(sueldo)

sueldo = 805
calcular_actividades_vacacionales(sueldo)


#Queremos saber si un alumno esta reprobado o necesita ir a vacacional o esta reprabado
# las condiciones son: si tiene 13 y 18 esta aprobado, si tiene 19 y 2 esta aprobado, si tiene 20 y 3 esta aprob con felicitaciones, si tiene entre 10 y 12 necesita ir a vacacional y si tiene menos de 11 entonces esta reprobado convierta esto en una funcion en la cual se pase la nota y el nombre del estudiante

def evaluar_estudiante(nombre: str, nota: int):
    if nota >= 13 and nota <= 18:
        print(f'{nombre} esta aprobado')
    elif nota >= 19 and nota <= 20:
        print(f'{nombre} esta aprobado con felicitaciones')
    elif nota >= 10 and  nota <= 12:
        print(f'{nombre} necesita ir a vacacional')
    elif nota < 11:
        print(f'{nombre} esta reprado')


evaluar_estudiante('Denys', 19)

def calcular_resultado_nota(nota, nombre):

    if nota < 0:
        print('La nota debe ser un número entero positivo')
    elif nota <= 10:
        print('El alumno {} esta reprobado'.format(nombre))
    elif nota <= 12:
        print('El alumno {} ira a vacacional'.format(nombre))
    elif nota <= 18:
        print('El alumno {} esta aprobado'.format(nombre))
    elif nota <= 20:
        print('El alumno {} esta aprobado con felicitaciones'.format(nombre))
    else:
        print('El alumno {} se va a la nasa con Wisin y Yandel'.format(nombre))


calcular_resultado_nota(-1, 'Eduardo')

