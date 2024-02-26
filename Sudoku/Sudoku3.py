#
# Archivo: Sudoku.py
#
# Descripción: Programa que dado un tablero de sudoku por resolver, completa
#              el sudoku.
#
# Motivo: Ocio.
#
# Fecha: 08/01/2016

import sys


################################################################################
#############  D E F I N I C I Ó N   D E   E S T R U C T U R A S  ##############
################################################################################

class casilla():
    def __init__(self,nombre, bloque, fila, columna):
        self.nombre = nombre
        self.bloque = bloque
        self.fila   = fila
        self.columna = columna
        self.listaPosibles = [1,2,3,4,5,6,7,8,9]
        self.marcada = False

class bloque():
    def __init__(self):  # Es necesario crear el "init" para que se pueda crear más de un objeto de este tipo.
        self.listaCasillas = []
        self.listaDisponibles = [1,2,3,4,5,6,7,8,9]

class fila():
    def __init__(self):  # Es necesario crear el "init" para que se pueda crear más de un objeto de este tipo.
        self.listaCasillas = []
        self.listaDisponibles = [1,2,3,4,5,6,7,8,9]

class columna():
    def __init__(self):  # Es necesario crear el "init" para que se pueda crear más de un objeto de este tipo.
        self.listaCasillas = []
        self.listaDisponibles = [1,2,3,4,5,6,7,8,9]

class estado():
    def __init__(self):
        self.padre = None
        self.hijo = None
        self.listaPosiblesCasillas = None # Cada elemento será la lista de los posibles valores de una casilla en particular,
                                        # así que esta lista tendrá 81 elementos
        self.listaDisponiblesFilas = None
        self.listaDisponiblesColumnas = None
        self.listaDisponiblesBloques = None

class varGlobal():
    estadoActual = None

varGlobal = varGlobal()

################################################################################
###########  C R E A C I Ó N   D E   L A S   E S T R U C T U R A S  ############
################################################################################

""" Creación de los bloques """
bloque1 = bloque()
bloque2 = bloque()
bloque3 = bloque()
bloque4 = bloque()
bloque5 = bloque()
bloque6 = bloque()
bloque7 = bloque()
bloque8 = bloque()
bloque9 = bloque()

""" Creación de las filas """
fila1 = fila()
fila2 = fila()
fila3 = fila()
fila4 = fila()
fila5 = fila()
fila6 = fila()
fila7 = fila()
fila8 = fila()
fila9 = fila()

""" Creación de las columnas """
columna1 = columna()
columna2 = columna()
columna3 = columna()
columna4 = columna()
columna5 = columna()
columna6 = columna()
columna7 = columna()
columna8 = columna()
columna9 = columna()

""" Creación de las casillas """
casilla1 = casilla("B1 - 1",bloque1,fila1,columna1)
casilla2 = casilla("B1 - 2",bloque1,fila1,columna2)
casilla3 = casilla("B1 - 3",bloque1,fila1,columna3)
casilla4 = casilla("B2 - 1",bloque2,fila1,columna4)
casilla5 = casilla("B2 - 2",bloque2,fila1,columna5)
casilla6 = casilla("B2 - 3",bloque2,fila1,columna6)
casilla7 = casilla("B3 - 1",bloque3,fila1,columna7)
casilla8 = casilla("B3 - 2",bloque3,fila1,columna8)
casilla9 = casilla("B3 - 3",bloque3,fila1,columna9)

casilla10 = casilla("B1 - 4",bloque1,fila2,columna1)
casilla11 = casilla("B1 - 5",bloque1,fila2,columna2)
casilla12 = casilla("B1 - 6",bloque1,fila2,columna3)
casilla13 = casilla("B2 - 4",bloque2,fila2,columna4)
casilla14 = casilla("B2 - 5",bloque2,fila2,columna5)
casilla15 = casilla("B2 - 6",bloque2,fila2,columna6)
casilla16 = casilla("B3 - 4",bloque3,fila2,columna7)
casilla17 = casilla("B3 - 5",bloque3,fila2,columna8)
casilla18 = casilla("B3 - 6",bloque3,fila2,columna9)

casilla19 = casilla("B1 - 7",bloque1,fila3,columna1)
casilla20 = casilla("B1 - 8",bloque1,fila3,columna2)
casilla21 = casilla("B1 - 9",bloque1,fila3,columna3)
casilla22 = casilla("B2 - 7",bloque2,fila3,columna4)
casilla23 = casilla("B2 - 8",bloque2,fila3,columna5)
casilla24 = casilla("B2 - 9",bloque2,fila3,columna6)
casilla25 = casilla("B3 - 7",bloque3,fila3,columna7)
casilla26 = casilla("B3 - 8",bloque3,fila3,columna8)
casilla27 = casilla("B3 - 9",bloque3,fila3,columna9)

casilla28 = casilla("B4 - 1",bloque4,fila4,columna1)
casilla29 = casilla("B4 - 2",bloque4,fila4,columna2)
casilla30 = casilla("B4 - 3",bloque4,fila4,columna3)
casilla31 = casilla("B5 - 1",bloque5,fila4,columna4)
casilla32 = casilla("B5 - 2",bloque5,fila4,columna5)
casilla33 = casilla("B5 - 3",bloque5,fila4,columna6)
casilla34 = casilla("B6 - 1",bloque6,fila4,columna7)
casilla35 = casilla("B6 - 2",bloque6,fila4,columna8)
casilla36 = casilla("B6 - 3",bloque6,fila4,columna9)

casilla37 = casilla("B4 - 4",bloque4,fila5,columna1)
casilla38 = casilla("B4 - 5",bloque4,fila5,columna2)
casilla39 = casilla("B4 - 6",bloque4,fila5,columna3)
casilla40 = casilla("B5 - 4",bloque5,fila5,columna4)
casilla41 = casilla("B5 - 5",bloque5,fila5,columna5)
casilla42 = casilla("B5 - 6",bloque5,fila5,columna6)
casilla43 = casilla("B6 - 4",bloque6,fila5,columna7)
casilla44 = casilla("B6 - 5",bloque6,fila5,columna8)
casilla45 = casilla("B6 - 6",bloque6,fila5,columna9)

casilla46 = casilla("B4 - 7",bloque4,fila6,columna1)
casilla47 = casilla("B4 - 8",bloque4,fila6,columna2)
casilla48 = casilla("B4 - 9",bloque4,fila6,columna3)
casilla49 = casilla("B5 - 7",bloque5,fila6,columna4)
casilla50 = casilla("B5 - 8",bloque5,fila6,columna5)
casilla51 = casilla("B5 - 9",bloque5,fila6,columna6)
casilla52 = casilla("B6 - 7",bloque6,fila6,columna7)
casilla53 = casilla("B6 - 8",bloque6,fila6,columna8)
casilla54 = casilla("B6 - 9",bloque6,fila6,columna9)

casilla55 = casilla("B7 - 1",bloque7,fila7,columna1)
casilla56 = casilla("B7 - 2",bloque7,fila7,columna2)
casilla57 = casilla("B7 - 3",bloque7,fila7,columna3)
casilla58 = casilla("B8 - 1",bloque8,fila7,columna4)
casilla59 = casilla("B8 - 2",bloque8,fila7,columna5)
casilla60 = casilla("B8 - 3",bloque8,fila7,columna6)
casilla61 = casilla("B9 - 1",bloque9,fila7,columna7)
casilla62 = casilla("B9 - 2",bloque9,fila7,columna8)
casilla63 = casilla("B9 - 3",bloque9,fila7,columna9)

casilla64 = casilla("B7 - 4",bloque7,fila8,columna1)
casilla65 = casilla("B7 - 5",bloque7,fila8,columna2)
casilla66 = casilla("B7 - 6",bloque7,fila8,columna3)
casilla67 = casilla("B8 - 4",bloque8,fila8,columna4)
casilla68 = casilla("B8 - 5",bloque8,fila8,columna5)
casilla69 = casilla("B8 - 6",bloque8,fila8,columna6)
casilla70 = casilla("B9 - 4",bloque9,fila8,columna7)
casilla71 = casilla("B9 - 5",bloque9,fila8,columna8)
casilla72 = casilla("B9 - 6",bloque9,fila8,columna9)

casilla73 = casilla("B7 - 7",bloque7,fila9,columna1)
casilla74 = casilla("B7 - 8",bloque7,fila9,columna2)
casilla75 = casilla("B7 - 9",bloque7,fila9,columna3)
casilla76 = casilla("B8 - 7",bloque8,fila9,columna4)
casilla77 = casilla("B8 - 8",bloque8,fila9,columna5)
casilla78 = casilla("B8 - 9",bloque8,fila9,columna6)
casilla79 = casilla("B9 - 7",bloque9,fila9,columna7)
casilla80 = casilla("B9 - 8",bloque9,fila9,columna8)
casilla81 = casilla("B9 - 9",bloque9,fila9,columna9)

"""Designar a los bloques sus respectivas casillas"""
bloque1.listaCasillas = [casilla1,casilla2,casilla3,casilla10,casilla11,casilla12,casilla19,casilla20,casilla21]
bloque2.listaCasillas = [casilla4,casilla5,casilla6,casilla13,casilla14,casilla15,casilla22,casilla23,casilla24]
bloque3.listaCasillas = [casilla7,casilla8,casilla9,casilla16,casilla17,casilla18,casilla25,casilla26,casilla27]
bloque4.listaCasillas = [casilla28,casilla29,casilla30,casilla37,casilla38,casilla39,casilla46,casilla47,casilla48]
bloque5.listaCasillas = [casilla31,casilla32,casilla33,casilla40,casilla41,casilla42,casilla49,casilla50,casilla51]
bloque6.listaCasillas = [casilla34,casilla35,casilla36,casilla43,casilla44,casilla45,casilla52,casilla53,casilla54]
bloque7.listaCasillas = [casilla55,casilla56,casilla57,casilla64,casilla65,casilla66,casilla73,casilla74,casilla75]
bloque8.listaCasillas = [casilla58,casilla59,casilla60,casilla67,casilla68,casilla69,casilla76,casilla77,casilla78]
bloque9.listaCasillas = [casilla61,casilla62,casilla63,casilla70,casilla71,casilla72,casilla79,casilla80,casilla81]

"""Designar a las filas sus respectivas casillas"""
fila1.listaCasillas = [casilla1,casilla2,casilla3,casilla4,casilla5,casilla6,casilla7,casilla8,casilla9]
fila2.listaCasillas = [casilla10,casilla11,casilla12,casilla13,casilla14,casilla15,casilla16,casilla17,casilla18]
fila3.listaCasillas = [casilla19,casilla20,casilla21,casilla22,casilla23,casilla24,casilla25,casilla26,casilla27]
fila4.listaCasillas = [casilla28,casilla29,casilla30,casilla31,casilla32,casilla33,casilla34,casilla35,casilla36]
fila5.listaCasillas = [casilla37,casilla38,casilla39,casilla40,casilla41,casilla42,casilla43,casilla44,casilla45]
fila6.listaCasillas = [casilla46,casilla47,casilla48,casilla49,casilla50,casilla51,casilla52,casilla53,casilla54]
fila7.listaCasillas = [casilla55,casilla56,casilla57,casilla58,casilla59,casilla60,casilla61,casilla62,casilla63]
fila8.listaCasillas = [casilla64,casilla65,casilla66,casilla67,casilla68,casilla69,casilla70,casilla71,casilla72]
fila9.listaCasillas = [casilla73,casilla74,casilla75,casilla76,casilla77,casilla78,casilla79,casilla80,casilla81]

"""Designar a las columnas sus respectivas casillas"""
columna1.listaCasillas = [casilla1,casilla10,casilla19,casilla28,casilla37,casilla46,casilla55,casilla64,casilla73]
columna2.listaCasillas = [casilla2,casilla11,casilla20,casilla29,casilla38,casilla47,casilla56,casilla65,casilla74]
columna3.listaCasillas = [casilla3,casilla12,casilla21,casilla30,casilla39,casilla48,casilla57,casilla66,casilla75]
columna4.listaCasillas = [casilla4,casilla13,casilla22,casilla31,casilla40,casilla49,casilla58,casilla67,casilla76]
columna5.listaCasillas = [casilla5,casilla14,casilla23,casilla32,casilla41,casilla50,casilla59,casilla68,casilla77]
columna6.listaCasillas = [casilla6,casilla15,casilla24,casilla33,casilla42,casilla51,casilla60,casilla69,casilla78]
columna7.listaCasillas = [casilla7,casilla16,casilla25,casilla34,casilla43,casilla52,casilla61,casilla70,casilla79]
columna8.listaCasillas = [casilla8,casilla17,casilla26,casilla35,casilla44,casilla53,casilla62,casilla71,casilla80]
columna9.listaCasillas = [casilla9,casilla18,casilla27,casilla36,casilla45,casilla54,casilla63,casilla72,casilla81]

"""Lista de todas las casillas"""
listaCasillas = [casilla1,casilla2,casilla3,casilla4,casilla5,casilla6,casilla7,casilla8,casilla9,casilla10,casilla11,casilla12,casilla13,casilla14,casilla15,casilla16,\
                 casilla17,casilla18,casilla19,casilla20,casilla21,casilla22,casilla23,casilla24,casilla25,casilla26,casilla27,casilla28,casilla29,casilla30,casilla31,\
                 casilla32,casilla33,casilla34,casilla35,casilla36,casilla37,casilla38,casilla39,casilla40,casilla41,casilla42,casilla43,casilla44,casilla45,casilla46,\
                 casilla47,casilla48,casilla49,casilla50,casilla51,casilla52,casilla53,casilla54,casilla55,casilla56,casilla57,casilla58,casilla59,casilla60,casilla61,\
                 casilla62,casilla63,casilla64,casilla65,casilla66,casilla67,casilla68,casilla69,casilla70,casilla71,casilla72,casilla73,casilla74,casilla75,casilla76,\
                 casilla77,casilla78,casilla79,casilla80,casilla81]

"""Lista de todos los bloques"""
listaBloques = [bloque1,bloque2,bloque3,bloque4,bloque5,bloque6,bloque7,bloque8,bloque9]

"""Lista de todas las filas"""
listaFilas = [fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila8,fila9]

"""Lista de todas las columnas"""
listaColumnas = [columna1,columna2,columna3,columna4,columna5,columna6,columna7,columna8,columna9]

################################################################################
##############  C R E A C I Ó N   D E   L A S   R U T I N A S  #################
################################################################################

def marcar(casilla,valor):
    casilla.marcada = True
    if valor in casilla.bloque.listaDisponibles:
        casilla.bloque.listaDisponibles.remove(valor)
    if valor in casilla.fila.listaDisponibles:
        casilla.fila.listaDisponibles.remove(valor)
    if valor in casilla.columna.listaDisponibles:
        casilla.columna.listaDisponibles.remove(valor)
    casilla.listaPosibles = [valor]
    
#### Leer el archivo ####
archivo       = open("datosSudoku.txt", "r")
arregloLineas = archivo.readlines()
iterador = 0

for linea in arregloLineas:
    linea.split(" ")
    for i in range(len(linea)):
        if (linea[i]!=" ") and (linea[i]!='\n'):
            valor = int(linea[i])
            if valor != 0:
                marcar(listaCasillas[iterador],valor)
            iterador +=1

archivo.close()

### Determinar si el sudoku está completo ###
def sudokuCompleto():
    completo = True
    for casilla in listaCasillas:
        if len(casilla.listaPosibles)>1:  
            completo = False
            break
    return completo

def imprimirSudokuCompleto():
    print(casilla1.listaPosibles[0],casilla2.listaPosibles[0],casilla3.listaPosibles[0], casilla4.listaPosibles[0],casilla5.listaPosibles[0], \
          casilla6.listaPosibles[0],casilla7.listaPosibles[0],casilla8.listaPosibles[0], casilla9.listaPosibles[0])
    print(casilla10.listaPosibles[0],casilla11.listaPosibles[0],casilla12.listaPosibles[0],casilla13.listaPosibles[0],casilla14.listaPosibles[0],\
          casilla15.listaPosibles[0],casilla16.listaPosibles[0], casilla17.listaPosibles[0],casilla18.listaPosibles[0])
    print(casilla19.listaPosibles[0],casilla20.listaPosibles[0],casilla21.listaPosibles[0],casilla22.listaPosibles[0],casilla23.listaPosibles[0],\
          casilla24.listaPosibles[0],casilla25.listaPosibles[0],casilla26.listaPosibles[0],casilla27.listaPosibles[0])
    print(casilla28.listaPosibles[0],casilla29.listaPosibles[0],casilla30.listaPosibles[0],casilla31.listaPosibles[0],casilla32.listaPosibles[0],\
          casilla33.listaPosibles[0],casilla34.listaPosibles[0],casilla35.listaPosibles[0],casilla36.listaPosibles[0])
    print(casilla37.listaPosibles[0],casilla38.listaPosibles[0],casilla39.listaPosibles[0],casilla40.listaPosibles[0],casilla41.listaPosibles[0],\
          casilla42.listaPosibles[0],casilla43.listaPosibles[0],casilla44.listaPosibles[0],casilla45.listaPosibles[0])
    print(casilla46.listaPosibles[0],casilla47.listaPosibles[0],casilla48.listaPosibles[0],casilla49.listaPosibles[0],casilla50.listaPosibles[0],\
          casilla51.listaPosibles[0],casilla52.listaPosibles[0],casilla53.listaPosibles[0],casilla54.listaPosibles[0])
    print(casilla55.listaPosibles[0],casilla56.listaPosibles[0],casilla57.listaPosibles[0],casilla58.listaPosibles[0],casilla59.listaPosibles[0],\
          casilla60.listaPosibles[0],casilla61.listaPosibles[0],casilla62.listaPosibles[0],casilla63.listaPosibles[0])
    print(casilla64.listaPosibles[0],casilla65.listaPosibles[0],casilla66.listaPosibles[0],casilla67.listaPosibles[0],casilla68.listaPosibles[0],\
          casilla69.listaPosibles[0],casilla70.listaPosibles[0],casilla71.listaPosibles[0],casilla72.listaPosibles[0])
    print(casilla73.listaPosibles[0],casilla74.listaPosibles[0],casilla75.listaPosibles[0],casilla76.listaPosibles[0],casilla77.listaPosibles[0],\
          casilla78.listaPosibles[0],casilla79.listaPosibles[0],casilla80.listaPosibles[0],casilla81.listaPosibles[0])

def imprimirSudokuIncompleto():
    for casilla in listaCasillas:
        print(str(casilla.nombre)+" ---> listaPosibles = "+str(casilla.listaPosibles))

### Función para recuperar las posibilidades restantes de las casillas, filas, columnas y ###
### bloques de un estado anterior ####
def regresarEstadoAnterior(estado):
    estado = estado.padre

    # Devolver las casillas
    for i in range(0,81):
        listaCasillas[i].listaPosibles = estado.listaPosiblesCasillas[i]
        
    # Devolver las filas, columnas y bloques
    for i in range(0,9):
        listaFilas[i].listaDisponibles = estado.listaDisponiblesFilas[i]
        listaColumnas[i].listaDisponibles = estado.listaDisponiblesColumnas[i]
        listaBloques[i].listaDisponibles = estado.listaDisponiblesColumnas[i]

### Función para modificar el estado actual y no crear uno nuevo ###
def actualizarEstadoActual(estado):
    estado.listaPosiblesCasillas = []
    estado.listaDisponiblesFilas = []
    estado.listaDisponiblesColumnas = []
    estado.listaDisponiblesBloques = []
    
    for casilla in listaCasillas:
        estado.listaPosiblesCasillas.append(casilla.listaPosibles)
    for fila in listaFilas:
        estado.listaDisponiblesFilas.append(fila.listaDisponibles)
    for columna in listaColumnas:
        estado.listaDisponiblesColumnas.append(columna.listaDisponibles)
    for bloque in listaBloques:
        estado.listaDisponiblesBloques.append(bloque.listaDisponibles)
    

################################################################################
##############  P R O C E D I M I E N T O   P R I N C I P A L  #################
################################################################################

### Crear el primer estado ###
estadoActual = estado()
varGlobal.estadoActual = estado
actualizarEstadoActual(estado)

def rutinaPrincipal(estadoActual, nivel):
    print("Entré, con nivel de: "+str(nivel))
    print("Aquí al entrar, mi sudoku incompleto es: \n")
    imprimirSudokuIncompleto()
    print("")
    hayCambio = True

    while hayCambio:
        hayCambio = False
    
        """ Analizar las casillas """
        for casilla in listaCasillas:
            #print("")
            #print(casilla.nombre)
            #print("Antes del cambio: "+str(casilla.listaPosibles))
            if not casilla.marcada:
                listaRemover = []
                #print("Disponibles del bloque ---> "+str(casilla.bloque.listaDisponibles))
                #print("Disponibles de la fila ---> "+str(casilla.fila.listaDisponibles))
                #print("Disponibles de columna ---> "+str(casilla.columna.listaDisponibles))
                for valor in casilla.listaPosibles:
                    if valor not in casilla.bloque.listaDisponibles:
                        listaRemover.append(valor)
                        hayCambio = True
                    elif valor not in casilla.fila.listaDisponibles:
                        listaRemover.append(valor)
                        hayCambio = True
                    elif valor not in casilla.columna.listaDisponibles:
                        listaRemover.append(valor)
                        hayCambio = True
                #print("Lista de valores a remover: "+str(listaRemover))
                for valor in listaRemover:
                    casilla.listaPosibles.remove(valor)
                if len(casilla.listaPosibles) == 0:
                    print(" \nVoy a regresarme ")
                    imprimirSudokuIncompleto()
                    print("")
                    return False
                if len(casilla.listaPosibles) == 1:
                    marcar(casilla,casilla.listaPosibles[0])
            #print("Después del cambio: "+str(casilla.listaPosibles))

        """Analizar si un valor aparece sólo una vez en una fila """
        for fila in listaFilas:
            for valor in fila.listaDisponibles:
                casillasAparece = []
                for casilla in fila.listaCasillas:
                    if valor in casilla.listaPosibles:
                        casillasAparece.append(casilla)
                if len(casillasAparece) == 1:
                    marcar(casillasAparece[0],valor)
                    hayCambio = True

        """Analizar si un valor aparece sólo una vez en una columna """
        for columna in listaColumnas:
            for valor in columna.listaDisponibles:
                casillasAparece = []
                for casilla in columna.listaCasillas:
                    if valor in casilla.listaPosibles:
                        casillasAparece.append(casilla)
                if len(casillasAparece) == 1:
                    marcar(casillasAparece[0],valor)
                    hayCambio = True

        """Analizar los bloques """
        for bloque in listaBloques:
            for valor in bloque.listaDisponibles:
                casillasAparece = []
                filasAparece = []
                columnasAparece = []
                for casilla in bloque.listaCasillas:
                    if valor in casilla.listaPosibles:
                        casillasAparece.append(casilla)
                        if casilla.fila not in filasAparece:
                            filasAparece.append(casilla.fila)
                        if casilla.columna not in columnasAparece:
                            columnasAparece.append(casilla.columna)
                """ Analizar si un valor aparece sólo una vez en un bloque """
                if len(casillasAparece) == 1:
                    marcar(casillasAparece[0],valor)
                    hayCambio = True
                """ Analizar si aparece en sólo una fila """
                if len(filasAparece) == 1:
                    for casilla in filasAparece[0].listaCasillas:
                        """ En caso afirmativo, ver si hay más con ese valor en la misma fila,
                        pero en otro bloque """
                        if casilla.bloque != bloque:
                            if valor in casilla.listaPosibles:
                                casilla.listaPosibles.remove(valor)
                                hayCambio = True
                """ Analizar si aparece en sólo una columna """
                if len(columnasAparece) == 1:
                    for casilla in columnasAparece[0].listaCasillas:
                        """ En caso afirmativo, ver si hay más con ese valor en la misma columna,
                        pero en otro bloque """
                        if casilla.bloque != bloque:
                            if valor in casilla.listaPosibles:
                                casilla.listaPosibles.remove(valor)
                                hayCambio = True
                                
        if not hayCambio:
            completo = sudokuCompleto()
            if completo:
                imprimirSudokuCompleto()
                return True
            else:
                print("nivel = "+str(nivel)+"\n")
                imprimirSudokuIncompleto()
                print(" ==================================================== ")
                print("\n")
            
                actualizarEstadoActual(estadoActual)
                for casilla in listaCasillas:
                    if len(casilla.listaPosibles) != 1:
                        print("####")
                        print("La casilla que se va a examinar es: "+str(casilla.nombre))
                        print("Su lista de posibles es: "+str(casilla.listaPosibles))
                        print("####")
                        for valor in casilla.listaPosibles:
                            estadoHijo = estado()
                            estadoHijo.padre = estadoActual
                            marcar(casilla,valor)
                            print("****")
                            print("Voy a entrar a uno nuevo")
                            print("El valor que se acaba de marcar es: "+str(valor))
                            print("****")
                            actualizarEstadoActual(estadoHijo)
                            seCumplio = rutinaPrincipal(estadoHijo, nivel+1)
                            print("")
                            print("Se cumplió = "+str(seCumplio))
                            print("La casilla actual es: "+str(casilla.nombre))
                            print("El valor que se iba a marcar es: "+str(valor))
                            print("Mi nivel actual es: "+str(nivel))
                            print("")
                            if seCumplio:
                                if nivel != 0:
                                    return True
                                else:
                                    imprimirSudokuCompleto()
                                    return True
                            else:
                                regresarEstadoAnterior(estadoHijo) # Necesario para que en la próxima iteración tome las posibilidades
                                                               # como estaban antes.

rutinaPrincipal(estadoActual, 0)





                    
            
            
            
