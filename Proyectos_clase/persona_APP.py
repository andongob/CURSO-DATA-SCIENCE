# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:54:58 2024

@author: rportatil112
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

if __name__ == "__name__": #te da una pista de la ubicación del archivo
    print("Se ha cargado la clase persona")
    '''
    En este caso si ejecuto este código en este archvio y ubicación imprimirá el print "Se ha cargado la clase persona"
    en cambio este mensaje no aparecerá cuando está este código importado desde otro script.jpy
    '''
