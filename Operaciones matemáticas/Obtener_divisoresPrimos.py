#
# Archivo: Obtener_divisoresPrimos.py
#
# Descripción: Programa que dado un número, devuelve luna lista con sus
#              divisores primos y la multiplicidad de cada uno.
#              Se invoca llamando "Obtener_divisoresPrimos(n).lista"
#
# Fecha de creación: 01/10/2017

from Hallar_primosN import *

class Obtener_divisoresPrimos():
    def __init__(self,n):
        listaPrimos = Hallar_primosN(n).lista
        listaDivisores = []
        res = n
        for i in range(len(listaPrimos)):
            primo = listaPrimos[i]
            multiplicidad = 0
            while res%primo == 0:
                multiplicidad +=1
                res = res/primo
                res = int(res)
            if multiplicidad != 0:
                listaDivisores.append((primo,multiplicidad))
        self.lista = listaDivisores
    
