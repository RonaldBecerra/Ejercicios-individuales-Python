"""
ENTENDER LA INTUICIÓN DE
https://mathoverflow.net/questions/9037/how-is-it-that-you-can-guess-if-one-of-a-pair-of-random-numbers-is-larger-with

Resulta que si te dan dos sobres, cada uno conteniendo un número entero, uno mayor que el otro, si sabes el contenido
de un sobre, aparentemente hay una manera de acertar si el otro número es mayor o menor que el ya visto con probabilidad
mayor que 1/2
"""

from random import choice
numerosPosibles = list(i for i in range(-1000000,1000001))

class globales:
    aciertos = 0

globales = globales()

def jugar():
    # Obtener los valores de los dos sobres, donde x es el valor del primero (el que se puede ver), y "y" es el valor del que sigue oculto
    x = choice(numerosPosibles)
    while True:
        y = choice(numerosPosibles)
        if x != y:
            break
    

    # Obtener el valor de r, que es lo que definirá nuestra decisión junto con el valor de x
    r = choice(numerosPosibles)

    # Cuando r es menor o igual a x, se supone que uno debe apostar por que "y" es menor que x
    if (r <= x):
        if x > y:
            globales.aciertos += 1
    else: # Cuando r es mayor que x, se supone que uno debe apostar por que "y" es mayor que x
        if y > x:
            globales.aciertos += 1

numIteraciones = 1000000
for i in range(numIteraciones):
    jugar()

print("La probabilidad es "+str(globales.aciertos/numIteraciones))
    
        
