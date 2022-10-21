# EJERCICIO LISTAS

# Metodos propios

lista = [45, 32, 3, 78]
print("lista original : ", lista)
# funcion append: añada un elemento a la lista
lista.append(955)
lista.append(7)
print("lista despues de usar append: ", lista)
# Funciona sort: ordena la lista
lista.sort()
print("lista ordenada: ", lista)
# Funcion reverse: invierte el orden de la lista
lista.reverse()
print("lista al reves: ", lista)
# Funcion extend: añade los elementos de una lista a la lista
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend: ", lista)
# Funcion count: cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista 
print("Nuemros de elementos 45: ", lista.count(45))
# Funcion insert: añade el elemento pasado como parametro a la lista en la posicion indicada tambien por parametro
lista.insert(4,111)
print("Lista despues de extend: ", lista)
# Funcion remove: elimina la primera ocurrencia empezando por la izquierda de lista del elemento indicado como parametro.
lista.remove(45)
print("Lista despues de remove: ", lista)
# Funcion index:devuelve la posicion de la primera ocurrencia de izquierda a derecha en la lista, del elemento pasado como parametro
print("Posicion del elemento 111: ", lista.index(111))
# Funcion pop: elimina el ultimo elemento de la lista y lo devuelve como resultado de la operacion.
lista.pop()
print("Lista despues de pop:", lista)
# Funcion clear: elimina todos elementos de la lista
lista.clear()
print("LIsta despues de clear: ", lista)




