#
# Archivo: minimoComunMultiplo.py
#
# Descripción: Programa que dado dos números, devuelve el mínimo
#              común múltiplo entre ellos.
#
# Fecha de creación: 01/10/2017
# Última modificación: 23/11/2017

import sys
from primos import *

def minimoComunMultiplo(m,n,divisoresPrimosM = None,divisoresPrimosN = None):
    """
    Entrada
        * m: primer número.
        * n: segundo número.
        * divisoresPrimosM: lista de los factores primos de M,
            (opcional)      con sus multiplicidades.
        * divisoresPrimosN: lista de los factores primos de N,
            (opcional)      con sus multiplicidades.
    Salida
        * mcm: mínimo común múltiplo de los dos números. """
    
    if divisoresPrimosM == None:
        divisoresPrimosM = obtener_divisoresPrimos(m)
    if divisoresPrimosN == None:
        divisoresPrimosN = obtener_divisoresPrimos(n)
    mcm = 0
    m = abs(m)
    n = abs(n)
    if m == 1:
        mcm = n
    elif n == 1:
        mcm = m
    elif (m==0) or (n==0):
        pass
    else:
        try:
            assert(m == int(m))
            assert(n == int(n))
        except:
            print("No son números enteros")
            sys.exit()
        m = int(m)
        n = int(n)
        
        divisoresPrimosNmarcados = []

        divisoresComunes = []

        for i in range(len(divisoresPrimosM)):
            primoComunBuscar = divisoresPrimosM[i][0]
            encontrado = False
    
            # Comprobar si no hay que seguir buscando
            if primoComunBuscar > divisoresPrimosN[len(divisoresPrimosN)-1][0]:
                divisoresComunes.append((primoComunBuscar,divisoresPrimosM[i][1]))
                break
        
            for j in range(len(divisoresPrimosN)):
                if primoComunBuscar == divisoresPrimosN[j][0]:
                    if divisoresPrimosM[i][1] <= divisoresPrimosN[j][1]:
                        divisoresComunes.append((primoComunBuscar,divisoresPrimosN[j][1]))
                    else:
                        divisoresComunes.append((primoComunBuscar,divisoresPrimosM[i][1]))
                    encontrado = True
                    divisoresPrimosNmarcados.append(primoComunBuscar)
                    break
            if not encontrado:
                divisoresComunes.append((primoComunBuscar,divisoresPrimosM[i][1]))
        for i in range(len(divisoresPrimosN)):
            numero = divisoresPrimosN[i][0]
            if numero in divisoresPrimosNmarcados:
                divisoresPrimosNmarcados.remove(numero)
            else:
                divisoresComunes.append((numero,divisoresPrimosN[i][1]))

        for i in range(len(divisoresComunes)):
            if i == 0:
                mcm += divisoresComunes[i][0]**divisoresComunes[i][1]
            else:
                mcm *= divisoresComunes[i][0]**divisoresComunes[i][1]
            
    return mcm
