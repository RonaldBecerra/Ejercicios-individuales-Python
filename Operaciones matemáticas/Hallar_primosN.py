#
# Archivo: Hallar_primosN.py
#
# Descripción: Programa que dado un número N, devuelve una lista de
#              todos los números primos que hay desde 2 hasta N.
#              Se invoca llamando "Hallar_primosN(n).lista"
#
# Fecha de creación: 01/10/2017

class Hallar_primosN():
    def __init__(self,n):      
        if n < 2:
            listaPrimos = []
        elif n == 2:
            listaPrimos = [2]
        else:
            listaPrimos = [2]
            for i in range(2,n+1):
                insertar = True
                for j in range(len(listaPrimos)):
                    if i%listaPrimos[j] == 0:
                        insertar = False
                        break
                if insertar:
                    listaPrimos.append(i)
        self.lista = listaPrimos
