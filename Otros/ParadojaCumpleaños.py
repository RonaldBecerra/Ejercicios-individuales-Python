# Paradoja del cumpleaños
from random import choice
from random import shuffle

listaDias = list(i for i in range(1,366))

total = 0
intentos = 1000000
numPersonas = 23

for i in range(intentos):
    l = []
    contar = False
    for k in range(numPersonas):
        c = choice(listaDias)
        if c not in l:
            l.append(c)
        else:
            contar = True
            break
    if contar:
        total += 1

print(str(total*100/intentos)+"%")
