lista = ["python", 8, 4.5, True]
print(lista)

#agregar un elemento al final
lista.append(20)
print(lista)

#insertar un elemento
lista.insert(1,"profesor")
print(lista)

# eliminar ultimo elemento
lista.pop()
print(lista)

#ordenar
edades = [20,19,35,40,60,32,10]
edades.sort()
print(edades)
edades.sort(reverse = True)
print(edades)

#insertar lista dentro de otra
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10]
list1.append(list2)
edades.sort()
print(list1)

#eliminar 
lista.remove(8)
print(lista)

#valor
print(lista.index('profesor'))

#limpiar
list2.clear()
print(list2)

#contar veces valor
valores = [1,2,3,4,5,6,10,25,10,30,25,60,4,6]
print(valores.count(6))

#concatenar
nombres = ['Diego','Alex','Camilo']
apellidos = ['Sandoval','Deimon','Duran']
concat = nombres + apellidos
print(concat)

#String como lista
curso = "Programación \"avanzada\" en python"
print(curso)
print(curso[13:23])
print(curso.find('en'))
print(curso.count('p'))
print(curso.upper())
print(curso.title())
print(curso.lower())
print(curso.replace('a','A'))
new_curso = curso.split(' ')
print(new_curso)