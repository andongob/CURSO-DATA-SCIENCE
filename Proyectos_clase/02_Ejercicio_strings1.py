# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:08:16 2024

@author: rportatil112
"""
%reset -f

# Ejercicio 1: Tipos de datos
# Define una variable de cada tipo de dato primitivo: un entero, un flotante, una cadena de texto y un booleano.
# Imprime el valor y el tipo de cada variable utilizando la función type().


nombre = "Ana Verónica"
nombre_corto = 'Ana'
apellido1 = 'Ndongo'
apellido2 = 'Bindang'
edad = 50
residencia = 'Bilbao'
peso = 74.5
tiene_canas = True

type(nombre)
type(edad)
type(residencia)
type(peso)

print('nombre (str):',nombre)
print('edad (int):',edad)
print('residencia (str):',residencia)
print('nombre (float):',peso)

# Ejercicio 2: Operaciones matemáticas
# Define dos números enteros e imprime el resultado de las siguientes operaciones: 
    suma, resta, multiplicación, división, división entera, exponente, y módulo.

suma = 20 + 30
print(suma)
resta = 30 - 20
print(resta)
multiplicación = 9 * 3
print(multiplicación)
división = 9 / 3
print(división)
division_entera = 9 // 3
print("División entera:", division_entera)
exponente = 2 ** 3
print(exponente)
modulo = 9 % 2 #muestra el resto de la división
print("Módulo:", modulo)



# Ejercicio 3: Operadores comparativos y lógicos
# Define dos variables x = 10 y y = 20.
# Compara x y y usando los operadores: ==, !=, >, <, >=, <=.
# Usa los operadores lógicos and, or y not.

x = 10 
y = 20

z = True
q = False

x == y
x != y
x > y
x < y
x >= y
x =< 
print("not z and q:", not z and q)
print(z or q)

# Ejercicio 4: Conversión de tipos
# Solicita al usuario su edad con input(), conviértelo en entero, y multiplica la edad por 2.

edad = input("Introduce tu edad: ")
print(edad * 3) # al estar en formato texto lo que hace es incrementar

edad = int(edad)
print(edad * 2) # aquí multiplica


# Ejercicio 5: Cadenas de texto
# Define una cadena con tu nombre completo.
# Concatenar tu nombre y tu apellido usando + y luego con f-strings.
# Imprime la primera letra de tu nombre, la última letra de tu apellido, y la longitud total de la cadena completa.
# Convierte tu nombre a mayúsculas y elimina espacios adicionales al principio o final.

nombre_completo = 'Ana Verónica Ndongo Bindang'
nombreCorto_apellido = nombre_corto + " " + apellido1
fnombreCorto_apellido = f'{nombre} {apellido1} {apellido2}'
print('fnombreCorto_apellido')
nombre[0]
apellido2[-1]
len(fnombreCorto_apellido)
fnombreCorto_apellidomays = fnombreCorto_apellido.upper()
fnombreCorto_apellidomins = fnombreCorto_apellido.lower()


# Ejercicio 6: Formateo de cadenas y números
# Define una variable pi = 3.14159 y muestra el valor con 2 decimales.
# Alinea el valor de pi a la derecha en un espacio de 10 caracteres, con 3 decimales.

pi = 3.14159

# Ejercicio 7: Comentarios
# Escribe un código que sume dos números y comenta cada línea.

nPar = 8
nImpar = 7
sumaParImpar = nPar + nImpar





# Ejercicio 8: Ejercicio práctico final
# Solicita al usuario su nombre y edad.
# Crea una frase usando f-strings: "Hola, me llamo [nombre] y tengo [edad] años."
# Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". Si es menor, imprime "Eres menor de edad".
# Convierte el nombre a mayúsculas y cuenta cuántas veces aparece la letra "a" en el nombre.

