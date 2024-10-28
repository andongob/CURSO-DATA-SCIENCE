#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:51:51 2023

@author: laptop
"""

#######################
# List comprehension  #
#######################
"""
La comprensión de listas en Python es una característica que permite construir listas 
de manera concisa y legible utilizando una sintaxis compacta. 

Permite crear una lista a partir de otra lista, una cadena, u otra secuencia de datos, 
aplicando una expresión a cada elemento de la secuencia. 

Esto se hace mediante una sintaxis que combina bucles for y condicionales de una manera 
más compacta que los enfoques tradicionales.

Por ejemplo, considera la siguiente comprensión de lista que genera una lista de los 
cuadrados de los números del 0 al 9:
"""
parabola = [x**2 for x in range(10)]
"""
Aquí, x**2 es la expresión que se aplica a cada elemento x en el rango de 0 a 9. 
La comprensión de lista luego crea una lista con los resultados de estas expresiones.

Las comprensiones de lista pueden incluir también condiciones, lo que permite filtrar 
elementos según ciertas condiciones. Por ejemplo:
"""
parabola_pares = [x**2 for x in range(10) if x % 2 == 0]
"""
Esta comprensión de lista crea una lista de los cuadrados de los números del 0 al 9 que son pares.

La función que apliquemos a los elementos de la lista la podemos definir aparte:
"""

def divide2(num):
    print(f"Divido {num} entre 2")
    return num/2

lista_num = [divide2(elemento) for elemento in list(range(0, 300, 15))]
"""
Desordenamos la lista de manera aleatoria. Esta lista de números será nuestro 
"conejillo de indias" para ver el funcionamiento de map y filter
"""
import random
random.shuffle(lista_num)

########
# Map  #
########
"""
`map` aplica una función cualquiera a un iterable de manera que se ejecuta elemento a elemento.

Por ejemplo, si creamos la función `duplica` que recibe un número y lo devuelve multiplicado por 2
"""
def duplica(numero):
    return 2 * numero

# Podemos hacer pasar por la función a todos los elementos de lista_num
generador = map(duplica, lista_num)

# map no se ejecuta inmediatamente sino que crea una función generadora
# que en cada petición "next" evalúa la función para un elemento del iterable.

# El uso de map equivale a esto:
"""
def mapeador(lista_cualquiera):
    for elemento in lista_cualquiera:
        yield duplica(elemento)

generador = mapeador(lista_num)     
"""

next(generador)
next(generador)
next(generador)

# Otro ejemplo, con una función que devuelve texto
def imprime(numero):
    return f"Este término está ocupado por el elemento {numero}"


generador2 = map(imprime, lista_num)
next(generador2)
next(generador2)
next(generador2)

# Puedo ejecutar la función en todos los elementos si creo una 
# lista para los resultados
lista_desde_generador = list(generador2)

lista_num2 = list(map(duplica, lista_num))

###########
# Filter  #
###########
"""
La sintaxis de `filter`, es como la de `map` , pero usando una función que devuelve `True` o `False`.

El resultado es una selección de los elementos que devuelven `True` al ser pasados por la función.
"""

def tiene_decimales(num):
    if num == int(num):
        return False
    else:
        return True

iterable_num_decimales = filter(tiene_decimales, lista_num)
next(iterable_num_decimales)

# Ejecutamos el filtrado de una sola vez
lista_num_decimales = list(iterable_num_decimales)
# Incluso podemos crear el generador en el momento de crear la lista
lista_num_decimales = list(filter(tiene_decimales, lista_num))


###########
# Lambda  #
###########
"""
Son funciones que pueden utilizar cualquier número de parámetros pero una única expresión. 
Esta expresión es evaluada y devuelta. 
Se pueden usar en cualquier lugar en el que una función sea requerida. 
"""
def doble(num):
    return num*2

# Lambda por reducción de una función sencilla
iterable2 = map(lambda num: num * 2, lista_num)

next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)

# Lambda con múltiples parámetros
iterable3 = map(lambda x, y: x + y, lista_num, lista_num2)

lista_num3 = list(iterable3)

#___________#
# Ejercicio #
#-----------#
# Crear una lista con los números de 0 al 100.

lista_0_a_100 = [x for x in range(101)]
'''
He olvidado que se empieza en 0, por eso hay que poner 101 ya que el 0 contaría como 1 (primer valor)
'''
# Dividirlos entre tres con map y una función lambda.


dividir_lista = list(map(lambda  x: x / 3, lista_0_a_100)) 
'''
list: creo la lista
map: para que se aplique a todos los valores de la lista
lambda: para realizar una función simple que es recorrer los valores de la lista y dividirlos entre 3
'''

# Filtrar los que tienen parte decimal con una función lambda.

lista_filtrada_int = list(filter(lambda x: x % 3 == 0, lista_0_a_100))
'''
Había llegado hasta la función, pero no entendía no me salian los valores hasta que no he hecho == 0
me he apoyado en chatGPT para esto
'''

#__________#
# Solución #
#----------#


#___________#
# Ejercicio #
#-----------#
# Creamos una lista de edades que por error contiene números negativos y excesivos
import random
edades = [random.randint(-7, 130) for i in range(500)]
edades.count(-3)
edades.count(121)


# Usar filter para eliminar los valores



# Usar map para sustituirlos por 120 o 0








