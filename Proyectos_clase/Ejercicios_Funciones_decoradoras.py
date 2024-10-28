# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 23 09:36:57 2024

# @author: rportatil112
# """

# Ejercicio 1: Creación básica de un decorador
# Escribe un decorador básico llamado mi_decorador que imprima "Llamando a la función" antes de ejecutar la función decorada 
# y "Función ejecutada" después de que la función decorada haya terminado.

def mi_decorador(func): #func hará referencia a la función que va a ser decorada
    def lo_que_hace_mi_decorador():
        print("Llamando a la función") #imprime antes de que se ejecute la función a decorar
        func() #se ejecuta la función a decorar
        print('Función ejecutada') #imprime después de que se ejecute la función a decorar
    return(lo_que_hace_mi_decorador) #devuelve la "decoración"
        

@mi_decorador
def saludar():
    print("¡Hola!")
    
# Llamada a la función decorada
saludar()
'''
Es imprtante ejecutar el código completo
seleccionando todo
'''



# Ejercicio 2: Decorador con argumentos
# Modifica el decorador mi_decorador para que sea capaz de decorar una función con cualquier número de argumentos. 
# (Empieza con 2 argumentos, usando la función sumar(a, b) como ejemplo de función decorada.)
def mi_decorador(func):
    # Completa el decorador para aceptar funciones con argumentos
    def multi_argumentos(*args):
        resultado = func(*args)
        return(resultado)
    return(multi_argumentos)
           

@mi_decorador
def sumar(a, b):
    return a + b

# Llamada a la función decorada
resultado = sumar(3, 4)
print(f"Resultado de la suma: {resultado}")


# Ejercicio 3: Decorador con retorno modificado
# Crea un decorador llamado duplicar_resultado que modifique la función decorada para que su resultado se duplique.
# Usa la función multiplicar(a, b) para probar el decorador.
def duplicar_resultado(func):
    # Completa el decorador para duplicar el resultado de la función
    def multiplica_resultado(a, b):
        resultado = func(a, b ) * 2 
        return(resultado)
    return(multiplica_resultado)
    

@duplicar_resultado
def multiplicar(a, b):
    return a * b

# Llamada a la función decorada
resultado = multiplicar(5, 3)
print(f"Resultado duplicado: {resultado}")


# Ejercicio 4: Decorador anidado
# Crea dos decoradores: decorador1 y decorador2. El primero imprimirá "Primero" antes de ejecutar la función decorada, 
# y el segundo imprimirá "Segundo". Luego, aplica ambos decoradores a la función mi_funcion.
def decorador1(func):
    # Completa decorador1
    def imp_antes():
        print("Primero")
        func()
    return(imp_antes)
'''
Cuidado con la posición del return
'''

def decorador2(func):
    # Completa decorador2
    def imp_despues():
        func()
        print("Segundo")
    return(imp_despues)
'''
Cuidado con la posición del return
'''

@decorador1
@decorador2
def mi_funcion():
    print("¡Hola desde la función!")

# Llamada a la función decorada
mi_funcion()


# Ejercicio 5: Aplicación práctica (autenticación)
# Imagina que estás desarrollando una aplicación y necesitas controlar el acceso a ciertas funciones según si el usuario está autenticado o no. Crea un decorador llamado requiere_autenticacion que verifique si una variable global usuario_autenticado es True antes de permitir la ejecución de una función. Si el usuario no está autenticado, imprime un mensaje de error.
# usuario_autenticado = False

# def requiere_autenticacion(func):
#     # Completa el decorador para verificar la autenticación
#     pass

# @requiere_autenticacion
# def ver_perfil():
#     print("Perfil del usuario")

# # Intenta ejecutar la función decorada
# ver_perfil()

# # Simula la autenticación del usuario
# usuario_autenticado = True
# ver_perfil()


# Ejercicio 6: Decorador que limita el tiempo
# Objetivo: Crear un decorador con parámetros que simule un "timeout" o tiempo límite.
# Implementa un decorador llamado timeout(segundos) que limite la ejecución de una función a un máximo de n segundos. Si la función tarda más de ese tiempo en ejecutarse, debe devolver un mensaje como "Tiempo de espera excedido".
# import time

# def timeout(segundos):
#     # Implementa aquí el decorador que limite el tiempo de ejecución
#     pass

# @timeout(3)
# def tarea_larga():
#     time.sleep(5)
#     print("¡Tarea completada!")

# # Llamada a la función decorada
# tarea_larga()



# Ejercicio 7: Modificar el resultado según un parámetro
# Objetivo: Manipular el resultado de una función con un decorador que acepte parámetros.
# Crea un decorador llamado multiplica_resultado(factor) que multiplique el resultado de la función decorada por un valor dado.
def multiplica_resultado(factor): #recibe el parámetro, recibe el nº 10 del del ejemplo obtener()
    # Implementa aquí el decorador con parámetros
    def resultado_multiplicado(func): #devuelve la función decorada()
        def decorada(): #ejecuta la función func() 
            resultado = func()
            return(resultado * factor)
        return decorada
    return(resultado_multiplicado) #devuelve la función dentro de la función decoradora

@multiplica_resultado(10)
def obtener_numero():
    return 7

# Llamada a la función decorada
print(obtener_numero())  # Debería imprimir 70



