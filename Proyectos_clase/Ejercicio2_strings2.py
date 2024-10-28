# # -*- coding: utf-8 -*-
# """
# Created on Tue Oct  8 12:39:56 2024

# @author: rportatil112
# """
%reset -f

# Ejercicio 1: Transformación de cadenas
# Define una cadena con el valor "PYTHON es un lenguaje GENIAL".
# Convierte la cadena a minúsculas, luego a mayúsculas, y finalmente,
 transforma solo las primeras letras de cada palabra en mayúsculas (capitalización).
# Invierte el orden de los caracteres de la cadena.

phrase1 = 'PYTHON es un lenguaje GENIAL'
phrase1Minus = phrase1.lower()
phrase1Mayus = phrase1.upper()
phrase1.title()
phrase1Invertida = phrase1[::-1]
print(phrase1Invertida)


# Ejercicio 2: Extracción de iniciales
# Define una cadena con tu nombre completo (nombre y apellido).
# Extrae las iniciales de tu nombre y apellido usando slicing y concatenación.

name = 'Ana Verónica'
surname1 = 'Ndongo'
surname2 = 'Bindang'
initName = name[0]
initName2 = name[4]
initSurname1 = surname1[0]
initSurname2 = surname2[0]
print(initName, initName2, initSurname1, initSurname2)


# Ejercicio 3: Crear un mensaje dinámico
# Define tres variables: producto, precio, y cantidad (con valores cualquiera).
# Crea un mensaje dinámico que diga: "Compraste [cantidad] unidades de [producto] a un precio de [precio] cada uno."
# Calcula el costo total (multiplicando cantidad y precio) e incluye esta información en el mensaje.

producto = 'piruletas'
precio = 2
cantidad = 20
msgDinamic = f'Compraste {cantidad} unidades de {producto} a un precio de {precio}'
print(msgDinamic)


# Ejercicio 4: Comparar dos frases
# Define dos frases y verifica si son exactamente iguales.
# Convierte ambas frases a minúsculas y vuelve a compararlas para ignorar diferencias en mayúsculas/minúsculas.

phrase1 = 'En Bilbo hace frío'
phrase2 = 'En Sevilla hace calor'
phrase1 == phrase2

phrase1Minus = phrase1.lower()
phrase2Minus = phrase2.lower()


# Ejercicio 5: Recuento de vocales
# Define una frase cualquiera.
# Cuenta cuántas veces aparece cada vocal (a, e, i, o, u) en la frase.

phrase2 = 'En Bilbo hace frío'
phrase2Count = phrase2.count('a')
phrase2Count = phrase2.count('e')
phrase2Count = phrase2.count('i')
phrase2Count = phrase2.count('o')
phrase2Count = phrase2.count('u')

# Ejercicio 6: Crear un acrónimo
# Define una cadena con una frase de varias palabras (por ejemplo, "Asociación Internacional de Programadores").
# Crea un acrónimo con las iniciales de cada palabra (por ejemplo, "AIP").

phrase3 = 'Club Internacional De Piruletas Rojas'
print('phrase3')
phrase3 = phrase3.max()


# Ejercicio 7: Cambiar palabras en una frase
# Define una frase.
# Reemplaza una palabra específica en la frase por otra de tu elección.


phrase4 = 'En Gazteiz hace CALOR'
replacePhrase4 = phrase4.replace('CALOR', 'FRÍO')
print(replacePhrase4)

# Ejercicio 8: Verificar si una palabra está contenida
# Define una frase y una palabra.
# Verifica si la palabra está contenida en la frase y muestra el resultado.

phrase5 = 'Bilbao no tiene mar'
print('mar' in phrase5)
print(str('mar'))

# Ejercicio 9: Recortar y reorganizar una frase
# Define una frase con tres palabras.
# Reorganiza las tres palabras en un nuevo orden utilizando la concatenación.

phrase6 = 'Tengo tres peras'
phrase6Reorder = 'peras' + ' ' + 'tres' + ' ' + 'Tengo'
phrase6Split = phrase6.split(' ')

# Ejercicio 10: Formato de números y alineación
# Define un número decimal cualquiera.
# Imprime el número con 3 decimales y luego alinéalo a la izquierda, derecha y centro en un espacio de 12 caracteres.

j = 10.2575
print("{:.3f}".format(j))

print(f"{j:<12.3f}")  # Izquierda
print(f"{j:>20.3f}")  # Derecha
print(f"{j:^30.3f}")  # Centro

