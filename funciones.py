def mensaje():
    print("Hola, soy una función")

def saludo(name):
    print("Hola",name)

def operacion(a, b, op):
    if op == 1:
        print("suma =", a + b)
    elif op == 2:
        print("resta =", a - b)
    elif op == 3:
        print("multiplicación =", a * b)
    elif op == 4:
        print("división =", a / b)

def subsidio(sueldo):
    if sueldo >= 960000*2:
        salario = sueldo + 100000
    else:
        salario = sueldo
    return salario

mensaje()
saludo('Diego')
operacion(8, 5, 3)

sueldo = int(input('Digite su sueldo: '))
x = subsidio(sueldo)
print('Total a pagar:',x)
