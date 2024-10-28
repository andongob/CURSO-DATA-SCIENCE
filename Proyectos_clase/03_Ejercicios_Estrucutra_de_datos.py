# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct  9 14:55:04 2024

# @author: rportatil112
# """

# Ejercicio 1: Listas
# Crea una lista con al menos 5 elementos de diferentes tipos (números, cadenas de texto, booleanos).
# Añade un nuevo elemento al final de la lista.
# Inserta un elemento en la segunda posición.
# Elimina el último elemento de la lista.
# Accede al tercer elemento de la lista.
# Clona la lista y modifica un elemento primitivo de la copia, verificando que al modificar la copia, la lista original no se ve afectada.
# Extra: Crea una lista de nombres y conviértela en una cadena de texto separando los nombres por comas.


lista0 = [ 1, 2, 'perro', 'gato', False]
lista0.append('delfin')
lista0.insert(1, 1.5)
elemento_eliminado = lista0.pop(6)
tercer_elemento = lista0[2]
print(tercer_elemento)
lista0_clon = lista0[:]
lista0_clon[3] = 'Orestes'
print('Lista Clonada', lista0_clon)
print('Lista Original', lista0)
lista0_nombre = ['Patricia', 'Julio', 'Ibone', 'Luma']
lista0_nombre = ", ".join(lista0_nombre) #importante aquí la comilla doble


# Ejercicio 2: Tuplas
# Crea una tupla con 5 elementos de cualquier tipo.
# Accede al primer y al último elemento de la tupla.
# Intenta modificar el segundo elemento y observa el resultado (explicar por qué no es posible).
# Desempaqueta los tres primeros elementos de la tupla en tres variables.
# Extra: Convierte la tupla en una lista, añade un nuevo elemento y vuelve a convertirla en tupla.

tupla0 = (1, 2, 'perro', 'gato', False)
tupla0_1º = tupla0[0]
tupla0_2º = tupla0[-1]
#no se puede modificar le valor de una tupla: no hay método (append?)
Lista0_Ele1, Lista0_Ele2, Lista0_Ele3 = tupla0[0:3]
tupla0_aLista1 = list(tupla0)
tupla0_aLista1.insert(-1, 'pájaro') #desplaza lo que hay al final de la lista 
tupla0_aLista1.append('pájaro') #inserta al final de la lista por eso no necesita posición
print(tupla0_aLista1)
tupla1 = tuple(tupla0_aLista1)

eliminar_tupla0_aLista1 = tupla0_aLista1.pop(5)

# Ejercicio 3: Diccionarios
# Crea un diccionario con tres pares clave-valor. Usa cadenas de texto como claves y valores de diferentes tipos.
# Añade una nueva clave-valor al diccionario.
# Modifica el valor de una clave existente.
# Elimina una clave del diccionario.
# Accede al valor de una clave usando .get() para evitar un error si la clave no existe.

Diccionario0 = {"nombre": "Luma", "edad": 10, "ciudad": "Bilbao"}
Diccionario0["profesión"] = "Feliciana"
Diccionario0["nombre"] = "Orestes"
Diccionario0["profesión"] = "Feliciano"

del Diccionario0["profesión"]
profesion_eliminada = Diccionario0.pop("profesión", "No especificada")  # Elimina y guarda el valor
del profesion_eliminada

profesion = Diccionario0.get("profesión", "No especificada") #campo1 = if, campo2=else



# Ejercicio 4: Conjuntos
# Crea un conjunto con al menos 5 elementos.
# Añade un nuevo elemento al conjunto.
# Intenta añadir un elemento duplicado y observa qué sucede.
# Elimina un elemento del conjunto.
# Crea otro conjunto con algunos elementos en común con el primer conjunto y realiza las siguientes operaciones:
# Unión: Devuelve todos los elementos que están en cualquiera de los dos conjuntos.
# Intersección: Devuelve solo los elementos que están en ambos conjuntos.
# Diferencia: Devuelve los elementos que están en el primer conjunto, pero no en el segundo.

conjunto0 = {1, 2, "perro", "gato", False, "Orestes"}
conjunto0.add("Luma")
conjunto0.discard("Luma")
print(conjunto0)
conjunto1 = { 2, 3, "perro", "pájaro", True, "Luma"}
union = conjunto0.union(conjunto1)
interseccion = conjunto0.intersection(conjunto1)
diferencia = conjunto0.difference(conjunto1)

# Extra: Diferencia simétrica: Devuelve los elementos que están en uno u otro conjunto, pero no en ambos (investigar cómo hacerlo).

diferencia_simetrica = conjunto0.symmetric_difference(conjunto1)


# Ejercicio 5: Filtrando con Listas y Conjuntos
# Dada una lista con elementos duplicados, conviértela en un conjunto para eliminar los duplicados.
# Ordena los elementos del conjunto y conviértelos de nuevo en una lista.

lista1 = [ 1, 2, 2, "perro", "perro", "gato", False]
lista_a_conjunto = set(lista1)





# Extras
# Ejercicio 6: Trabajando con Diccionarios Anidados
# Crea un diccionario que contenga información sobre un estudiante (nombre, edad, calificaciones en diferentes materias).
# Añade una nueva materia con su calificación al diccionario.
# Modifica la calificación de una materia existente.

Diccionario0 = {"nombre": "Pluto", "edad": 20, "Lengua": 7.5, "Matemáticas": 8.0, "Inglés": 7}
Diccionario0["Euskera"] = 8.5
Diccionario0["nombre"] = "Milú"

del Diccionario0["Euskera"]
print(Diccionario0)

# Ejercicio 7: Listas de Diccionarios
# Crea una lista de diccionarios donde cada diccionario represente un libro con las claves: título, autor y año de publicación (puedes llamarlo ‘libro1’, ‘libro2’, etc).
# Añade un nuevo libro a la lista.

diccionarioLibros = {"libro1": {
        "título": "El lobo estepario",
        "autor": "Herman Hesse",
        "año": 1927
    },
    "libro2": {
        "título": "Buenos días tristeza",
        "autor": "Francois Sagan",
        "año": 1954
    }
}

diccionarioLibros ["libro3"] = {
        "título": "Asterix y Obelix",
        "autor": "René Goscinny",
        "año": 1966
    }


# Ejercicio 8: Operaciones Complejas con Conjuntos
# Dada una lista de usuarios que han completado diferentes cursos, crea conjuntos para los usuarios que han completado cada curso.
# Encuentra los usuarios que han completado todos los cursos (intersección).
# Encuentra los usuarios que han completado al menos uno de los cursos (unión).
# Extra: ¿Te atreves?
# A continuación, te propongo dos ejercicios simples para practicar cómo recorrer los elementos de una lista y una matriz. Sé que aún no hemos visto estructuras repetitivas (bucles), pero puedes buscar en Google cómo iterar listas en Python.


curso1 = {"estudiante1", "estudiante2", "estudiante3", "estudiante4", "estudiante5"}
curso2 = {"estudiante6", "estudiante7", "estudiante8", "estudiante9"}
curso1 = {"estudiante2", "estudiante4", "estudiante6", "estudiante8", "estudiante7"}




# Recorrer una lista
# Dada una lista de 5 números, imprime cada uno de los elementos en una nueva línea.
# numeros = [10, 20, 30, 40, 50]

numeros = [10, 20, 30, 40, 50]
print(10)
print(20)
print(30)
print(40)
print(50)

print(numeros)


# Recorrer una matriz
# Dada una matriz (lista de listas) con 2 filas y 3 columnas, imprime cada uno de los elementos en una nueva línea.
# matriz = [ [1, 2, 3], [4, 5, 6] ]

matriz = [ [1, 2, 3], [4, 5, 6] ]
print(matriz)

lista_a = matriz[0]
lista_b = matriz[1]

matriz = [[1, 2, 3], [4, 5, 6]]



