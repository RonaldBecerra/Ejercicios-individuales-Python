#
# Archivo: primos.py
#
# Descripción: Programa que contiene dos clases:

#   1) Dado un entero, devuelve la lista con los primos menores o iguales a él.
#   2) Dado un entero, devuelve su descomposición en factores primos.
#
# Fecha de creación: 01/10/2017
# Última modificación: 23/11/2017

class varGlobal:
    primero = None
    listaPrimosTotales = [2,3,5,7,11,13,17,19]
    cantGuardados = 8
    maximoPrimoGuardado = 19

varGlobal = varGlobal()

def hallar_primosN(n):
    """
    Entrada
        * n: número entero positivo. 
    Salida
        * listaPrimos: lista de todos los primos que hay desde 2 hasta n. """

    if varGlobal.maximoPrimoGuardado == n:
        return varGlobal.listaPrimosTotales
    elif varGlobal.maximoPrimoGuardado > n:
        alias = varGlobal.listaPrimosTotales
        retornar = alias[:]
        long = len(alias)
        removidos = 0
        for i in range(long-1):
            if alias[long-1-i] > n:
                retornar.remove(retornar[long-1-removidos])
                removidos += 1
            else:
                break
        return retornar
    else:
        minimo = varGlobal.maximoPrimoGuardado + 1
        for i in range(minimo,n+1):
            insertar = True
            j = 0
            while j < varGlobal.cantGuardados:
                if i %varGlobal.listaPrimosTotales[j] == 0:
                    insertar = False
                    break
                j += 1
            if insertar:
                varGlobal.listaPrimosTotales.append(i)
                varGlobal.maximoPrimoGuardado = i
                varGlobal.cantGuardados += 1
        return varGlobal.listaPrimosTotales

"""def obtener_divisoresPrimosAnt(n,listaPrimos = None):
    "
    Entrada
        * n: número al que se le quieren hallar los factores primos.
        * listaPrimos: lista de todos los primos que hay desde 2 hasta n.
           (opcional)
    Salida
        * listaDivisores: lista de los factores primos de N,
            (opcional)    con sus multiplicidades. "

    if n == 0:
        return []
    if listaPrimos == None:
        listaPrimos = hallar_primosN(n)
    listaDivisores = []
    res = n
    acumulado = 1
    for i in range(len(listaPrimos)):
        primo = listaPrimos[i]
        multiplicidad = 0
        while res%primo == 0:
            multiplicidad +=1
            res = res/primo
            res = int(res)
        if multiplicidad != 0:
            listaDivisores.append((primo,multiplicidad))
            acumulado *= primo**multiplicidad
            if acumulado == n:
                break
    return listaDivisores """

def obtener_divisoresPrimos(n):
    """
    Entrada
        * n: número al que se le quieren hallar los factores primos.
    Salida
        * listaDivisores: lista de los factores primos de N,
            (opcional)    con sus multiplicidades. """

    if n == 0:
        return []
    listaDivisores = []
    res = n
    acumulado = 1
    ap = 0
    ultimo = varGlobal.maximoPrimoGuardado
    while acumulado != n:
        if ap >= varGlobal.cantGuardados:
            ultimo += 100
            hallar_primosN(ultimo)
        primo = varGlobal.listaPrimosTotales[ap]
        multiplicidad = 0
        while res%primo == 0:
            multiplicidad +=1
            res = res//primo
            res = int(res)
        if multiplicidad != 0:
            listaDivisores.append((primo,multiplicidad))
            acumulado *= primo**multiplicidad
        ap += 1
        
    return listaDivisores

class nodoListaPrimos:
    def __init__(self,valor):
        self.valor = valor
        self.listaPrimos = None
        self.anterior = None
        self.siguiente = None

def buscarAgregarListaPrimos(numero):
    if varGlobal.primero == None:
        nodo = nodoListaPrimos(numero)
        nodo.listaPrimos = obtener_divisoresPrimos(numero)
        varGlobal.primero = nodo
        return nodo.listaPrimos
    nodoActual = varGlobal.primero
    if numero < nodoActual.valor:
        nodo = nodoListaPrimos(numero)
        nodo.listaPrimos = obtener_divisoresPrimos(numero)
        varGlobal.primero = nodo
        nodo.siguiente = nodoActual
        nodoActual.anterior = nodo
        return nodo.listaPrimos
    elif numero == nodoActual.valor:
        return nodoActual.listaPrimos
    else:
        while nodoActual.siguiente != None:
            nodoSiguiente = nodoActual.siguiente
            if (nodoActual.valor < numero) and (numero < nodoSiguiente.valor):
                nodo = nodoListaPrimos(numero)
                nodo.listaPrimos = obtener_divisoresPrimos(numero)
                nodoActual.siguiente = nodo
                nodo.anterior = nodoActual
                nodo.siguiente = nodoSiguiente
                nodoSiguiente.anterior = nodo
                return nodo.listaPrimos
            if numero == nodoSiguiente.valor:
                return nodoSiguiente.listaPrimos
            nodoActual = nodoSiguiente
        nodo = nodoListaPrimos(numero)
        nodo.listaPrimos = obtener_divisoresPrimos(numero)
        nodoActual.siguiente = nodo
        nodo.anterior = nodoActual
        return nodo.listaPrimos

from time import time
def hacer(n):
    ini = time()
    lista = obtener_divisoresPrimos(n)
    fin = time()
    print(fin-ini)
    
    
