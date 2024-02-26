#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Archivo: EscribirMatrizCaracolModulos.py
#
# Descripción: Módulos para el archivo EscribirMatrizCaracolModulosProgramaPrincipal.py
#
# Fecha: 06/03/2017
#

def pedirDatos(entrada = 'MatrizArchivoGenerico.txt'):
    """ Función que recibe como entrada un archivo que contiene una matriz.
        Devuelve un arreglo cuyos elementos son las líneas del archivo.
    """
    archivo  = open(entrada,'r')
    devolver = archivo.readlines()
    archivo.close()
    return devolver

def obtenerMatrizOriginal(lineasLeidas):
    """ Recibe como entrada un arreglo con las líneas leídas de un archivo,
        las cuales se supone deben representar las filas de la matriz.
        
        Devuelve como salida un vector de tres elementos:

        1) La matriz leída desde el archivo, pero escrita como una lista.
        2) El número de filas de la matriz.
        3) El número de columnas de la matriz.

        Además, imprime un mensaje de error y finaliza la ejecución del programa
        en caso de que las dimensiones no correspondan en todas las filas y columnas.
    """

    matrizLista = []
    numColumnas = 0
    numFilas = 0

    for linea in lineasLeidas:
        sumarUnaFila = False
        linea = linea.split(" ") # Los elementos están separados por espacios
        longitudFilaActual = 0
        
        for elemento in linea:
            if elemento == "\n" or elemento == " ":
                pass
            else:
                elemento = elemento.split("\n")
                matrizLista.append(elemento[0])
                longitudFilaActual += 1
                sumarUnaFila = True

        if sumarUnaFila:
            numFilas += 1
            if numColumnas == 0:
                numColumnas = longitudFilaActual
            else:
                if numColumnas != longitudFilaActual:
                    return 0

    return matrizLista, numFilas, numColumnas

def errorObteniendoMatriz():
    import sys 
    print("ERROR: Las filas deben ser todas del mismo tamaño.")
    sys.exit()
    
def convertirMatrizACaracol(matrizLista,numFilas,numColumnas):
    matrizCaracol = []
    for i in range(numFilas):
        matrizCaracol.append([])
        for j in range(numColumnas):
            matrizCaracol[i].append("$%")

    if numFilas <= numColumnas:
        numIteraciones = numFilas
    else:
        numIteraciones = numColumnas

    indiceLista = 0

    for it in range(numIteraciones):
        # Caso en que la iteración sea par
        if it%2 == 0:
            # Llenar la fila
            for k in range(it//2,numColumnas-it//2):
                matrizCaracol[it//2][k] = matrizLista[indiceLista]
                indiceLista += 1
            # Llenar la columna
            for k in range(1+it//2,numFilas-it//2):
                matrizCaracol[k][numColumnas-1-it//2] = matrizLista[indiceLista]
                indiceLista += 1

        else:
            # Llenar la fila
            for k in range(it//2,numColumnas-1-it//2):
                matrizCaracol[numFilas-1-it//2][numColumnas-2-k] = matrizLista[indiceLista]
                indiceLista += 1
            # Llenar la columna
            for k in range(1+it//2,numFilas-1-it//2):
                matrizCaracol[numFilas-1-k][it//2] = matrizLista[indiceLista]
                indiceLista += 1

    return matrizCaracol


            
            
            
            
            
