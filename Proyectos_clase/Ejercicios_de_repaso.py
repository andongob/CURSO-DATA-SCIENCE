# # -*- coding: utf-8 -*-
# """
# Created on Mon Oct 21 09:00:53 2024

# @author: rportatil112
# """

# 1. Cálculo de área y perímetro de un rectángulo
# Crea una función que pida al usuario ingresar el ancho y la altura de un rectángulo, y que luego calcule y muestre su área y perímetro.

def ejercicio_1():
    base = float(input("Introduzca la base: "))
    altura = float(input("Introduzca la altura: "))
    
    area = base * altura
    perimetro = 2 * (base + altura)  # Fórmula correcta para el perímetro de un rectángulo
    
    return area, perimetro  # Devuelve ambos valores

area, perimetro = ejercicio_1()
print(f"El área es {area} y el perímetro es {perimetro}")


# 2. Promedio de una lista de números
# Escribe una función que tome una lista de números como parámetro y retorne el promedio de los números. #
# Incluye la validación para que solo acepte listas que contengan al menos un número.

lista = [1, 2, 3, 4, 5]

def promedio1():
    return(sum(lista))

def promedio2():
    return(len(lista))

def ejercicio_2():
    a = promedio1()
    b = promedio2()
    return(a / b)

print(f"El promedio de la lista es {ejercicio_2()}")

# 3. Contar ocurrencias de una palabra
# Escribe un programa que solicite al usuario ingresar una frase y una palabra,
# y luego cuente cuántas veces aparece la palabra en la frase, sin importar las mayúsculas o minúsculas.

def ejercicio_3():
    frase = str(input("Introduce una frase: "))
    palabra = str(input("Introduce una palabra: "))
    if palabra in frase:
        contador = frase.count(palabra)
        print(f"{palabra} aparece en la frase {contador} veces")
    else:
        print(f"{palabra} no aparece en la frase" )

ejercicio_3()


# 4. Intercambiar valores de una tupla
# Crea una función que reciba una tupla de dos elementos y retorne una nueva tupla con los valores intercambiados. 

tupla = ("Bilbao", "Bizkaia")

def desempaquetado():
    a, b = tupla #desempaquetado
    return(b, a)

def ejercicio_4():
    tupla_invertida = (desempaquetado())
    return(tupla_invertida)

ejercicio_4()
    

# 5. Divisores de un número
# Crea un programa que solicite al usuario ingresar un número entero positivo y que luego imprima todos sus divisores.



def ejercicio_5():
    entero = int(input("Introduzca un número entero positivo: "))
    lista = [] #aquí se van a mostrar los divisores

    for i in lista:
        divide = entero % 2
        return(divide)
        lista.append()
        
ejercicio_5()        


def ejercicio_5():
    entero = int(input("Introduzca un número entero positivo: "))
    divisores = []
    
    for i in range(1, entero + 1):  # Incluimos 1 y el número en sí como divisores
        if entero % i == 0:  # Si el resto es 0, es divisor
            divisores.append(i)
    
    print(f"Los divisores de {entero} son: {divisores}")

# Ejemplo de uso:
ejercicio_5()


# 6. Filtrar números pares de una lista
# Escribe una función que reciba una lista de números y devuelva una nueva lista que contenga solo los números pares. 
# Usa un bucle for y operadores condicionales.

def ejercicio_6(num):
    lista = [1, 2, 3, 4, 5]
    lista_pares = []
    for i in lista:
        if num // 2 :
            lista_pares.append()
    return(lista_pares)

ejercicio_6(4)

# 7. Manejo de excepciones en una calculadora
# Crea una calculadora que permita sumar, restar, multiplicar y dividir dos números ingresados por el usuario. Asegúrate de manejar excepciones como la división por cero utilizando un bloque try-except.
# 8. Suma de valores de un diccionario
# Escribe un programa que tome un diccionario cuyos valores sean números y calcule la suma de todos los valores.

dicc =  {"num1" : 1, "num2" : 3, "num3" : 5, "num4" : 7, "num5" : 9, }

def ejercicio_8():
    suma_total = 0 #vamos a necesitar una referencia desde donde empezar
    for i in dicc.values():
        suma_total += i #tengo que recordar que += asigna valores a la iteración
    return(suma_total)
    print(suma_total)

ejercicio_8()




# 9. Lectura y escritura en archivos
# Crea un programa que lea el contenido de un archivo de texto llamado datos.txt y 
#luego escriba una nueva versión del archivo donde cada línea está numerada. Utiliza el bloque with para gestionar los archivos.

with open (r"datos.txt", "r", encoding="latin1") as datos_origen: #leemos el archivo origen que queremos enúmerar
    with open(r"datos_new.txt", "w", encoding="latin1") as ejercicio_9: #creamos la nueva versión 
        for indice, linea in enumerate(datos_origen): #desempaquetamos en dos variables
            print(f"{indice}-{linea}") #mostramos el resultado en pantalla
            ejercicio_9.write(f"{indice}-{linea}") #escribimos el print en el archivo creado
            
   

# 10. Generador de números pares
# Escribe una función generadora que devuelva números pares entre 0 y un valor n proporcionado por el usuario. Luego, imprime todos los números generados.

def ejercicio_10():
    valor = input("Introduzca un número mayor a 0: ")
    if valor < 0 :
        print ("El valor no es igual o mayor a 0, vuelva a intentarlo")
    elif valor != int():
        print ("El valor no es un número entero")
    for i in valor:
        par = i % 2 
        print(par)
        
ejercicio_10()
