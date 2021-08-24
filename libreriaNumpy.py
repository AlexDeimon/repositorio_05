import numpy as np

#Array de una dimencion
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)

#array de 2 dimenciones
b = np.array([(1,2,3,0),(4,5,6,1),(7,8,9,2)])
print(b)

#crear matrizes con 0
ceros = np.zeros((4,4))
print(ceros)

#crear matriz vacia
vacia = np.empty((5,5))
print(vacia)

#crear una matriz con valor fijo
full = np.full((5,5),2)
print(full)

#matriz identidad
identidad = np.eye(4,4)
print(identidad)

#crear arrray con valores espaciados unidormemente
espacio = np.arange(0,50,5)
print(espacio)
espacio1 = np.arange(start=100, stop=1, step=5)
print(espacio1)

espacio2 = np.linspace(2,10,5)
print(espacio2)

#imprimir las dimenciones de una matriz
print(b.ndim)

#el tipo de datos de la matriz
print(full.dtype)

#cambiar la forma de la matriz

m1 = np.array([(1,2,3),(4,5,6)])
print(m1)

m2 = m1.reshape(3,2)
print(m2)

#imprimir una columna de la matriz
print(m2[:0])

#imprimir una celda

print(b[1,1])

#el valor minimo
print(b.min())

#el valor maximo 
print(b.max)

#suma de los valores
print(b.sum())

notas = np.array([(4.5,3.5,2.0),(4.0,5.0,3.5),(4.5,3.5,2.0)])
print(notas)
print(np.std(notas))

#operaciones con matrices
x = np.array([(1,2,3),(4,5,6),(7,8,9)])
y = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(x + y)
print(x - y)
print(x * y)
print(x / y)

