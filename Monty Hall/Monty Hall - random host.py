from random import choice
from random import shuffle
conjunto = ['Premio','Vacío','Vacío']

# El que siempre se cambia
def jugar1(conjunto):
    conjuntoOriginal = conjunto[:]
    shuffle(conjunto)
    numeros = [0,1,2]
    eleccionInicial = choice(numeros)  # Elección del concursante
    numeros.remove(eleccionInicial)    # Para no volver a elegir la puerta de al principio
    azar = choice(numeros)             # Eleccion del presentador
    
    if conjunto[azar] == 'Premio':
        return jugar1(conjuntoOriginal) # No vale el juego si el presentador abre el premio
    else:
        numeros.remove(azar) # Para no volver a elegir la puerta que abrió el presentador
        eleccionFinal = conjunto[numeros[0]]
        if eleccionFinal == 'Premio':
            return True
        else:
            return False

# El que siempre mantiene la elección inicial
def jugar2(conjunto):
    conjuntoOriginal = conjunto[:]
    shuffle(conjunto)
    numeros = [0,1,2]
    eleccionInicial = choice(numeros)  # Elección del concursante
    numeros.remove(eleccionInicial)    # Para no volver a elegir la puerta de al principio
    azar = choice(numeros)             # Elección del presentador
    
    if conjunto[azar] == 'Premio':
        return jugar1(conjuntoOriginal) # No vale el juego si el presentador abre el premio
    else:
        eleccionFinal = conjunto[eleccionInicial]
        if eleccionFinal == 'Premio':
            return True
        else:
            return False

sumaCambia = 0
sumaNoCambia = 0

for i in range(0,100000):
    if jugar1(conjunto):
        sumaCambia +=1
    if jugar2(conjunto):
        sumaNoCambia +=1

proba1 = sumaCambia/100000
proba2 = sumaNoCambia/100000

print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
        
        
