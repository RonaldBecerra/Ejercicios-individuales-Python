"""
El propósito de este código es mostrar que si una lista de elementos tiene duplicados (a lo sumo uno por cada valor)
entonces es más barato hacer un ordenamiento previo para que los duplicados aparezcan contiguos y así eliminarlos
en una sola pasada, que dejar la lista desordenada y tener que comparar cada elemento con todos los siguientes para
localizar su posible duplicado.
"""


import random
from time import time
import sys

tiempoAlgoritmo1 = 0
tiempoAlgoritmo2 = 0
cantElementos = 200

def algoritmo_con_ordenamiento(lista):
    listaRetornar = []
    lista2 = lista[:]
    lista2.sort()
    length = len(lista2)

    prevNum = None
    for i in range(length):
        elem = lista2[i]
        if elem == prevNum:
            listaRetornar.append(elem)
        prevNum = elem
    return listaRetornar
    
def algoritmo_con_doble_iteracion(lista):
    listaRetornar = []
    length = len(lista)
    for i in range(length):
        elem = lista[i]
        for k in range(i+1,length):
            if elem == lista[k]:
                listaRetornar.append(elem)
    return listaRetornar
            

for i in range(100):
    numDuplicados = random.randint(0,cantElementos) # Cantidad de duplicados que tendrá la lista final
    
    # Vamos a construir la lista de números originales
    lista100mil = list(i for i in range(1,1000000))
    listaOriginales = []
    for j in range(cantElementos):
        nuevo = random.choice(lista100mil)
        listaOriginales.append(nuevo)
        lista100mil.remove(nuevo)

    # Vamos a construir la lista final
    listaFinal = listaOriginales[:]
    for j in range(numDuplicados):
        duplicado = random.choice(listaOriginales)
        listaOriginales.remove(duplicado)
        listaFinal.append(duplicado)
    random.shuffle(listaFinal)

    t1 = time()
    remover1 = algoritmo_con_ordenamiento(listaFinal)
    t2 = time()
    tiempoAlgoritmo1 += (t2 - t1)
    remover1.sort()

    t1 = time()
    remover2 = algoritmo_con_doble_iteracion(listaFinal)
    t2 = time()
    tiempoAlgoritmo2 += (t2 - t1)
    remover2.sort()

    if remover1 != remover2:
        sys.exit()


print("\n\nEl tiempo total con ordenamiento es : "+str(tiempoAlgoritmo1))
print("El tiempo total con doble iteración es : "+str(tiempoAlgoritmo2))
    



    
