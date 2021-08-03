import random
#while
num = int(input("Ingrese un numero: "))
enc = random.randint(1,100)
while num != enc:
    if num > enc:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    num = int(input("Ingrese un numero: "))
print("Felicidades, lo haz encontrado")

#contar pares e impares mientras sean diferentes de 0
num = int(input("Ingrese un numero o 0 para terminar: "))
pares = 0
impares = 0
while num != 0:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input("Ingrese un numero o 0 para terminar: "))
print("total de pares: ", pares)
print("total de impares: ", impares)

i = 0
while i <= 10:
    j = 0
    aux = ""
    while j <= i:
        aux = aux + "*"
        j += 1
    print(aux)
    i += 1

suma = 0
num = 0
while suma <= 30:
    suma += num
    num += 1
    print("El numero es: ",num)
    if num > 6: break
print("la suma es ",suma)

#for
for i in [8,3,7,2,0,8,2,0,2,1]:
    print(i, end=" ")
print(" ")
for i in range(10):
    print(i*10, end=" ")
print(" ")
for i in "Universiad":
    print (i)
print(" ")
for i in range(0,10,2):
    print(i)

import numpy as np
for i in np.arange(0,1,0.1):
    print(i)

animales = ['gato','perro','zorro']
for animal in animales:
    print("el animal es: ",animal) 