#
# Archivo: La vieja.py
#
# Descripción: Programa que permite jugar contra la máquina el juego de la vieja,
#              permitiéndole al jugador decidir si va a ser el primero o el
#              segundo.
#
# Motivo: Quiero descubrir una estrategia que haga que la máquina sea invencible.
#         La manera es evaluando los grupos de tres que se pueden hacer (caminos),
#         y los valores correspondientes a cada casilla, dependiendo de cuántos 
#         caminos gana un jugador marcándolos y cuántos les bloquea a su adversa-
#         rio.
#
# Fecha: 08/12/2016

import sys


################################################################################
###############  E S T R U C T U R A S   A U X I L I A R E S  ##################
################################################################################

""" Estructura un nodo de una lista """
class nodo():

    def __init__(self):
        self.elemento  = None  # Elemento que constiruye el nodo
        self.anterior  = None  # Anterior en la lista a este nodo
        self.siguiente = None  # Siguiente en la lista a este nodo

""" Estructura de una lista, que puede ser de caminos o de casillas """
class lista():

     def __init__(self):
         self.primero = None
         self.ultimo  = None

     def buscar(self, elementoBuscar): # Debe recibir el identificador, no el elemento ni el nodo
         nodoActual = self.primero 
         if nodoActual == None:
             return False, None
         while nodoActual.elemento.identificador != elementoBuscar:
             nodoActual = nodoActual.siguiente
             if nodoActual == None:
                 return False, None
         return True, nodoActual  # Retorna el nodo del elemento que se está buscando

     def eliminar(self, elementoEliminar): # Debe recibir un identificador, no el elemento ni el nodo
         nodoEliminar = self.buscar(elementoEliminar)[1] 
         if nodoEliminar == self.primero:
             if nodoEliminar == self.ultimo:
                 self.primero = None
                 self.ultimo  = None
             else:
                 self.primero = nodoEliminar.siguiente
                 self.primero.anterior = None
         elif nodoEliminar == self.ultimo:
             self.ultimo = nodoEliminar.anterior
             self.ultimo.siguiente = None
         else:
             nodoEliminar.anterior.siguiente = nodoEliminar.siguiente
             nodoEliminar.siguiente.anterior = nodoEliminar.anterior

     def insertar(self, elementoInsertar): # Debe recibir el elemento en sí, no su identificador
                                           # ni el nodo que lo contiene
         nodoInsertar = nodo()
         nodoInsertar.elemento = elementoInsertar
         if self.primero == None:
             self.primero = nodoInsertar
             self.ultimo  = nodoInsertar
         else:
             self.ultimo.siguiente = nodoInsertar
             nodoInsertar.anterior = self.ultimo
             self.ultimo = nodoInsertar
             
""" Estructura de una casilla del tablero """
class casilla(object):

    def __init__(self, identificador):
        self.identificador = identificador # Letra que establece cuál casilla es
        self.listaCaminos  = lista() # Lista de caminos disponibles a los cuales 
                                   # pertenece
        self.dueño         = None
        self.ocupada       = False # Determina si el nodo ya ha sido ocupado

""" Camino de tres nodos mediante el cual un jugador gana la partida al comple-
tarlo """
class camino():

    def __init__(self, identificador, casilla1, casilla2, casilla3):
        self.identificador = identificador # Permite saber qué camino es
        self.casilla1      = casilla1 # Apuntador al primer nodo que lo constituye
        self.casilla2      = casilla2 # Apuntador al segundo nodo que lo constituye
        self.casilla3      = casilla3 # Apuntador al tercer nodo que lo constituye
        self.dueño         = None # Apuntador al jugador que tiene posibilidad de
                                  # completarlo ("jug1" o "jug2")
        self.disponible    = True # Indica si el camino todavía puede ser completado

    def cant_ocupados(self):
        ocupados = 0
        if self.casilla1.dueño != None: # Determinar si el nodo está ocupado por 
                                        # algún jugador
            ocupados += 1
        if self.casilla2.dueño != None:
            ocupados += 1
        if self.casilla3.dueño != None:
            ocupados += 1
        return ocupados 

# Función para traspasar un nodo de una lista a otra
def traspasar(objeto, lista_origen, lista_destino):
    lista_origen.eliminar(objeto.elemento.identificador)
    lista_destino.insertar(objeto.elemento)

# Función para imprimir una casilla
def imprimir_casilla(casilla):
    if casilla.ocupada == False:
        print("_", end="")
    elif casilla.dueño.numJugador == 1:
        print("O", end="")
    else:
        print("X", end="")

# Función para imprimir el tablero después de una jugada
def imprimir_tablero(a,b,c,d,e,f,g,h,i):
    imprimir_casilla(a)
    print(" ", end="")
    imprimir_casilla(b)
    print(" ", end="")
    imprimir_casilla(c)
    print("")
    imprimir_casilla(d)
    print(" ", end="")
    imprimir_casilla(e)
    print(" ", end="")
    imprimir_casilla(f)
    print("")
    imprimir_casilla(g)
    print(" ", end="")
    imprimir_casilla(h)
    print(" ", end="")
    imprimir_casilla(i)
    print("")
    print("")    

# Estructura de un jugador
class jugador():

    def __init__(self, numJugador, tipoJugador):
        self.numJugador  = numJugador  # Determina si es el primero o el segundo
        self.tipoJugador = tipoJugador # Determina si es una persona ("P") o la 
                                       # máquina ("M")
        self.listaCaminos = [lista(),lista()]  
        # Lista de caminos disponibles en los que el jugador ha ocupado una 
        # casilla y dos casillas, respectivamente.

# Subrutina que ejecuta la mejor jugada para el jugador actual
def juegaMáquina(numJugador):
    pass # Retorna la casilla que se seleccionó

# Función para imprimir el mensaje final según se haya ganado o no
def mensaje_final(jugador1, jugador2, jugadorGanador=None):
    if jugadorGanador != None:
        if (jugador1.tipoJugador == "P" and jugador2.tipoJugador == "M") or \
(jugador1.tipoJugador == "M" and jugador2.tipoJugador == "P"):
            if jugadorGanador.tipoJugador == "P":
                print("¡Felicitaciones, usted ha ganado!")
            else:
                print("Lo sentimos, usted ha perdido.")
        elif (jugador1.tipoJugador == "P" and jugador2.tipoJugador == "P"):
            print("Ganó el jugador "+str(jugadorGanador.numJugador))
    else:
        print("Ganó la vieja")
    sys.exit()
                                       
################################################################################
###################  I N I C I A L I Z A R   J U E G O  ########################
################################################################################

# Inicializar casillas y sus identificadores
casilla_a = casilla("a")
casilla_b = casilla("b")
casilla_c = casilla("c")
casilla_d = casilla("d")
casilla_e = casilla("e")
casilla_f = casilla("f")
casilla_g = casilla("g")
casilla_h = casilla("h")
casilla_i = casilla("i")

# Inicializar los caminos
camino_1 = camino(1, casilla_a, casilla_b, casilla_c)
camino_2 = camino(2, casilla_a, casilla_e, casilla_i)
camino_3 = camino(3, casilla_a, casilla_d, casilla_g)
camino_4 = camino(4, casilla_b, casilla_e, casilla_h)
camino_5 = camino(5, casilla_c, casilla_e, casilla_g)
camino_6 = camino(6, casilla_c, casilla_f, casilla_i)
camino_7 = camino(7, casilla_d, casilla_e, casilla_f)
camino_8 = camino(8, casilla_g, casilla_h, casilla_i)

# Inicializar las listas de caminos de las casillas
casilla_a.listaCaminos.insertar(camino_1)
casilla_a.listaCaminos.insertar(camino_2)
casilla_a.listaCaminos.insertar(camino_3)

casilla_b.listaCaminos.insertar(camino_1)
casilla_b.listaCaminos.insertar(camino_4)

casilla_c.listaCaminos.insertar(camino_1)
casilla_c.listaCaminos.insertar(camino_5)
casilla_c.listaCaminos.insertar(camino_6)

casilla_d.listaCaminos.insertar(camino_3)
casilla_d.listaCaminos.insertar(camino_7)

casilla_e.listaCaminos.insertar(camino_2)
casilla_e.listaCaminos.insertar(camino_4)
casilla_e.listaCaminos.insertar(camino_5)
casilla_e.listaCaminos.insertar(camino_7)

casilla_f.listaCaminos.insertar(camino_6)

casilla_f.listaCaminos.insertar(camino_7)

casilla_g.listaCaminos.insertar(camino_3)
casilla_g.listaCaminos.insertar(camino_5)
casilla_g.listaCaminos.insertar(camino_8)

casilla_h.listaCaminos.insertar(camino_4)
casilla_h.listaCaminos.insertar(camino_8)

casilla_i.listaCaminos.insertar(camino_2)
casilla_i.listaCaminos.insertar(camino_6)
casilla_i.listaCaminos.insertar(camino_8)

# Inicializar la lista de los caminos que no tienen posesión
lista_caminosSinPosesion = lista()
lista_caminosSinPosesion.insertar(camino_1)
lista_caminosSinPosesion.insertar(camino_2)
lista_caminosSinPosesion.insertar(camino_3)
lista_caminosSinPosesion.insertar(camino_4)
lista_caminosSinPosesion.insertar(camino_5)
lista_caminosSinPosesion.insertar(camino_6)
lista_caminosSinPosesion.insertar(camino_7)
lista_caminosSinPosesion.insertar(camino_8)

# Inicializar la lista de las casillas que no están ocupadas
lista_casillas_noOcupadas = lista()
lista_casillas_noOcupadas.insertar(casilla_a)
lista_casillas_noOcupadas.insertar(casilla_b)
lista_casillas_noOcupadas.insertar(casilla_c)
lista_casillas_noOcupadas.insertar(casilla_d)
lista_casillas_noOcupadas.insertar(casilla_e)
lista_casillas_noOcupadas.insertar(casilla_f)
lista_casillas_noOcupadas.insertar(casilla_g)
lista_casillas_noOcupadas.insertar(casilla_h)
lista_casillas_noOcupadas.insertar(casilla_i)

################################################################################
##################  P R O G R A M A   P R I N C I P A L  #######################
################################################################################

print("                     JUEGO DE LA VIEJA                     ")
print("                     -----------------")
print("\n")
print("Seleccione el tipo de jugador 1")
print("    1) Escriba P si el jugador es una persona.")
print("    2) Escriba M si el jugador es la máquina.\n")
while True:
    try:
        res = input("    --> Su respuesta: ")
        print("")
        assert((res == "m") or (res == "M") or (res == "p") or (res == "P"))
        break
    except:
        print(">>> Debe ingresar una de las opciones indicadas.")
        print(">>> Vuelva a intentarlo.\n")
if res == "m" or res == "M":
    jugador1 = jugador(1,"M")
else:
    jugador1 = jugador(1,"P")
print("")
print("Seleccione el tipo de jugador 2")
print("    1) Escriba P si el jugador es una persona.")
print("    2) Escriba M si el jugador es la máquina.\n")
while True:
    try:
        res = input("    --> Su respuesta: ")
        print("")
        assert((res == "m") or (res == "M") or (res == "p") or (res == "P"))
        break
    except:
        print(">>> Debe ingresar una de las opciones indicadas.")
        print(">>> Vuelva a intentarlo.\n")
if res == "m" or res == "M":
    jugador2 = jugador(2,"M")
else:
    jugador2 = jugador(2,"P")
print("")

# Rutina principal en la que se desarrolla el juego
def jugar():
    jugadorActual = jugador1
    oponente = jugador2
    while True:
        imprimir_tablero(casilla_a, casilla_b, casilla_c, casilla_d, casilla_e, \
casilla_f, casilla_g, casilla_h, casilla_i)

        # Verificar si quedan jugadas disponibles
        if lista_casillas_noOcupadas.primero == None:
            mensaje_final(jugador1,jugador2)
            
        # Cuando juega la máquina
        if jugadorActual.tipoJugador == "M": 
            casillaJugada = juegaMáquina(jugadorActual.numJugador)

        # Cuando juega una persona
        else:
            while True: 
                try:
                    casillaJugada = input("Casilla a jugar: ")
                    print("")
                    (seguir,casillaJugada) = lista_casillas_noOcupadas.buscar(casillaJugada)
                    assert(seguir)
                    break
                except:
                    print(">>> Debe seleccionar una casilla no ocupada.")
                    print(">>> Vuelva a intentarlo.\n")
                    
        # En esta parte se moverán los caminos disponibles asociados a la casilla
        # a la lista que sea adecuada.
        casillaJugada.elemento.ocupada = True
        casillaJugada.elemento.dueño   = jugadorActual
        lista_casillas_noOcupadas.eliminar(casillaJugada.elemento.identificador)
        caminoExaminar = casillaJugada.elemento.listaCaminos.primero # El camino a examinar
                                                                     # es una estructura 
                                                                     # nodo, no un camino
        while caminoExaminar != None:
            if caminoExaminar.elemento.disponible == True:
                dueñoDelCamino = caminoExaminar.elemento.dueño
                if dueñoDelCamino == None:
                    traspasar(caminoExaminar,lista_caminosSinPosesion,jugadorActual.listaCaminos[0])
                    caminoExaminar.elemento.dueño = jugadorActual
                elif dueñoDelCamino == jugadorActual:
                    if dueñoDelCamino.listaCaminos[0].buscar(caminoExaminar.elemento.identificador)[0]:
                        traspasar(caminoExaminar,dueñoDelCamino.listaCaminos[0],dueñoDelCamino.listaCaminos[1])
                    else:
                        mensaje_final(jugador1,jugador2,jugadorActual)
                else:
                    caminoExaminar.elemento.dueño = None
                    caminoExaminar.elemento.disponible = False
                    if dueñoDelCamino.listaCaminos[0].buscar(caminoExaminar.elemento.identificador)[0]:
                        dueñoDelCamino.listaCaminos[0].eliminar(caminoExaminar.elemento.identificador)     
                    else:
                        dueñoDelCamino.listaCaminos[1].eliminar(caminoExaminar.elemento.identificador) 

            caminoExaminar = caminoExaminar.siguiente
        (jugadorActual, oponente) = (oponente, jugadorActual)

jugar()

"""
# Imprimir la lista de casillas no ocupadas.
print("Se va a imprimir la lista de casillas no ocupadas.\n")
contador = 0
nodoActual = lista_casillas_noOcupadas.primero
while nodoActual != None:
    contador += 1
    print(str(contador)+") "+str(nodoActual.elemento.identificador))
    nodoActual = nodoActual.siguiente
    
print("")

# Imprimir la lista de caminos disponibles        
print("Se va a imprimir la lista de caminos sin posesión.\n")
contador = 0
nodoActual = lista_caminosSinPosesion.primero
while nodoActual != None:
    contador += 1
    print(str(contador)+") "+str(nodoActual.elemento.identificador))
    nodoActual = nodoActual.siguiente
    
print("")

# Imprimir la lista de caminos correspondientes a la casilla "a"
print("Se va a imprimir la lista de caminos corresponientes a la casilla (a).\n")
contador = 0
nodoActual = casilla_a.listaCaminos.primero
while nodoActual != None:
    contador += 1
    print(str(contador)+") "+str(nodoActual.elemento.identificador))
    nodoActual = nodoActual.siguiente
    
print("")

"""

    





