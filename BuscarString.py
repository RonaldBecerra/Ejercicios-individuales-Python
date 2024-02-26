#!/usr/bin/python
import os
import sys

class globales:
    resultado = []

globales = globales()

# Función principal en la que el usuario indica en qué ruta inicia la búsqueda
def buscar():
    ruta = input("Ingrese la ruta a examinar: ")
    texto = input("Ingrese el texto a ser buscado: ")
    buscarSubdirectorios = input("¿Quiere buscar también en subdirectorios (s/n)? ");

    if buscarSubdirectorios in ['1', 1, "S", "s"]:
        buscarSubdirectorios = True
    else:
        buscarSubdirectorios = False

    buscar_aux(ruta, texto.lower(), buscarSubdirectorios)

    if len(globales.resultado) != 0:
        print("\nLa rutas donde se encontraron resultados son:\n")
        i = 0
        for elem in globales.resultado:
            i += 1
            print(str(i) + ") " + elem)


# Función que va examinando los elementos de un directorio
# Se llama recursivamente si el elemento es un directorio
# Si es un archivo, invoca a otra función para examinarlo
def buscar_aux(ruta, texto, buscarSubdirectorios):
    try:
        elementos = os.listdir(ruta)

        for elem in elementos:
            rutaExaminar = ruta + '\\' + elem
            examinar_archivo(rutaExaminar, texto, buscarSubdirectorios)
    except:
        pass

# Examina las líneas de un archivo y determina si encuentra el texto indicado
def examinar_archivo(rutaArchivo, texto, buscarSubdirectorios):
    try:
        archivo = open(rutaArchivo)
        sePudoLeer = True
    except:
        sePudoLeer = False

    if sePudoLeer:
        for linea in archivo:
            arregloSplit = linea.lower().split(texto)
            if (len(arregloSplit) > 1):
                globales.resultado.append(rutaArchivo)
                break;
        archivo.close() 

    elif buscarSubdirectorios:
        # Si no se pudo leer probablemente es porque es un directorio
        buscar_aux(rutaArchivo, texto, buscarSubdirectorios)   

buscar()
