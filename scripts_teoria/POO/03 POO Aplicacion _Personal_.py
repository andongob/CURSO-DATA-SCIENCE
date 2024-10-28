#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

####################################
# Programación Orientada a Objetos #
####################################
# Creamos una aplicación para gestionar el "Personal" de una empresa

#----------------------------------
# Etapa1: Creo una clase "Persona"
#----------------------------------
"""
Los atributos de una persona serán.
    Nombre
    Apellidos (1º y 2º)
    trabajando (booleano)
    Ubicación
    
La Persona podrá:
    Presentarse
    Fichar (modificando trabajando a True o False)
    Viajar (cambiando la ubicacion)

"""

class Persona:
    pass

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

print(type(director))
print(type(secretario))

director.presentarse()
secretario.presentarse()

director.trabajando
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

director.viaja("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")


#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------
"""
Ahora al fichar, se almacenarán los fichajes en una lista

"""









director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')


secretario.ficha()
secretario.trabajando

secretario.fichajes
secretario.muestra_fichajes()

#-------------------------------------------------------------
# Etapa2: Vamos a llevar la contabilidad del tiempo trabajado 
#-------------------------------------------------------------
"""
Un método calculará el tiempo que se ha trabajado a partir de los fichajes

Añadiremos además un atributo de "sueldo_hora" para calcular el salario
"""



#############
# Ejercicio #
#___________#
"""
Crear un método que asigne una dieta de transporte de un euro cada vez que una 
persona fiche

Modificar el método que calcula el sueldo para que añada la dieta de transporte.
"""