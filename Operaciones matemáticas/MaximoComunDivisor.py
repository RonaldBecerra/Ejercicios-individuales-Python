#
# Archivo: MaximoComunDivisor.py
#
# Descripción: Programa que dado dos números, devuelve el máximo
#              común divisor entre ellos. Para usarlo, se debe invocar
#              de la forma "MaximoComunDivisor(m,n).valor"
#
# Fecha de creación: 01/10/2017

import sys
from Obtener_divisoresPrimos import *

class MaximoComunDivisor():
    def __init__(self,m,n):
        mcd = 1
        m = abs(m)
        n = abs(n)
        if (m == 1) or (n==1):
            pass
        elif m == 0:
            mcd = n
        elif n == 0:
            mcd = m
        else:
            try:
                assert(m == int(m))
                assert(n == int(n))
            except:
                print("No son números enteros")
                sys.exit()
            m = int(m)
            n = int(n)
        
            divisoresPrimosM = Obtener_divisoresPrimos(m).lista
            divisoresPrimosN = Obtener_divisoresPrimos(n).lista

            divisoresComunes = []

            for i in range(len(divisoresPrimosM)):
                primoComunBuscar = divisoresPrimosM[i][0]
        
                # Comprobar si no hay que seguir buscando
                if primoComunBuscar > divisoresPrimosN[len(divisoresPrimosN)-1][0]:
                    break
            
                for j in range(len(divisoresPrimosN)):
                    if primoComunBuscar == divisoresPrimosN[j][0]:
                        if divisoresPrimosM[i][1] <= divisoresPrimosN[j][1]:
                            divisoresComunes.append((primoComunBuscar,divisoresPrimosM[i][1]))
                        else:
                            divisoresComunes.append((primoComunBuscar,divisoresPrimosN[j][1]))
                        break

            for i in range(len(divisoresComunes)):
                mcd *= divisoresComunes[i][0]**divisoresComunes[i][1]

        self.valor = mcd

    
                                            
                                            
