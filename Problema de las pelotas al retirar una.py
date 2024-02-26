from random import choice, uniform
from math import floor

NUM_BALLS = 100
ITERATIONS = 10000000

def juego(NUM_BALLS):
    # Cantidad de bolas rojas
    n = floor(uniform(0,NUM_BALLS+1))

    # Caja con las pelotas
    #   0: rojo
    #   1: verde
    box = [0] * n + [1] * (NUM_BALLS - n)

    # Escoger una pelota de la caja
    taken_ball = choice(box)

    # Si la pelota tomada es roja
    #if taken_ball == 0:
    return sum(box[i] == 0 for i in range(NUM_BALLS)) - 1
    
    # Si la pelota tomada es verde, el juego no es válido
    return None

def main(NUM_BALLS, ITERATIONS):  
    average_prob = 0
    i = 0
    while i < ITERATIONS:
        amount_red = juego(NUM_BALLS)
        if amount_red != None:
            average_prob += amount_red
            i += 1
    average_prob = average_prob / ((NUM_BALLS-1) * ITERATIONS)
    print(average_prob)

main(NUM_BALLS, ITERATIONS)
            
        

    

    


    

