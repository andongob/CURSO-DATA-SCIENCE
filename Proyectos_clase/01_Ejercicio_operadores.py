# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:28:45 2024

@author: rportatil112
"""

# """Operaciones básicas
# 1. Sumar 22,8 y 35,3

22 + 8
35 + 3

# 2. Restar 25-10

20 -10

# 3. Multiplicar 3,14 por 5

3,14 * 5

# 4. Dividir 50 entre 4.
50 /4

# 5. Calcular de dos maneras la raíz cuadrada de 125."""

125**0.5
125**(1/2)


"""Creación de variables simples
1. Crear variables con las operaciones anteriores."""

suma1 = 22 + 8
b = 35 +3
c = 20 -10
d = 3,14 * 5
e = 50 / 4
f = 125**0.5
g = 125**(1/2)


"""Comprobación de la clase
1. Comprobar la clase de las variables creadas."""

type(suma1)
type(b)
type(c)
type(d)
type(e)
type(f)
type(g)


# """Creación de cadenas.
# 1. Crear tres cadenas: Nombre y apellidos, lugar de nacimiento y lugar de residencia.
# 2. Comprobar el tipo de dato cada una de las cadenas."""

nombre = 'Ana'
apellidos = 'Ndongo'
lugar_nacimiento = 'Sevilla'
lugar_residencia = 'Bilbao'

type(nombre)
type(apellidos)
type(lugar_nacimiento)
type(lugar_residencia)

# """Concatenación de cadenas.
# 1. Crear la frase “Me llamo ” “, nací en “ “ pero vivo en “ con vuestros datos
# concatenando frases.

frase1 = f"Mi nombre es {nombre}, vivo en {lugar_residencia}"
print(frase1)

# 2. Medir la longitud de la cadena creada."""

len(frase1)

# """Extracción elementos de la cadena
# 1. Extraer la ciudad en la que vivís.
lugar_residencia.find("Bi")
frase1[26:32]

# 2. Extraer vuestras iniciales."""

nombre[0:1]
apellidos[0:1]



# """Transformar en mayúsculas/minúsculas.
# 1. Poner todo con minúsculas."""
# 

frase1Min = frase1.lower()
print(frase1Min)


# """Comprobar si existen ciertos elementos.
# # 1. Comprobar si existe vuestro nombre.
frase2 = 'Mi nombre es Ana, vivo en Bilbao'
'Ana' in frase1

# 2. Comprobar el número de veces que aparece la letra “a”.

frase1.count("a") #es case-sensitive

# """Separar una cadena
# 1. Separar vuestra cadena por espacios."""

frase3 = 'Mi\tnombre\tes\tAna,\tvivo\ten\tBilbao'
print(frase3)


frase2sep = frase2.split("a",maxsplit=5)
print(frase2)

# """Transformar una cadena.
# 1. Poner vuestros datos en mayúsculas."""

frase2Max = frase2.upper()
print(frase2Max)

frase2 = frase2.replace("Ana","Ana Verónica")
print("frase2")

"""Creación de listas
1. Crear dos listas con los días de la semana y los días del mes del curso.
2. Analizar el tipo de dato del primer elemento de cada lista.
3. Concatenar las dos listas.
4. Crear una lista encadenando los elementos de la lista 1
5. Comprobar si existe el lunes y el día 18 en la lista concatenada.
6. Eliminar el viernes y su correspondiente día del mes.
7. Añadir el fin de semana y sus días del mes correspondientes en su lugar."""

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dias_octubre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

type(dias_octubre)
type(dias_semana)

listas = dias_semana + dias_octubre
print(listas)

lista_encadenada = [listas]
comprueba_lunes = "Lunes" in listas
print(comprueba_lunes)

lista_encadenada = [listas]
comprueba_dia = 18 in listas
print(comprueba_dia)

indice_viernes = listas.index("Viernes") #primero hay que encontrar el índice
print(indice_viernes)

del(listas[4])


    
    




