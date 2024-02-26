from random import choice

def dado():
    A = [1,2,3,4,5,6]
    return choice(A)

colores = ["Verde", "Morado", "Amarillo", "Rojo", "Azul", "Anaranjado"]

class casilla:
    def __init__(self,anterior=None,siguiente=None,color = None):
        self.anterior = anterior
        self.siguiente = siguiente
        self.inicio = False # Determina si es el punto de partida de algún color
        self.final = False  # Determina si es el final del recorrido de casillas comunes de algún color (no contando la parte interna de una casa)
        self.color = color  # Determina de cuál color esta casilla es inicio o final
        


