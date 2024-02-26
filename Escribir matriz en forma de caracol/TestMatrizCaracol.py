#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Archivo: TestMatrizCaracol.py
#
# Descripción: Archivo para ejecutar casos de prueba para el archivo
#              EscribirMatrizCaracolModulos.py
#
# Fecha: 06/03/2017
#

import unittest
from EscribirMatrizCaracolModulos import *

class GlobalTester(unittest.TestCase):

    def test_obtenerMatrizOriginal_NoRechazaMatrizErronea(self):
        # Comprueba si una matriz con dimensiones mal definidas es rechazada
        lineasLeidas = pedirDatos('MatrizErronea1.txt')
        salida       = obtenerMatrizOriginal(lineasLeidas)
        self.assertEqual(salida,0,"No rechazó la matriz errónea 1.")

        lineasLeidas = pedirDatos('MatrizErronea2.txt')
        salida       = obtenerMatrizOriginal(lineasLeidas)
        self.assertEqual(salida,0,"No rechazó la matriz errónea 2.")

    def test_obtenerMatrizOriginal_RechazaMatrizValida(self):
        # Comprueba si una matriz con dimensiones bien definidas es rechazada
        lineasLeidas = pedirDatos('MatrizValida1.txt')
        salida       = obtenerMatrizOriginal(lineasLeidas)
        self.assertEqual(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','14','16','17','18','19','100'], salida[0], "No devolvió la matriz como era.")
        self.assertEqual(4,salida[1],"El número de filas no es devuelto correctamente.")
        self.assertEqual(5,salida[2],"El número de columnas no es devuelto correctamente.")

    def test_obtenerMatrizOriginal_RechazaMatrizMasColumnasQueFilas(self):
        # COmrpueba si una matriz con más columnas que final es aceptada
        lineasLeidas = pedirDatos('MatrizMasColumnasQueFilas.txt')
        salida = obtenerMatrizOriginal(lineasLeidas)
        self.assertNotEqual(0, salida, "No acepta matrices con más columnas que filas.")
        self.assertEqual(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'], salida[0], "No leyó la matriz como era.")
        self.assertEqual(3,salida[1],"El número de filas no es devuelto correctamente.")
        self.assertEqual(5,salida[2],"El número de columnas no es devuelto correctamente.")

if __name__ == '__main__':
    unittest.main()

