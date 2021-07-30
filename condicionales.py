num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1 > num2:
    print("el numero mayor es: ",num1)
else:
    print("el numero mayor es: ",num2)

a = 3
b = 2
c = 5
if a > b:
    if a > c:
        print("Mayor: ",a)
    else:
        print("mayor: ",c)
elif b > c:
    print("Mayor ",b)
else:
    print("Mayor",c)

