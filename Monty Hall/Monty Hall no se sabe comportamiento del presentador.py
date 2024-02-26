"""
Aquí intentaremos ver qué pasa si existen estos posibles comportamientos del presentador:

0) El presentador sólo revela la cabra cuando el jugador ha escogido cabra.
1) El presentador sólo revela la cabra cuando el jugador ha escogido auto.
2) El presentador siempre revela una cabra.
3) El presentador siempre revela una cabra de la puerta de menor numeración de las que el concursante no eligió. Si ahí no hay cabra, no revela nada.
4) El presentador siempre revela una cabra de la puerta de mayor numeración de las que el concursante no eligió, Si ahí no hay cabra, no revela nada.

entonces la probabilidad de ganar al cambiar ya no es 2/3 sino 5/9
"""

from random import choice   # "choice" es una función predeterminada para elegir un valor aleatorio de una lista.
from random import shuffle  # "shuffle" es una función predeterinada para barajar los contenidos de una lista.

class globales:
    NUM_REPETICIONES = 5000000
    numVecesSePuedeCambiar = 0
    numGanadasCambiando = 0 

globales = globales()


def jugarCambiando(conjunto, comportamiento):
    shuffle(conjunto) # Barajar contenidos
    numerosPuertas = [0,1,2] 
    eleccionInicial = choice(numerosPuertas)
    numerosPuertas.remove(eleccionInicial) 

    sePuedeCambiar = True # Determina si al final se puede cambiar de elección o no.

    # Caso en el que la revelación sólo se intenta hacer en la puerta de menor numeración de las que no ha elegido el concursante.
    if (comportamiento == 3):
        if (conjunto[numerosPuertas[0]] == 'Cabra'):
            numerosPuertas.remove(numerosPuertas[0])
        else:
            sePuedeCambiar = False
    # Caso en el que la revelación sólo se intenta hacer en la puerta de mayor numeración de las que no ha elegido el concursante.
    elif (comportamiento == 4):
        if (conjunto[numerosPuertas[1]] == 'Cabra'):
            numerosPuertas.remove(numerosPuertas[1])
        else:
            sePuedeCambiar = False
    # Caso en que el jugador ha elegido la puerta correcta
    elif conjunto[eleccionInicial] == 'Auto':    
        if (comportamiento == 1) or (comportamiento == 2):
            puertaRevelada = choice(numerosPuertas)                   
            numerosPuertas.remove(puertaRevelada)   
        elif comportamiento == 0: 
            sePuedeCambiar = False
    # Caso en que el jugador escogió una puerta con cabra. Eso significa que las otras dos puertas tiene un Auto y una Cabra.
    else:
        # Comportamiento en el que el presentador no hace la revelación.
        if (comportamiento == 1):
            sePuedeCambiar = False
        elif (comportamiento == 0) or (comportamiento == 2):
            # Ahora tenemos que determinar cuál de las dos puertas restantes es la que tiene cabra, para que el presentador la revele
            if conjunto[numerosPuertas[0]] == 'Cabra':                                       
                numerosPuertas.remove(numerosPuertas[0]) 
            else:
                numerosPuertas.remove(numerosPuertas[1])  

    if sePuedeCambiar:
        globales.numVecesSePuedeCambiar += 1
        eleccionFinal = numerosPuertas[0] 

        if conjunto[eleccionFinal] == 'Auto':
            globales.numGanadasCambiando +=1  

    # No nos interesa contabilizar cuando no se puede cambiar, porque lo que queremos ver aquí es la proporción de veces que se
    # gana cuando efectivamente está la oportunidad de cambiar.

# Hacer las iteraciones y sacar la probabilidad
def jugar():
    contenidos = ['Auto','Cabra','Cabra']   # Ésta es la lista de puertas con sus contenidos. En este momento, el carro está en la puerta 1.
    
    while (globales.numVecesSePuedeCambiar < globales.NUM_REPETICIONES):
        numerosComportamientos = [2,3,4]
        comportamientoPresentador = choice(numerosComportamientos)
        jugarCambiando(contenidos, comportamientoPresentador)

    probabilidad = globales.numGanadasCambiando/globales.numVecesSePuedeCambiar
    print("La probabilidad de acertar cambiando para la modalidad escogida es: "+str(probabilidad))

    globales.numVecesSePuedeCambiar = 0
    globales.numGanadasCambiando = 0 


jugar()






        
        
