# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:30:49 2024

@author: rportatil112
"""



#Crear una función que reciba dos números y devuelva el mayor de ellos.

        
def big_num(a, b):
    a = int(input("Introduce un número: "))
    b = int(input("Introduce otro número: "))
    if a > b:
        return a
    else:
        return b
                   
big_num(9,78)

#Crear una función que reciba dos parámetros y que compruebe si el primer número es divisible entre el segundo 
#(es decir, que al dividir el primero entre el segundo el resto sea cero).

def rest_num (a, b): #una manera de hacerlo
    if a % b == 0:
        return True
    else:
        return False
    
rest_num(8,3)

def rest_num2 (a, b): #otra manera de hacerlo más compacta
    return a % b == 0

rest_num2(9, 2)


#Calcular el área de un círculo

#A = 3,14 * r2

def area_o (r):
    return 3.14 * r**2

area_o(5)

#el mismo resultado de cálculo del área del círculo, utilizando el método math

import math 

def area_o_math (r):
    return math.pi * r**2

area_o_math(5)


#Calcular el área de un triángulo

#A = (base × altura) / 2


def area_3 (b, a):
    return b * a / 2

area_3(20,40)

#☻------otra forma----------------

def area_4():
    b = int(input("Introduce la base: "))
    a = int(input("Introduce la altura: "))
    return b * a / 2

# Llamada a la función
resultado = area_4()
print(f"El área del triángulo es: {resultado}")

#☻------una tercera forma----------------

def area_tri():
    base = float(input("Introduce base: "))
    altura = float(input("Introduce altura: "))
    area = base * altura/2
    return area

area_tri()


#Crear una función que reciba el radio de un círculo y devuelva el área y el perímetro.

import math

def calc_per (r):
    return math.pi * r**2 and 2 * math.pi * r  #calcula el área


calc_per(4)



from math import pi as PI #importante compilar todo

def calc_per(radio):
    area = PI * radio**2
    perimetro = 2 * PI * radio
    return area, perimetro


calc_per(4)

# # Ejemplo de uso
#radio = float(input("Introduce el radio: "))
# area, perimetro = calc_per(radio)


# Crea una función que pueda realizar operaciones básicas como suma, resta, multiplicación y división. 
# Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.
# Utiliza funciones separadas para cada operación.

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

print("Selecciona la operación:")
print("Elige 1 para Sumar")
print("Elige 2 para Restar")
print("Elige 3 para Multiplicar")
print("Elige 4 para Dividir")

while True:
    eleccion = input("Introduce la opción (1/2/3/4): ")

    if eleccion in ('1', '2', '3', '4'): #tratamos las elecciones como una lista y solicitamos el input con dos números para todas las operaciones
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if eleccion == '1':
            print(f"{num1} + {num2} = {suma(num1, num2)}")
        elif eleccion == '2':
            print(f"{num1} - {num2} = {resta(num1, num2)}")
        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
        elif eleccion == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Opción no válida") #nos aseguramos que se haga input de los valores que queremos sean el input

    siguiente = input("¿Quieres hacer otra operación? (sí/no): ")
    if siguiente.lower() != 'sí':
        break


# Utiliza funciones separadas para cada operación.


# def suma(tupla):
#     num1, num2 = tupla
#     return num1 + num2

# def resta(num1, num2):
#     return num1 - num2

# def multiplica(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     return num1 / num2

# def pide_opcion():
#     print(
#           1: Sumar
#           2: Restar
#           3: Multiplicar
#           4: Dividir
#           s: Salir     
#           )
#     opcion = input("Elige una opción: ")
#     return opcion

# def pide_numeros():
#     num1 = float(input("Introduzca el primer número: "))
#     num2 = float(input("Introduzca el segundo número: "))
#     return num1, num2

# def calculadora():
#     while True:
#         opcion = pide_opcion()
#         if opcion == "1":
#             return suma(pide_numeros())
#         elif opcion == "2":
#             return resta(*pide_numeros())
#         elif opcion == "3":
#             return multiplica(*pide_numeros())
#         elif opcion == "4":
#             return divide(*pide_numeros())
#         elif opcion == "s":
#             print("Adios")
#             break
#         else:
#             print("Opción inválida")

# calculadora()

#Condiciones de un nº primo:
# debe ser un número entero    
# Un número es primo si es mayor o igual a 2 
# y solo tiene dos divisores: 1 y el propio número.
# 
    
 #----------------------------------------   
    
def es_primo(num):
    if num < 2:  # Debe ser mayor o igual a 2; el 1 no se considera primo
        return False
    for i in range(2, num):  # Recorre el bucle entre el 2 y la variable num
        if num % i == 0: #si la división entre la valariable (num) y el valor iterado (i) es 0 significa que num tiene divisor por tanto no es primo
            return False
    return True

numero = int(input("Introduce un número: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


es_primo(numero)

#-----------------------------------------

