# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:41:44 2024

@author: rportatil112
"""

# Ejercicio 1: Función para verificar si una lista está ordenada
# Objetivo: Escribe una función que reciba una lista de números y determine si la lista está ordenada de menor a mayor.
# Descripción:
# La función debe recibir una lista de números y devolver True si los números están en orden ascendente, y False en caso contrario. 
# Si la lista tiene solo un elemento o está vacía, se considera que está ordenada. No puedes usar la función sorted() ni ninguna función de Python que ordene listas directamente.
# Instrucciones:
# Utiliza un bucle for para recorrer la lista.
# En cada iteración del bucle, compara si el número actual es menor o igual al siguiente número.
# Si en algún momento encuentras un número mayor que el siguiente, la lista no está ordenada, por lo que deberías retornar False inmediatamente.
# lista = [1, 2, 3, 4, 5]
# print(verificar_orden(lista))  # Salida esperada: True

# lista2 = [3, 2, 1]
# print(verificar_orden(lista2))  # Salida esperada: False

lista = [1, 2, 3, 4, 5]
        
def list_order(lista):
    esta_ordenada = True #damos por hecho que la lista está ordenada
    
    for i in range(1, 5, 1): #el tercer número (step) puede obviarse para el valor 1 por que ese valor se presupone, a partir del 2 sí 
        posicion_1 = lista[i - 1] #esto comprueba el número anterior
        posicion_2 = lista[i] #esto comprueba la posición que está mirando
        
        if posicion_1 > posicion_2:
            esta_ordenada = False #si no coincide con la presunción de que está ordenada le doy la vuelta para romper el bucke
            break
        # aquí podemos poner la salida para imprimir la salida
        if esta_ordenada:
            print("Está ordenada")
        else:
            print("No está ordenada")


list_order(1)
print(list_order.__name__)
            
# Ejercicio 2: Función para calcular el precio final con impuestos y descuentos
# Objetivo: Escribe una función llamada calcular_precio_final que calcule el precio final de un producto aplicando un impuesto y un descuento opcional.
# Descripción:
# La función debe recibir los siguientes parámetros:
# precio (obligatorio): el precio base del producto.
# impuesto (nombrado, con valor por defecto del 21%): el porcentaje de impuestos que se aplicarán al precio base.
# descuento (nombrado, con valor por defecto de 0): un descuento opcional que se aplicará al precio después de añadir los impuestos. 


def impuesto(imp_valor, precio):
    precio >= 0
    return precio * imp_valor/100
    """
    Calcula el valor de impuesto a aplicar
    """        
impuesto(21, 45)



def calcular_precio_final("precio" >= 0, "Impuesto" = impuesto(imp_valor, precio) , "Descuento" = 0 ):
    print(input("Precio"))
    print(input("Impuesto"))
    print(input("Descuento"))
    return precio + impuesto
    
calcular_precio_final(45)
 
# Ejercicio 3: Sistema de evaluación de resultados
# Diseña un programa que simule un sistema de evaluación de resultados deportivos. El usuario deberá ingresar los resultados de varios partidos 
# en formato de goles de dos equipos (por ejemplo, 2-1, 3-3, etc.). El programa debe procesar cada resultado y determinar si fue una victoria, 
# derrota o empate. También debe identificar si se dieron condiciones especiales, como más de 3 goles en total o si algún equipo no marcó goles. 
# Al final, muestra un resumen con las estadísticas.


