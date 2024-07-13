#For
# bucle repetitivo que debe tener un final

for numero in range(0,10):
    print(numero)

print('----------')
for numero in range(5):
    print(numero)

print('----------')
for numero in range(1,10,2):
    print(numero)

#El for se usa mayormente cuando queremos iterar elementos de una lista o tupla
notas = [10, 15, 6, 13, 18, 20]

for nota in notas:
    #cada vuelta ingresará a una posicion de la lista
    print(nota)

#El bucle for sirve para iterar texto

texto = 'El dia de hoy fue un día muy frío ya que estamos en invierno'

for letra in texto:
    print(letra)



# Se tiene la siguiente informacion: 
notas = [15, 7, 12, 14, 20]

#Imprimir las notas aprobadas y las notas desaprobadas
#indicar cuantas notas son aprobadas y cuantas desaprobadas
#Sacar el promedio de las notas aprobadas y el promedio de las notas desaprobadas

aprobadas = []
desaprobadas = []

for nota in notas:
    if nota > 10:
        aprobadas.append(nota)        
        
    else:  
        desaprobadas.append(nota)

promedio_aprobadas = sum(aprobadas) / len(aprobadas)
numero_naprobadas = len(aprobadas)
promedio_desaprobadas = sum(desaprobadas) / len(desaprobadas)
numero_ndesaprobadas = len(desaprobadas)
print('Notas aprobadas:', aprobadas)
print ('Numero de notas aprobadas es ', numero_naprobadas)
print('Notas desaprobadas:', desaprobadas)
print ('Numero de notas desaprobadas es ', numero_ndesaprobadas)
print('Promedio de notas aprobadas:', promedio_aprobadas)
print('Promedio de notas desaprobadas:', promedio_desaprobadas)

        










