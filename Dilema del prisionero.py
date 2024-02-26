import copy
from random import choice, uniform
    
def partida(jugador1, jugador2, lista_juego_acumulado):
    #print("\nNueva partida\n==========")
    accion1 = jugador1.generar_movimiento(lista_juego_acumulado, 1)
    accion2 = jugador2.generar_movimiento(lista_juego_acumulado, 0)

    #print(f"    {jugador1.nombre} juega {accion1} con puntuacion {jugador1.puntuacion}")
    #print(f"    {jugador2.nombre} juega {accion2} con puntuacion {jugador2.puntuacion}")

    suma_acciones = accion1 + accion2

    if suma_acciones == 0:
        jugador1.puntuacion += 1
        jugador2.puntuacion += 1
    elif suma_acciones == 1:
        jugador1.puntuacion += 5 * (not accion1)
        jugador2.puntuacion += 5 * (not accion2)
    else: # La suma es igual a 2
        jugador1.puntuacion += 3
        jugador2.puntuacion += 3

    #print("      Al terminar")
    #print(f"    {jugador1.nombre} queda con puntuacion {jugador1.puntuacion}")
    #print(f"    {jugador2.nombre} queda con puntuacion {jugador2.puntuacion}")

    lista_juego_acumulado.append((accion1, accion2))

def juego_entre_dos(jugador1, jugador2):
    lista_juego_acumulado = []
    jugador1.inicializar_valores()
    jugador2.inicializar_valores()
    
    for i in range(200): # Tiene que ser 200
        partida(jugador1, jugador2, lista_juego_acumulado)

def torneo(lista_jugadores):
    length = len(lista_jugadores)
    for i in range(5): # Tiene que ser 5
        for j in range(length):
            for k in range(j, length):
                # Almacenar valores anteriores
                j1, j2 = lista_jugadores[j], lista_jugadores[k]
                if j==k:
                   j2 = copy.deepcopy(j1)
                    
                puntOriginal_1, puntOriginal_2 = j1.puntuacion, j2.puntuacion
                nombre_1, nombre_2 = j1.nombre, j2.nombre

                # Realizar el juego
                juego_entre_dos(j1, j2)

                # Anotar lo que se ganó
                dif_1, dif_2 = j1.puntuacion - puntOriginal_1, j2.puntuacion - puntOriginal_2
                if j1.versusOponentes.get(nombre_2) != None:
                    j1.versusOponentes[nombre_2] += dif_1
                    j2.versusOponentes[nombre_1] += dif_2
                else:
                    j1.versusOponentes[nombre_2] = dif_1
                    j2.versusOponentes[nombre_1] = dif_2
                
    imprimir_resultados(lista_jugadores)

# Imprimir los resultados del torneo
def imprimir_resultados(lista_jugadores):
    # Ordenamos la lista de jugadores por su puntuación de mayor a menor
    lista_ordenada = sorted(lista_jugadores, key=lambda x: x.puntuacion, reverse=True)

    for elem in lista_ordenada:
        print(f"\n{elem.nombre} -- {elem.puntuacion} -- {elem.versusOponentes}")

###########################################################
##############  C R E A R   J U G A D O R E S  ############
###########################################################

lista_nombres = [
    "Azar",
    "Friedman",
    "Joss",
    "Tit for Tat",
    "Tit for Two Tat",
    "Tester",
    "Defect-all",
    "Cooperate-all"
]

# False es no cooperar
# True es cooperar
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0
        self.versusOponentes = {}

    def inicializar_valores(self):
        # La primera partida se cuenta como la 1 (impar) así que hay que cambiar el valor de esto
        # al comenzar cada partida, no al terminarla.
        self.movimientoPar = True
        
        # Cuenta cuántas veces seguidas el oponente no ha cooperado hasta la última partida
        self.seguidasOponenteNoCooperando = 0

        # Cuenta cuántas veces el oponente no ha cooperado hasta el momento
        self.oponenteNoCooperadas = 0

        # Partida en la que ocurrió la primera no cooperación del oponente
        self.primeraNoCooperacionOponente = 0

    # Como la lista de juegos acumulados guarda tuplas, cada una con el movimiento
    # de cada jugador, es necesario saber cuál de las dos posiciones de la tupla
    # corresponde al oponente
    def generar_movimiento(self, lista_juego_acumulado, posicion_oponente):
        self.movimientoPar = not self.movimientoPar
        
        # Determinamos lo último que hizo el oponente
        if lista_juego_acumulado:
            ultimo_movimiento_oponente = lista_juego_acumulado[-1][posicion_oponente]

            # Caso en que el oponente cooperó en su última jugada
            if ultimo_movimiento_oponente:
                self.seguidasOponenteNoCooperando = 0

            # Caso en que el oponente no cooperó en su última jugada
            else:
                self.seguidasOponenteNoCooperando += 1
                self.oponenteNoCooperadas += 1

                if self.primeraNoCooperacionOponente == 0:
                    self.primeraNoCooperacionOponente = len(lista_juego_acumulado)
                
        # Generamos el movimiento correspondiente       
        if self.nombre == lista_nombres[0]:
            return self.azar()
        elif self.nombre == lista_nombres[1]:
            return self.friedman()
        elif self.nombre == lista_nombres[2]:
            return self.joss(lista_juego_acumulado)
        elif self.nombre == lista_nombres[3]:
            return self.tit_for_tat(lista_juego_acumulado)
        elif self.nombre == lista_nombres[4]:
            return self.tit_for_two_tat(lista_juego_acumulado)
        elif self.nombre == lista_nombres[5]:
            return self.tester(lista_juego_acumulado)
        elif self.nombre == lista_nombres[6]:
            return self.defect_all()
        elif self.nombre == lista_nombres[7]:
            return self.cooperate_all()

    # Auxiliar para algunas estrategias. Copia la última jugada del oponente
    def aux_copiar_ultimo_oponente(self):
        if self.seguidasOponenteNoCooperando == 0:
            return True
        return False

    # Elige el 50% de las veces cooperar o no cooperar
    def azar(self):
        return choice([False,True])

    # Guarda rencor para siempre. También conocida como Grim
    def friedman(self):
        if self.oponenteNoCooperadas > 0:
            return False
        return True

    # Comienza cooperando. Luego copia el último movimiento del oponente, pero
    # alrededor del 10% de las veces se hace el listo y no coopera
    def joss(self, lista_juego_acumulado):
        # En la primera partida, siempre cooperar
        if not lista_juego_acumulado:
            return True

        # 1) Hacerse el listo
        if uniform(0,1) < 0.1:
            #print("-----> Se hace el listo")
            return False
        
        # 2) Copiar el último movimiento del oponente
        return self.aux_copiar_ultimo_oponente()

    # Comienza cooperando. Luego copia el último movimiento del oponente
    def tit_for_tat(self, lista_juego_acumulado):
        # En la primera partida, siempre cooperar
        if not lista_juego_acumulado:
            return True
        
        # En el resto, copiar el último movimiento del oponente
        return self.aux_copiar_ultimo_oponente()  

    # Comienza cooperando. Luego solo deja de cooperar si el
    # oponente ha dejado de cooperar dos veces seguidas
    def tit_for_two_tat(self, lista_juego_acumulado):
        # En la primera partida, siempre cooperar
        if not lista_juego_acumulado:
            return True

        # Si el oponenente no ha dejado de cooperar 2 o más veces seguidas, cooperar
        if self.seguidasOponenteNoCooperando < 2:
            return True
        return False

    # En cada movimiento impar, intenta no cooperar.
    # Pero si el oponente alguna vez no cooperó, juega al tit for tat por el resto del juego.
    # Y jugar a tit for tat significa que la primera vez que lo hace, empieza cooperando.
    def tester(self, lista_juego_acumulado):
        # Si el oponente contraatacó, se disculpa y juega a tit for tat por el resto del juego
        if self.primeraNoCooperacionOponente > 0:
            return self.tit_for_tat(lista_juego_acumulado[self.primeraNoCooperacionOponente:])

        if self.movimientoPar:
            return True

        # En cada movimiento impar, intenta no cooperar. Esto incluye la primera partida
        return False

    # Nunca cooperar
    def defect_all(self):
        return False

    # Siempre cooperar
    def cooperate_all(self):
        return True

def main():
    lista_nombres = [
        "Azar",
        "Friedman",
        "Joss",
        "Tit for Tat",
        "Tit for Two Tat",
        "Tester",
        "Defect-all",
        "Cooperate-all"
    ]
    lista_jugadores = []
    for nombre in lista_nombres:
        lista_jugadores.append(Jugador(nombre))

    torneo(lista_jugadores)

if __name__ == '__main__':
    main()






