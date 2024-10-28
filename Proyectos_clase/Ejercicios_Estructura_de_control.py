# # -*- coding: utf-8 -*-
# """
# Created on Fri Oct 11 09:54:24 2024

# @author: rportatil112
# """

# Ejercicios de Estructuras de Control
# Nivel Básico
# Condicional simple (if)
# Escribe un programa que pida al usuario un número e imprima si es mayor, menor o igual a 10.
# Condicional con elif y else
# Pide al usuario su edad e imprime si es un niño (menor de 12 años), un adolescente (entre 12 y 17 años) o un adulto (18 años o más).
# Bucle while simple
# Escribe un programa que solicite al usuario ingresar un número. El programa debe sumar todos los números que el usuario introduzca hasta que el usuario ingrese un número negativo. Luego, muestra el total.
# Bucle for simple
# Crea un programa que imprima los números del 1 al 10 usando un bucle for.

key = 7 #declaro la variable con el número que quiero adivinar
random_number = None #declaro una variable con la cual comparar el número que quiero adivinar

while random_number != key: #defino cual va a ser la base de la comparación "mientras random_number sea distinto a key, haz lo siguente"
    random_number = int(input("Introduce un número:")) #mostramos el texto para que el usuario meta el input del nº a adivinar

    if random_number < key: #aquí empieza la primera condición: si a < b
        print("El nº es demasiado bajo") #muestra "texto"
        
    elif random_number > key: #aquí empieza la segunda condición: si a > b
        print("El nº es demasiado alto") #muestra "texto"

    else : print("El nº buscado es:", key) #si no cumple ni if ni elifventonces muestra el texto y la variable key





# Nivel Intermedio
# Uso de break en un bucle
# Escribe un programa que recorra los números del 1 al 10, pero que se detenga y salga del bucle cuando encuentre el número 7.
# Uso de continue en un bucle
# Crea un programa que imprima todos los números del 1 al 10 excepto el número 5, usando continue.
# Bucle for con else
# Escribe un programa que recorra los números del 1 al 5. Si el número 3 no se encuentra en el recorrido, imprime "No se encontró el número 3". Usa un bloque else junto con el for.
# Condicional con operadores lógicos
# Pide al usuario dos números y verifica si ambos son positivos. Si lo son, imprime "Ambos son positivos". Si al menos uno es negativo, imprime "Hay al menos un número negativo".

list_number = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #defino la lista
key = 7 #indico en que nº (que no posición) quiero que el bucle se detenga

for stop_key in list_number: #defino una variable (sin declarar) dentro del for y elijo la lista que quiero que 
    print(stop_key) #aquí compruebo como el bucle recorre hasta stop_ky que es el valor donde quiero que pare
    if stop_key == key: #la variable (sin declarar) debe ser igual a la variable (declarada) que es el valor que quiero que pare al encontrarlo
       print(f"Se encontró {stop_key}.")    #indico que muestre un mensaje de que ha encontrado el resultado de la condición
       break

print("Fin del bucle")    
#------------------------------------------

list_number = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #defino la lista
key = 5 #indico en que nº (que no posición) quiero que el bucle se detenga

for stop_key in list_number: #defino una variable (sin declarar) dentro del for y elijo la lista que quiero que 
    print(stop_key) #aquí compruebo como el bucle recorre hasta stop_ky que es el valor donde quiero que pare
    if stop_key < key: #la variable (sin declarar) debe ser igual a la variable (declarada) que es el valor que quiero que pare al encontrarlo
       print(f"Se encontró {stop_key}.")    #indico que muestre un mensaje de que ha encontrado el resultado de la condición
       continue
    if stop_key > key: #la variable (sin declarar) debe ser igual a la variable (declarada) que es el valor que quiero que pare al encontrarlo   
       print(f"Continuo a partir del {stop_key}")     

print("Fin del bucle")  

#--------------------------------

list_number0 = [ 1, 2, 3, 4, 5]
a = 3 #defino la variable que no quiero encontrar
existe = False #declaro la posibilidad de que esa variable existe o no

for i in list_number0: #digamos que i es como una variable no declarada que va incluido en el for para poder realizar el bucle
    if i == a:
       a == True 
    else:
        print(f"El número {i} no existe")
        
#----------------------------------


# Solicito al usuario que ingrese dos números
input1 = float(input("Introduce un nº cualquiera: "))
input2 = float(input("Introduce otro nº cualquiera: "))

# Verificar si ambos números son positivos
if input1 < 0 or input2 < 0: #no incluyo el 0 puesto que me interesa sacar positivos y negativos
    print("Hay al menos un número negativo.")
elif input1 == 0 and input2 == 0 : #incluyo el 0 ya que el 0 negativo no existe 
    print("El valor es 0, siempre es positivo")
else: #no cumple ninguna de las condiciones anteriores entonces son positivos
    print("Los números son positivos.")


    


# Nivel Avanzado
# Bucle anidado simple (matriz)
# Dada la siguiente lista de sublistas (una matriz): 
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Crea un programa que imprima todos los elementos de la matriz, fila por fila, usando un bucle for anidado.
# if anidado
# Escribe un programa que pida un número al usuario y determine si es par o impar. Si es par, verifica además si es divisible por 4.
# Bucle while con validación
# Crea un programa que pida al usuario una contraseña. El programa debe seguir pidiendo la contraseña hasta que el usuario ingrese la correcta (puedes definir la contraseña como "1234"). Cuando el usuario ingrese la contraseña correcta, imprime "Acceso concedido".

# Ejercicios Extra
# Bucle for anidado con condicional
# Escribe un programa que recorra una lista de números. Si el número es divisible por 2, verifica si también es divisible por 3. Si lo es, imprime "Divisible por 2 y 3", de lo contrario imprime "Solo divisible por 2" 
# numeros = [6, 4, 9, 12, 15]
# Bucle for anidado: Tablas de multiplicar
# Escribe un programa que imprima las tablas de multiplicar del 1 al 5 utilizando bucles anidados.
#  Adivina el número con if anidado y while
# Escribe un programa donde el usuario debe adivinar un número secreto (puedes definirlo tú, por ejemplo, numero_secreto = 8). El programa debe seguir pidiendo intentos hasta que el usuario adivine el número. Si el número es demasiado alto, imprime "El número es muy alto", si es muy bajo, imprime "El número es muy bajo". Usa un bucle while y if anidados.
# Número primo (Reto)   
# Crea un programa que pida al usuario un número y verifique si es primo o no. Para ello, utiliza un bucle anidado: el bucle exterior para iterar sobre los números y el bucle interior para verificar si el número es divisible solo por 1 y por sí mismo.
# Bucle for y condicional con listas
# Dada una lista de palabras: 
# palabras = ["python", "bucles", "condicional", "anidado", "ejercicio"]
# Crea un programa que imprima solo las palabras que tengan más de 6 letras. Además, cuenta cuántas palabras cumplen esta condición.
