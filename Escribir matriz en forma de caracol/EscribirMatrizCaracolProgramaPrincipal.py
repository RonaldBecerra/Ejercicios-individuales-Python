#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Archivo: EscribirMatrizCaracolProgramaPrincipal.py
#
# Descripción: Archivo que dada una matriz, la coloca en forma de caracol o
#              enrollada, siguiendo el sentido horario.
#
# Fecha: 06/03/2017
#
# Motivo: Tenía este algoritmo antes de que accidentalmente formateara mi
#         computadora, y ahora quiero recuperarlo.
#

from EscribirMatrizCaracolModulos import *

nombre = input("Ingrese el nombre del archivo que contiene la matriz: ")

if nombre == "":
    lineasLeidas = pedirDatos()
else:
    lineasLeidas = pedirDatos(nombre)

resultadoObtenerMatriz = obtenerMatrizOriginal(lineasLeidas)

if resultadoObtenerMatriz == 0:
    errorObteniendoMatriz()
else:
    matriz = resultadoObtenerMatriz[0]
    numFilas = resultadoObtenerMatriz[1]
    numColumnas = resultadoObtenerMatriz[2]

matrizFinal = convertirMatrizACaracol(matriz,numFilas,numColumnas)

for fila in matrizFinal:
    print(fila)
