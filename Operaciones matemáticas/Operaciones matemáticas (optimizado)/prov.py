from operacionesBasicasFracciones import *
from time import time


for n in range(1,20):
    fraccionTotal = fraccion(0,1)
    for a in range(1,n):
        for b in range(a+1,n+1):
            if a+b > n:
                if maximoComunDivisor(a,b) == 1:
                    fraccionNueva = fraccion(1,a*b)
                    fraccionTotal = sumar(fraccionNueva,fraccionTotal)
    x = fraccionTotal.numerador
    y = fraccionTotal.denominador
    print("n = "+str(n)+", suma = "+str(x)+"/"+str(y)+" = "+str(x/y))

"""
lista =[fraccion(203,456),fraccion(564,256),fraccion(746,918),fraccion(567,876),fraccion(156,594)]

tiempo_inicial = time()
fraccionTotal = fraccion(0,1)                
for i in range(len(lista)):
    fraccionTotal = sumar(fraccionTotal,lista[i])
    print("´", end = " ")
tiempo_final = time()

print(tiempo_final - tiempo_inicial)

tiempo_inicial = time()
fraccionTotal = fraccion(0,1)                
for i in range(len(lista)):
    fraccionTotal = sumar(fraccionTotal,lista[i])
tiempo_final = time()

print(tiempo_final - tiempo_inicial)
"""
    




