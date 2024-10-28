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

class Persona1:
 
    def __init__(self, nombre, primer_apellido, segundo_apellido, ubicacion = ""): 
        '''
        #ponemos ubicación como valor opcional a rellenar, importante recordar,
        una vez que ponga un argumento tipo clave = valor, todos los siguientes deben ser
        igual clave = valor
        '''
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.trabajando = False
        '''
        Al ser booleano no es necesario declararlo en la función
        '''
        self.ubicacion = ubicacion
    def presentarse(self):
        print (f"Hola, Me llamo es {self.nombre}")
    def ficha(self):
        if self.trabajando == True:
            print("Has fichado correctamente")
        else:
            print("No ha fichado")
    def viajar(self, nueva_ubicacion):
        print(f"{self.nombre} se ha trasladado de {self.ubicacion} a {nueva_ubicacion}.")
        self.ubicacion = nueva_ubicacion
    

director = Persona('Juan', 'Pérez', 'López', "Bilbao") 
'''
Aqui Bilbao puede estar o no y no dará error porque le hemos declarado la ubicación = "" (vacía)
si ponemos None nos saldrá el valor y a veces esto no nos interesa, ejemplo: Juan Perez None
'''
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

director.viajar("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")


#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------

from datetime import datetime, timedelta

class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, ubicacion="", tarifa=10):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.ubicacion = ubicacion
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)  # Tiempo total trabajado
        self.tarifa = tarifa  # Tarifa por hora

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} {self.primer_apellido} {self.segundo_apellido}")

    def fichar(self):
        ahora = datetime.now() #método now de la librería datetime
        if self.trabajando:
            # Cálculo de tiempo trabajado al fichar salida
            tiempo_jornada = ahora - self.fichajes[-1][0]
            self.tiempo_trabajado += tiempo_jornada
            print(f"{self.nombre} ha fichado su salida a las {ahora}. Jornada: {tiempo_jornada}")
            self.fichajes.append((ahora, "Salida"))
        else:
            # Fichaje de entrada
            print(f"{self.nombre} ha fichado su entrada a las {ahora}.")
            self.fichajes.append((ahora, "Entrada"))
        
        # Cambia el estado de trabajando
        self.trabajando = not self.trabajando
    
    def viajar(self, nueva_ubicacion):
        print(f"{self.nombre} se ha trasladado de {self.ubicacion} a {nueva_ubicacion}.")
        self.ubicacion = nueva_ubicacion

    def mostrar_fichajes(self):
        print(f"Fichajes de {self.nombre}:")
        for hora, tipo in self.fichajes:
            print(f"{tipo} a las {hora}")

    def calcula_sueldo(self):
        # Calcular sueldo en función del tiempo trabajado acumulado
        horas_trabajadas = self.tiempo_trabajado.total_seconds() / 3600
        sueldo = horas_trabajadas * self.tarifa
        dieta = self.dieta_transporte()
        return sueldo + dieta
    
    def dieta_transporte(self):
        self.dieta = 1
        sueldo_a_pagar = 0
        if self.trabajando:
            sueldo_a_pagar += self.dieta
        else:
                print("No aplica la dieta")
        return(sueldo_a_pagar)

            




# Crear instancias de Persona
director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

# Fichar entrada para secretario
secretario.fichar()  # "Juanito ha fichado su **entrada** a las ..."
# Fichar salida para secretario
secretario.fichar()  # "Juanito ha fichado su **salida** a las ..."

# Mostrar fichajes de secretario
secretario.mostrar_fichajes()  # Mostrar entradas y salidas registradas


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