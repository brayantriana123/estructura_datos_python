# EJERCICIOS DICCIONARIOS

# METODOS PROPIOS

diassemanaingles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday",
                    "Miércoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}
                    
print("DICCIONARIO ORIGINAL: " , diassemanaingles)

# Función Copy: Realiza una copia exacta del diccionario en uno nuevo. 
diccionariocopia = diassemanaingles.copy()
print("--------Copy--------")
print("DICCIONARIO COPIA: " , diccionariocopia)

# Función Pop: Obtiene el valor de la clave pasada como parámetro y además elimina el elemento del diccionario.
print("--------Pop--------")
print("Valor del Lunes (Pop): " , diassemanaingles.pop("Lunes"))
print("Diccionario después del pop: " , diassemanaingles)

# Función Popitem: Obtiene un elemento aleatorio del diccionario y lo elimina del mismo.    
print("--------Popitem--------")
print("Elemento al azar con  popitem: " , diassemanaingles.popitem())
print("Diccionarios después de Popitem: " , diassemanaingles)

# Función get: Obtiene el valor de la clave pasada como parámetro.
print("--------Get--------")
print("Valor del Martes (Get): " , diassemanaingles.get("Martes"))
print("Valor del Lunes (Get) ( no existe): " , diassemanaingles.get("Lunes"))
print("Valor del Lunes (Get) ( no existe): " , diassemanaingles.get("Lunes" , "No existe"))

# Función Update: Actualiza el diccionario utilizando otro diccionario. 
print("--------Update--------")
diassemanaingles.update({"Lunes": "MondayNUEVO", "Martes": "TuesdayNUEVO"})
print("Diccionario después del update: " , diassemanaingles)

# Función Setdefault: Intena insetar un elemento (clave y valor) en el diccionario. En caso de no  existir dicho elemento. la función inserta y devuelve el valor del elemento y en caso de existir, lo único que hace es devolver el valor actual.
print("--------Setdefault--------")
print("Setdefault: " , diassemanaingles.setdefault("Sabado" , "Saturday"))
print("Diccionario después del setdefault (Nuevo Elemento): " , diassemanaingles)
print("Setdefault del Lunes: " , diassemanaingles.setdefault("Lunes" , "Lunes"))
print("Diccionario después del setdefault (Elemento existente): " , diassemanaingles)


# Función Items: Devuelve un objeto iteravle (que puede utilizarse en bucles).
print("--------Items--------")
print("Elemento iterable (Items): " , diassemanaingles.items())

# Función Keys: Devuelve un objeto iteravle (que puede utilizarse en bucles) con las claves del diccionario.
print("--------Keys--------")
print("Elemento iterable (Claves): " , diassemanaingles.keys())

# Función Values: Devuelve un objeto iteravle (que puede utilizarse en bucles) con los valores del diccionario.
print("--------Values--------")
print("Elemento iterable (Valores): " , diassemanaingles.values())

# Función Clear: Elimina todos los elementos del diccionario.
print("--------Clear--------")
print("Diccionario antes del clear: " , diassemanaingles)
print("Diccionario después del clear: " , diassemanaingles.clear())