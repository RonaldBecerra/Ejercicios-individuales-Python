from random import choice
from random import shuffle
conjunto = ['Premio','Vacío','Vacío']

class globales:
    sumaCambia = 0
    sumaNoCambia = 0

globales = globales()

# El que siempre se cambia
def jugar1(conjunto):
    shuffle(conjunto)
    numeros = [0,1,2]
    eleccionInicial = choice(numeros)  # Elección del concursante
    numeros.remove(eleccionInicial)
    if conjunto[eleccionInicial] == 'Premio':
        azar = choice(numeros)
        numeros.remove(azar) # El presentador abre una puerta vacía

    else:
        if conjunto[numeros[0]] == 'Vacío':
            numeros.remove(numeros[0])
        else:
            numeros.remove(numeros[1])

    eleccionFinal = conjunto[numeros[0]]
    if eleccionFinal == 'Premio':
        globales.sumaCambia +=1


# El que siempre mantiene la elección inicial
def jugar2(conjunto):
    shuffle(conjunto)
    eleccionFinal = choice(conjunto)
    if eleccionFinal == 'Premio':
        globales.sumaNoCambia +=1



print("            10 INTENTOS")
print("            -----------")
print("")
        
for j in range(0,10):
    for i in range(0,10):
        jugar1(conjunto)
        jugar2(conjunto)
    proba1 = globales.sumaCambia/10
    proba2 = globales.sumaNoCambia/10
    print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
    print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
    print("10 intentos")
    print("")
    globales.sumaCambia = 0
    globales.sumaNoCambia = 0
    
print("")
print("            100 INTENTOS")
print("            ------------")
print("")

for j in range(0,10):
    for i in range(0,100):
        jugar1(conjunto)
        jugar2(conjunto)
    proba1 = globales.sumaCambia/100
    proba2 = globales.sumaNoCambia/100
    print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
    print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
    print("100 intentos")
    print("")
    globales.sumaCambia = 0
    globales.sumaNoCambia = 0
    
print("")
print("            1000 INTENTOS")
print("            -------------")
print("")

for j in range(0,10):
    for i in range(0,1000):
        jugar1(conjunto)
        jugar2(conjunto)
    proba1 = globales.sumaCambia/1000
    proba2 = globales.sumaNoCambia/1000
    print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
    print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
    print("1000 intentos")
    print("")
    globales.sumaCambia = 0
    globales.sumaNoCambia = 0

print("")
print("            10000 INTENTOS")
print("            --------------")
print("")

for j in range(0,10):
    for i in range(0,10000):
        jugar1(conjunto)
        jugar2(conjunto)
    proba1 = globales.sumaCambia/10000
    proba2 = globales.sumaNoCambia/10000
    print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
    print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
    print("10000 intentos")
    print("")
    globales.sumaCambia = 0
    globales.sumaNoCambia = 0

print("")
print("            100000 INTENTOS")
print("            ---------------")
print("")

for j in range(0,10):
    for i in range(0,100000):
        jugar1(conjunto)
        jugar2(conjunto)      
    proba1 = globales.sumaCambia/100000
    proba2 = globales.sumaNoCambia/100000
    print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
    print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
    print("100000 intentos")
    print("")
    globales.sumaCambia = 0
    globales.sumaNoCambia = 0

print("")
print("            1000000 INTENTOS")
print("            ----------------")
print("")

for j in range(0,10):
    for i in range(0,1000000):
        jugar1(conjunto)
        jugar2(conjunto)
    proba1 = globales.sumaCambia/1000000
    proba2 = globales.sumaNoCambia/1000000
    print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
    print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))
    print("1000000 intentos")
    print("")
    globales.sumaCambia = 0
    globales.sumaNoCambia = 0

"""

for i in range(0,3):
    jugar1(conjunto)
    jugar2(conjunto)

proba1 = globales.sumaCambia/3
proba2 = globales.sumaNoCambia/3
print("La probabilidad de acertar si siempre se cambia es: "+str(proba1))
print("La probabilidad de acertar si nunca se cambia es: "+str(proba2))

"""


        
        
