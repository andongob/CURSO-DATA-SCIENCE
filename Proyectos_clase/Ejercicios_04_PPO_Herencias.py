#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

import sys
sys.path.append(r"G:\Mi unidad\CURSO DATA SCIENCE\scripts_teoria\POO\personapp.py")  # Ajusta esta ruta según tu configuración
from datetime import timedelta, time


# Clase Persona que será la clase padre, aquí metemos la comprobación del DNI y no "tocamos" la importación
class Persona:
    def __init__(self, nombre, apellido1, apellido2="", ubicacion="", dni=None):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.ubicacion = ubicacion
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.sueldo_hora = 20
        self.dietas = 0
        self.dni = dni

    def validar_dni(dni):
        letras_control = "TRWAGMYFPDXBNJZSQVHLCKE"
        '''
        Coincide con el órden de la URL: 
        "https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/"
        '''
        
        if len(dni) != 9:
            return False, "El DNI debe tener 9 caracteres."

        numero = dni[:-1]  # Los primeros 8 caracteres (números)
        letra = dni[-1].upper()  # El último carácter, en mayúsculas
        '''
        Separamos los números y la letra de control
        '''

        if not numero.isdigit():
            return False, "Los primeros 8 caracteres deben ser dígitos."
        '''
        isdigit() solo verifica si la cadena podría ser un número entero (contiene solo dígitos). INT convierte a tipo, no verifica.
        '''

        numero = int(numero)
        letra_calculada = letras_control[numero % 23]
        '''
        En este caso sí que está convirtiendo la variable número en un int.
        '''

        # Verifica si la letra de control es correcta
        if letra == letra_calculada:
            return True, "DNI válido."
        else:
            return False, f"Letra de control incorrecta. Debería ser '{letra_calculada}'."


# Clase empleado que hereda de Persona
class empleado(Persona):
    def __init__(self, nombre, apellido1, apellido2="", ubicacion="", dni=None):
        super().__init__(nombre, apellido1, apellido2=apellido2, ubicacion=ubicacion, dni=dni)
        # Elimina `self` en el llamado a super()

        '''
        El super() recibe los parámetros del __init__ de la clase, super es aquí donde hereda, es decir, 
        la clase padre recibe los datos introducidos en la clase empleado.
        '''
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.sueldo_hora = 20
        self.dietas = 0

    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_tiempo_trabajado()
        print(f"El tiempo trabajado calculado: {tiempo_trabajado}")
        tiempo_trabajado = tiempo_trabajado.total_seconds()
        print(f"El tiempo trabajado en segundos: {tiempo_trabajado}")
        sueldo_a_pagar = self.sueldo_hora * tiempo_trabajado / 3600
        sueldo_a_pagar += self.dietas
        return sueldo_a_pagar


# Clase peon que hereda de empleado
class peon(empleado):
    def __init__(self, nombre, apellido1, apellido2="", ubicacion="", dni=None, guardia=False, bonus=""):
        super().__init__(nombre, apellido1, apellido2=apellido2, ubicacion=ubicacion, dni=dni)
        '''
        El super() recibe los parámetros del __init__ de la clase, super es aquí donde hereda, es decir, 
        la clase padre recibe los datos introducidos en la clase empleado.
        '''
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.sueldo_hora = 20
        self.dietas = 0
        self.guardia = guardia
        self.bonus_guardia = 30
        self.bonus = bonus

    def esta_de_guardia(self):
        """
        Verifica si el último fichaje cae dentro del horario de guardia (22:00 a 07:00).
        """
        if not self.fichajes:
            return False  # Aquí verificamos si ha fichado o no

        inicio_guardia = time(22, 0)  # 22:00
        fin_guardia = time(7, 0)      # 07:00
        '''
        Utilizo el método time de la librería datetime
        '''
        
        ultimo_fichaje = self.fichajes[-1].time()
        '''
        Aquí al ser fichajes una lista, recogemos el último valor [-1] para verificar si está dentro del rango de guardia
        ya que será la última hora registrada
        '''
        
        if inicio_guardia <= ultimo_fichaje or ultimo_fichaje <= fin_guardia:  # aquí verificamos el rango de horas
            print(f"{self.nombre} está en horario de guardia.")
            return True
        else:
            print(f"{self.nombre} no está en horario de guardia.")
            return False

    def calcula_sueldo(self):
        sueldo_a_pagar = super().calcula_sueldo()
        '''
        Importo la funcion calcula_sueldo de la clase padre
        '''

        if self.esta_de_guardia():
            sueldo_a_pagar += self.bonus_guardia
        '''
        le sumo el bonus
        '''
        return sueldo_a_pagar


# Clase oficinista que hereda de Persona
class oficinista(Persona):
    def __init__(self, nombre, apellido1, apellido2="", ubicacion="", dni=None):
        super().__init__(nombre, apellido1, apellido2=apellido2, ubicacion=ubicacion, dni=dni)
        '''
        El super() recibe los parámetros del __init__ de la clase, super es aquí donde hereda, es decir, 
        la clase padre recibe los datos introducidos en la clase empleado.
        '''
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.sueldo_hora = 20
        self.dietas = 0


# Clase directivo que hereda de Persona
class directivo(Persona):
    pass


if __name__ == "__main__":
    # Ejemplo de uso y verificación del DNI
    dni = "12345678Z"
    valido, mensaje = Persona.validar_dni(dni)
    print(mensaje)
