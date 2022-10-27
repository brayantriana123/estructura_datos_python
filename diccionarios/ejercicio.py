# EJERCICIOS DICCIONARIOS

# EJERCICIOS MANIPULACIÓN

# 1. Consite en la definicion de un diccionario y cómo acceder a sus elementos.

print("------Ejercicio 1------")
diassemanaingles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday",
                    "Miércoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}

print(diassemanaingles["Lunes"])
print(diassemanaingles["Miércoles"])
print(diassemanaingles["Viernes"])


# 2. Consiste en añadir elementos al diccionario, eliminar elementos del diccionario y modificar elvalor de los elementos  del diccionario

# Para añadir elementos al diccionario es  de la siguiente forma:
# diccionario["Nuevaclave"] = "Nuevovalor"

# Para modifcar el valor de un elemento del diccionario es de la siguiente forma:
#diccionario["ClaveQueSeVaAModificar"] = "Nuevovalor"

# Para eliminar un elemento del diccionario es de la siguiente forma:
# del diccionario["ClaveQueSeVaAEliminar"]


# Ejemplo:

print("------Ejercicio 2------")
diassemanaingles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday",
                    "Miércoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}

print(diassemanaingles)
diassemanaingles["Sábado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)


# 3. Uso de la funcion len() para conocer el número de elementos que componen el diccionario, uso de la funcion max() para conocer el elemento con el valor máximo y uso de la funcion min() para conocer el elemento con el valor mínimo.

print("------Ejercicio 3------")
diassemanaingles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday",
                    "Miércoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}

print("NÚMERO DE ELEMENTOS DEL DICCIONARIO: " , len(diassemanaingles))
print("ELEMENTO CON VALOR MÁXIMO: " , max(diassemanaingles))
print("ELEMENTO CON VALOR MÍNIMO: " , min(diassemanaingles))