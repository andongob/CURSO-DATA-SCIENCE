# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:54:28 2024

@author: rportatil112
"""
import os
os.chdir("G:\Mi unidad\CURSO DATA SCIENCE\Proyectos_clase")

from persona_APP import Persona #importo el fichero persona y no tengo que ejecutarlo,solo probar aquí el código

director = Persona('John', 'Taylor', ubicacion = "Teruel", tarifa = ())
secretario = Persona('Juanito', 'Pérez', 'García')


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')


secretario.ficha()
secretario.trabajando

secretario.fichajes
secretario.muestra_fichajes()



