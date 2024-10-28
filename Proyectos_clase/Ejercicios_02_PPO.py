# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:22:06 2024

@author: rportatil112
"""


#############
# Ejercicio #
#___________#

# Crear la clase coche que incluya los atributos 
# "marca", "modelo", "longitud" y "precio"


# class Coche_1:
#     marca = "Volkswagen"
#     modelo = "Caddy"
#     longitud = 2.5
#     precio = 10000

class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
    def __str__(self):
    	return f"{self.marca} {self.modelo} de {self.longitud} y {self.precio}"
    
    


# Crear objetos de la clase coche
# Atribuirles características que se creen al inicializar, basadas en datos
# introducidos al crear los objetos

mi_coche = Coche("Wolkwagen", "Polo", 2, 10000) #instancia 

mi_furgoneta = Coche("Wolkswagen", "Caddy", 3, 15000) 

concesionario = Coche("Wolkswagen", "California", 5, 30000)




# Atribuirles métodos que permitan imprimir en la pantalla:
# Un mensaje al borrar el objeto

class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
    def __str__(self):
    	return f"{self.marca} {self.modelo} de {self.longitud} y {self.precio}"
    def __del__(self): #agrego un método mágico e imprimo 
        print(f"Se ha borrado el {Coche} de la BBDD ")

mi_coche = Coche("Wolkwagen", "Polo", 2, 10000) #al incluir una nueva modificación en la clase hay que volver a generar el objeto

del(mi_coche)

# un valor de longitud

class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
    def __str__(self):
    	return f"{self.marca} {self.modelo} de {self.longitud} y {self.precio}"
    # def __del__(self): #agrego un método mágico e imprimo 
    #     print(f"Se ha borrado el {Coche} de la BBDD ")
    def __len__(self):
        return self.longitud


mi_furgoneta = Coche("Volkswagen", "Caddy", 3, 15000) #hay que volver a ejecutar la clase ya que mi_furgoneta tiene los valores antiguos
mi_coche = Coche("Wolkwagen", "Polo", 2, 10000)


len(mi_furgoneta)

# un valor al hacer print()
print(mi_furgoneta)

print(mi_coche)
# Crear métodos que permitan comparar los coches por el precio:
    
class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
    def __str__(self):
    	return f"{self.marca} {self.modelo} de {self.longitud} y {self.precio}"
    # def __del__(self): #agrego un método mágico e imprimo 
    #     print(f"Se ha borrado el {Coche} de la BBDD ")
    def __len__(self):
        return self.longitud

    def __lt__(self, otro):
        return self.precio < otro.precio  

    def __le__(self, otro):
        return self.precio <= otro.precio  


# Crear dos instancias de la clase Coche
mi_furgoneta = Coche("Volkswagen", "Caddy", 3, 15000)
mi_coche = Coche("Wolkwagen", "Polo", 2, 10000)

    
    
# if coche1 > coche2:
#   pass
mi_coche > mi_furgoneta
mi_coche != mi_furgoneta
print(min(lista_coches))


"""
Crear un método que reduzca el precio del coche en un porcentaje 
introducido como argumento
"""
mi_coche.rebaja(25)