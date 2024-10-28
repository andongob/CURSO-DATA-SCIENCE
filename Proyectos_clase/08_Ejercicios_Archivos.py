# Ejercicios Ficheros
# Recuerda marcar como directorio de trabajo el script donde estés ejecutando el fichero. También puedes crear una subcarpeta “archivos” donde meter todos los ficheros, para ello puedes usar rutas relativas: "./archivos/nombre_archivo.txt"
# Ejercicio 1: Leer un fichero de texto
# Objetivo: Crea un script que lea el contenido de un fichero llamado poema.txt y muestre su contenido en la consola.
# Abre el fichero en modo lectura ("r").
# Lee todo el contenido del fichero.
# Muestra el contenido en pantalla.
# Pistas:
# Usa la función open() para abrir el fichero.
# Usa el método .read() para leer todo el contenido de una sola vez.


with open("G:\Mi unidad\CURSO DATA SCIENCE\Proyectos_clase\Ejercicio_archivos\poema.txt", "w", encoding = "latin1") as poema_text:
    poema_text.write("Corazón Coraza - Mario Benedetti")


leer_poema = open("G:\Mi unidad\CURSO DATA SCIENCE\Proyectos_clase\Ejercicio_archivos\poema.txt", "r")
contenido_poema = leer_poema.read()
print(poema_text)
leer_poema.close()


# Ejercicio 2: Escribir en un fichero de texto
# Objetivo: Crea un script que escriba un mensaje en un fichero llamado notas.txt.
# Abre el fichero en modo escritura ("w").
# Si el fichero no existe, debe crearse automáticamente.
# Escribe en el fichero: "Esta es mi primera nota en este archivo."
# Pistas:
# Recuerda que el modo "w" sobrescribe el contenido si el fichero ya existe.
# Usa el método .write() para escribir en el fichero.

with open(r"G:\Mi unidad\CURSO DATA SCIENCE\Proyectos_clase\Ejercicio_archivos\notas.txt", "w") as notas_text:
    escribir_nota = notas_text.write("Esta es mi primera nota en este archivo.")
    print(notas_text)

# Ejercicio 3: Añadir contenido a un fichero
# Objetivo: Modifica el script del Ejercicio 2 para que no sobrescriba el contenido, sino que añada texto al final del fichero.
# Abre el fichero notas.txt en modo añadir ("a").
# Añade el siguiente mensaje: "Esta es otra línea añadida al archivo."
# Pistas:
# Usa el modo "a" para añadir contenido al final del fichero sin eliminar lo anterior.

notas_text = open(r".\Ejercicio_archivos\notas.txt", "a", encoding = "latin1")
notas_text.write("Esta es otra línea añadida al archivo. \n") #No es necesario declarar una variable en el write (respetar las nomenclaturas)\n continua la frase, si no se pone pasa al siguente renglón
print("Añado línea")
notas_text.close()

# Ejercicio 4: Leer líneas de un fichero
# Objetivo: Crea un script que lea y muestre cada línea de un fichero de texto, línea por línea.
# Usa el fichero poema.txt del Ejercicio 1.
# Abre el fichero en modo lectura.
# Lee el contenido línea por línea y muestra cada línea por separado.
# Pistas:
# Usa un bucle for para recorrer cada línea del fichero.

with open(".\Ejercicio_archivos\poema.txt", "r", encoding ="latin1") as lineas_poema:
    contenido_poema_lineas = lineas_poema.readlines()

for lineas in contenido_poema_lineas:
    print(poema_text)

# Ejercicio 5: Manejo de excepciones al leer un fichero
# Objetivo: Crea un script que intente leer un fichero llamado archivo_inexistente.txt y capture el error si el fichero no existe.
# Usa un bloque try-except para manejar el error FileNotFoundError.
# Si el fichero no se encuentra, muestra el mensaje "Error: El archivo no existe.".
# Pistas:
# Usa try-except para manejar la excepción FileNotFoundError.

try:
    with open(".\Ejercicio_archivos\archivo_inexistente.txt", "r") as archivo:
        leer_archivo = archivo.read()
        print("Contenido del archivo:")
        print(leer_archivo)
        
except FileNotFoundError:
    print("Error: El fichero 'archivo_inexistente.txt' no existe.")
        


# Ejercicio 6: Leer y escribir en un fichero CSV
# Objetivo: Crea un script que lea un fichero CSV llamado alumnos.csv, muestre su contenido y luego añada un nuevo alumno.
# Usa el fichero alumnos.csv con las columnas: Nombre, Edad, Email.
# Muestra el contenido de cada fila del fichero CSV.
# Añade un nuevo alumno al fichero: "Carlos, 24, carlos@mail.com".
# Pistas:
# Usa el módulo csv para manejar el fichero.
# Usa el método .writerow() para añadir nuevas filas.

import csv

with open(r".\Ejercicio_archivos\alumnos.csv", "w") as alumnos:
    escribe_cabecera = csv.writer(alumnos)
    escribe_cabecera.writerow(["Nombre", "Edad", "mail"])
    print(escribe_cabecera)
    escribe_cabecera.writerow(["Carlos", 24, "carlos@mail.com"])
    escribe_cabecera.writerow(["Ana", 43, "ana@mail.com"]) 
    escribe_cabecera.writerow(["Pedro", 35, "pedro@mail.com"]) 

   
# Ejercicio 7: Contar líneas y palabras en un fichero
# Objetivo: Crea un script que cuente el número de líneas y el número total de palabras en un fichero llamado texto.txt.
# Abre el fichero en modo lectura.
# Recorre cada línea del fichero, contando el número de líneas.
# Para cada línea, cuenta cuántas palabras contiene y suma el total de palabras.
# Muestra el número total de líneas y el número total de palabras.
# Pistas:
# Usa el método .split() para dividir una línea en palabras.
# Utiliza un contador para sumar las palabras.

with open(r".\Ejercicio_archivos\texto.txt", "w", encoding="latin1") as contar_texto:
    crear_archivo = contar_texto.write("Este un archivo recién salido del horno. \n")
    print(contar_texto)
    
    
with open(r".\Ejercicio_archivos\texto.txt", "a", encoding="latin1") as contar_texto:
    crear_archivo = contar_texto.write(" Y esta una línea recién agregada. \n")
    print(contar_texto)
    
with open(r".\Ejercicio_archivos\texto.txt", "r", encoding="latin1") as contar_texto:
    contar_texto.seek(0) #coloca el puntero al inicio del fichero
    lineas = contar_texto.readlines()
    contar_texto.split("\n")
    

with open(r".\Ejercicio_archivos\texto.txt", "r", encoding="latin1") as contar_texto:
    contar_texto.seek(0)  # Coloca el puntero al inicio del fichero
    lineas = contar_texto.readlines()
    
    len(lineas)
    
palabras = 0

for linea in líneas:
    palabras = palabras + len(linea.split(" ")
                              print(palabras)
                              

# Ejercicio 8: Buscar y eliminar duplicados en un fichero CSV
# Objetivo: Crea un script que lea un fichero CSV llamado clientes.csv y elimine los registros duplicados basados en la columna Email.
# Abre el fichero en modo lectura.
# Almacena los registros en un diccionario usando el Email como clave para eliminar duplicados.
# Escribe los registros únicos en un nuevo fichero CSV llamado clientes_unicos.csv.
# Pistas:
# Usa un diccionario para evitar duplicados.
# Escribe los registros únicos en un nuevo CSV.

# Ejercicio 9: Leer un fichero y buscar una palabra
# Objetivo: Crea un script que lea un fichero llamado libro.txt y busque una palabra específica introducida por el usuario.
# Solicita al usuario que introduzca la palabra a buscar.
# Abre el fichero y recorre su contenido.
# Muestra cuántas veces aparece la palabra en el fichero.
# Pistas:
# Usa el método .count() para contar las apariciones de la palabra en cada línea.




