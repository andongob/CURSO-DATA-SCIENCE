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
    def __init__(self, nombre, apellido1, apellido2 = "", ubicacion = ""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.ubicacion = ubicacion
        self.trabajando = False
        
    def presentarse(self):
        print(f"Soy {self.nombre} {self.apellido1} {self.apellido2}")
        
    def ficha(self):
        self.trabajando = not self.trabajando
        if self.trabajando:
            print("Bienvenido al trabajo, {self.nombre}")
        else:
            print("Adiós")
    
    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} --> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion



director = Persona('John', 'Taylor', ubicacion = "Teruel")
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

from datetime import datetime, timedelta

class Persona:
    def __init__(self, nombre, apellido1, apellido2="", ubicacion="", tarifa=10):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.ubicacion = ubicacion
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.tarifa = tarifa  # Tarifa por hora

    def presentarse(self):
        print(f"Soy {self.nombre} {self.apellido1} {self.apellido2}")
        
    def ficha(self):
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.now())
        if self.trabajando:
            print(f"Bienvenido al trabajo, {self.nombre}")
        else:
            print("Adiós")
    
    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} --> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    def muestra_fichajes(self):
        entrada, salida = self.separa_entrada_salida()
        print("Entradas                              Salidas")
        for ent, sal in zip(entrada, salida):
            print(f"{ent}    {sal}")
    
    def separa_entrada_salida(self):
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        return entradas, salidas
    
    def calcula_tiempo_trabajado(self):
        entrada, salida = self.separa_entrada_salida()
        tiempo_acumulado = timedelta(0)
        for ent, sal in zip(entrada, salida):
            tiempo_jornada = sal - ent
            tiempo_acumulado += tiempo_jornada
        self.tiempo_trabajado = tiempo_acumulado
        return tiempo_acumulado

    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_tiempo_trabajado()
        sueldo_a_pagar = self.tarifa * (tiempo_trabajado.total_seconds() / 3600)  # Convierte a horas
        return sueldo_a_pagar

    def dieta_transporte(self):
        self.dieta = 1
        sueldo_a_pagar = 0
        if self.trabajando:
            sueldo_a_pagar += self.dieta
        else:
            print("No aplica la dieta")
        return sueldo_a_pagar

        
timedelta(0)
secretario.sueldo_hora = 18

director = Persona('John', 'Taylor', ubicacion = "Teruel", tarifa = ())
secretario = Persona('Juanito', 'Pérez', 'García')


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