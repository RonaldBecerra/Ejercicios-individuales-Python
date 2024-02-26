from MaximoComunDivisor import *
from MinimoComunMultiplo import *

class fraccion():
    def __init__(self,numerador=None,denominador=1):
        self.numerador = numerador
        self.denominador = denominador

def sumar(frac1,frac2):
    num1 = frac1.numerador
    num2 = frac2.numerador
    den1 = frac1.denominador
    den2 = frac2.denominador

    denGen = MinimoComunMultiplo(den1,den2).valor
    numGen = int(denGen/den1 *num1 + denGen/den2 *num2)

    div = MaximoComunDivisor(denGen,numGen).valor
    denGen = int(denGen/div)
    numGen = int(numGen/div)

    return fraccion(numGen,denGen)

class lista:
    casos = []
lista = lista()
for n in range(1,51):
    print("")
    print("n = "+str(n))
    print("----------")
    cont = 0
    nuevo = [n,0,[]]
    for a in range(1,n):
        for b in range(a+1,n+1):
            if a+b > n:
                if MaximoComunDivisor(a,b).valor == 1:
                    cont += 1
                    nuevo[2].append((a,b))
                    print("("+str(a)+","+str(b)+")")
    nuevo[1] = cont
    lista.casos.append(nuevo)

"""for elem in lista.casos:
    fraccionAcumulada = fraccion(0,1)
    for par in range(elem[1]):
        parOrdenado = elem[2][par]
        fraccionNueva = fraccion(1,parOrdenado[0]*parOrdenado[1])
        fraccionAcumulada = sumar(fraccionAcumulada,fraccionNueva)
    (num,den) = (fraccionAcumulada.numerador, fraccionAcumulada.denominador)
    print("n = "+str(elem[0])+",  fracción = "+str(num)+"/"+str(den))"""
                                 


