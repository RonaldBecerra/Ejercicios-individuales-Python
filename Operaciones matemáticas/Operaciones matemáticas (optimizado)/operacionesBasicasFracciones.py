#
# Archivo: operacionesBasicasFracciones.py
#
# Descripción: Archivo que contiene las funciones auxiliares necesarias para
#              luego operar dos o más fracciones sin tener que utilizar números
#              en punto flotante.
#
# Fecha: 23/11/2017

from maximoComunDivisor import *
from minimoComunMultiplo import * 

class fraccion():
    def __init__(self,numerador=None,denominador=1):
        self.numerador = numerador
        self.denominador = denominador

def sumar(frac1,frac2):
    num1 = frac1.numerador
    num2 = frac2.numerador
    den1 = frac1.denominador
    den2 = frac2.denominador

    denGen = minimoComunMultiplo(den1,den2,buscarAgregarListaPrimos(den1),buscarAgregarListaPrimos(den2))
    numGen = denGen//den1 *num1 + denGen//den2 *num2

    div = maximoComunDivisor(denGen,numGen)
    denGen = denGen//div
    numGen = numGen//div

    return fraccion(numGen,denGen)

def multiplicar(frac1,frac2):
    num1 = frac1.numerador
    num2 = frac2.numerador
    den1 = frac1.denominador
    den2 = frac2.denominador

    denGen = den1 * den2
    numGen = num1 * num2

    div = maximoComunDivisor(denGen,numGen)
    denGen = denGen//div
    numGen = numGen//div

    return fraccion(numGen, denGen)

def dividir(frac1,frac2):
    num1 = frac1.numerador
    num2 = frac2.numerador
    den1 = frac1.denominador
    den2 = frac2.denominador

    numGen = num1 * den2
    denGen = den1 * num2

    div = maximoComunDivisor(denGen,numGen)
    denGen = denGen//div
    numGen = numGen//div

    return fraccion(numGen, denGen)

def operar(listaFracciones,listaOperadores):
    """
    Entrada
        * listaFracciones: lista con las fracciones que se quieren operar
        * listaOperadores: lista con los operadores que se quieren aplicar sobre
                           las fracciones, considerando que el primer operador
                           actúa sobre la primera y segunda; el segundo sobre ese 
                           resultado y la tercera, etc.
    Salida
        * fraccionDevolver: fracción (clase con argumentos "numerador" y "denominador"),
                            resultado de aplicar todas las operaciones. """
    
    listaOperadoresNueva = listaOperadores[:]
    listaFraccionesNueva = listaFracciones[:]

    fraccionDevolver = listaFraccionesNueva[0]
    listaFraccionesNueva.remove(listaFraccionesNueva[0])

    if listaOperadores == []:
        return fraccionDevolver
    
    else:
        while (listaOperadoresNueva[0] != "+") and (listaOperadoresNueva[0] != "-"):
            if listaOperadoresNueva[0] == "*":
                fraccionDevolver = multiplicar(fraccionDevolver,listaFraccionesNueva[0])
            elif listaOperadoresNueva[0] == ":":
                fraccionDevolver = dividir(fraccionDevolver,listaFraccionesNueva[0])
            listaFraccionesNueva.remove(listaFraccionesNueva[0])
            listaOperadoresNueva.remove(listaOperadoresNueva[0])

            if listaOperadoresNueva == []:
                break
            
        if listaOperadoresNueva != []:
            if listaOperadoresNueva[0] == "+":
                listaOperadoresNueva.remove(listaOperadoresNueva[0])
                fraccionDevolver = sumar(fraccionDevolver,operar(listaFraccionesNueva,listaOperadoresNueva))
            elif listaOperadoresNueva[0] == "-":
                listaOperadoresNueva.remove(listaOperadoresNueva[0])
                listaFraccionesNueva[0].numerador *= -1
                fraccionDevolver = sumar(fraccionDevolver,operar(listaFraccionesNueva,listaOperadoresNueva))
    return fraccionDevolver
