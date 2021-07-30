#función print
print("Programación avanzada")
print("Programación avanzada\nUniversidad Libre")
print("Universidad Libre", "Fredys Simanca: ","")
print("Universidad Libre -->", end="-->")
print("Programación Avanzada")
print("Universidad", "Libre", "Programación", "Avanzada", sep="-", end=" ")
print("Programación avanzada")

#Operaciones básicas
#potencia
print(2**3)
print(2**3.0)
print(2.0**3)
print(2.0**3.0)
print(2**2**3)

#producto
print(2*3)
print(2*3.0)
print(2.0*3)
print(2.0*3.0)

#Division entera
print(10//3)
print(10//3.0)
print(10.0//3)
print(10.0//3.0)

#Division exacta
print(10/3)
print(10/3.0)
print(10.0/3)
print(10.0/3.0)

#Modulo
print(10%3)
print(10%3.0)
print(10.0%3)
print(10.0%3.0)

#suma
print(10+3)
print(10+3.0)
print(10.0+3)
print(10.0+3.0)

#resta
print(10-3)
print(10-3.0)
print(10.0-3)
print(10.0-3.0)

#variables
asignatura = "Programación Avanzada"
codigo = 6029
activo = True

print("Espacio: ", asignatura, codigo, activo)

num1 = 10
num2 = 4
resultado = num1 + num2
print("Suma = ",resultado)
print("resta= ",num1-num2)
resultado = num1 / num2
print("division= ",resultado)

curso = "Programación Avanzada"
profesor = "Freddy Simanca"
final = "Este es el curso de "+ curso + " por "+profesor
print(final)

final = "Este es el curso de %s por %s" %(curso, profesor)
print(final)

final = "Este es el curso de {} por {}".format(curso, profesor)
print(final)

#ingreso de variables
num3 = int(input("Ingrese un numero: "))
result = num2 * num3
print(result)

#Comparadores
a = 10
b = 15
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)

