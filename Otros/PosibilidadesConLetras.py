class globales:
    tablaHashGLORIA = list([] for i in range(185))
    tablaHashPRECIO = list([] for i in range(185))
    tablaHashNEURALGICA = list([] for i in range(662))
    tablaHashMIHOGAR = list([] for i in range(1000))
    tablaHashPLENODESCARO = list([] for i in range(4000))

globales = globales()

class nodoLetras:
    def __init__(self,estado,padre=None):
        self.estado = estado
        self.padre = padre
        self.hijos = None


class estado:
    def __init__(self,cadenaAcumulada, valorCadena, letrasRestantes):
        self.cadenaAcumulada = cadenaAcumulada
        self.valorCadena = valorCadena
        self.letrasRestantes = letrasRestantes

class colaFIFO:

    def __init__(self,primero=None,ultimo=None):

        self.primero = primero

        self.ultimo = ultimo

        self.tamanio = 0

        self.tamanioMax = 0



    def push(self,nodoNuevoCola):

        if self.primero == None:

            self.primero = nodoNuevoCola

            self.ultimo = nodoNuevoCola

        self.ultimo.siguiente = nodoNuevoCola

        self.ultimo = nodoNuevoCola

        self.tamanio += 1

        if self.tamanio > self.tamanioMax:

            self.tamanioMax = self.tamanio



    def pop(self):

        devolver = self.primero

        if devolver != None:

            self.primero = devolver.siguiente

            self.tamanio -= 1

        return devolver

def obtenerValorCadenaGLORIA(arreglo):
    valorDevolver = 0
    #letrasConValores = [["G",2],["L",3],["O",5],["R",7],["I",11],["A",13]]
    i = 0
    for elem in arreglo:
        i += 1
        if elem == "G":
            valorDevolver += i*2
        elif elem == "L":
            valorDevolver += i*3
        elif elem == "O":
            valorDevolver += i*5
        elif elem == "R":
            valorDevolver += i*7
        elif elem == "I":
            valorDevolver += i*11
        elif elem == "A":
            valorDevolver += i*13

    return valorDevolver

def obtenerValorCadenaPRECIO(arreglo):
    valorDevolver = 0
    #letrasConValores = [["G",2],["L",3],["O",5],["R",7],["I",11],["A",13]]
    i = 0
    for elem in arreglo:
        i += 1
        if elem == "P":
            valorDevolver += i*2
        elif elem == "R":
            valorDevolver += i*3
        elif elem == "E":
            valorDevolver += i*5
        elif elem == "C":
            valorDevolver += i*7
        elif elem == "I":
            valorDevolver += i*11
        elif elem == "O":
            valorDevolver += i*13

    return valorDevolver

def obtenerValorCadenaNEURALGICA(arreglo):
    valorDevolver = 0
    #letrasConValores = [["N",2],["E",3],["U",5],["R",7],["A",11],["L",13]],["G",17]],["I",19]],["C",23]]
    i = 0
    for elem in arreglo:
        i += 1
        if elem == "P":
            valorDevolver += i*2
        elif elem == "R":
            valorDevolver += i*3
        elif elem == "E":
            valorDevolver += i*5
        elif elem == "C":
            valorDevolver += i*7
        elif elem == "I":
            valorDevolver += i*11
        elif elem == "O":
            valorDevolver += i*13

    return valorDevolver

def obtenerValorCadenaNEURALGICA(arreglo):
    valorDevolver = 0
    #letrasConValores = [["N",2],["E",3],["U",5],["R",7],["A",11],["L",13]],["G",17]],["I",19]],["C",23]]
    i = 0
    for elem in arreglo:
        i += 1
        if elem == "P":
            valorDevolver += i*2
        elif elem == "R":
            valorDevolver += i*3
        elif elem == "E":
            valorDevolver += i*5
        elif elem == "C":
            valorDevolver += i*7
        elif elem == "I":
            valorDevolver += i*11
        elif elem == "O":
            valorDevolver += i*13

    return valorDevolver

def obtenerValorCadenaMIHOGAR(arreglo):
    valorDevolver = 0
    #letrasConValores = [["N",2],["E",3],["U",5],["R",7],["A",11],["L",13]],["G",17]],["I",19]],["C",23]]
    i = 0
    for elem in arreglo:
        i += 1
        if elem == "M":
            valorDevolver += i*2
        elif elem == "I":
            valorDevolver += i*3
        elif elem == "H":
            valorDevolver += i*5
        elif elem == "O":
            valorDevolver += i*7
        elif elem == "G":
            valorDevolver += i*11
        elif elem == "A":
            valorDevolver += i*13
        elif elem == "R":
            valorDevolver += i*13

    return valorDevolver

def obtenerValorCadenaPLENODESCARO(arreglo):
    valorDevolver = 0
    i = 0
    for elem in arreglo:
        i += 1
        if elem == "P":
            valorDevolver += i*2
        elif elem == "L":
            valorDevolver += i*3
        elif elem == "E":
            valorDevolver += i*5
        elif elem == "N":
            valorDevolver += i*7
        elif elem == "O":
            valorDevolver += i*11
        elif elem == "D":
            valorDevolver += i*13
        elif elem == "S":
            valorDevolver += i*17
        elif elem == "C":
            valorDevolver += i*19
        elif elem == "A":
            valorDevolver += i*23
        elif elem == "R":
            valorDevolver += i*29

    return valorDevolver

def generarHijos(nodo,funcion):
    cadenaAcumulada = nodo.estado.cadenaAcumulada[:]
    letrasRestantes = nodo.estado.letrasRestantes[:]
    maxI = len(letrasRestantes)
    listaHijos = []

    for i in range(maxI):
        letraNueva = letrasRestantes[i]
        nuevasLetrasRestantes = list(letrasRestantes[j] for j in range(i))+list(letrasRestantes[j] for j in range(i+1,maxI))
        nuevaCadena = cadenaAcumulada[:]+[letraNueva]
        valorCadenaNueva = funcion(nuevaCadena)
        nuevoEstado = estado(nuevaCadena,valorCadenaNueva,nuevasLetrasRestantes)
        nodoHijo = nodoLetras(nuevoEstado,nodo)
        listaHijos.append(nodoHijo)

    return listaHijos

def BFS(nodoInicial,funcion,maxTam,tablaHash):
    cola = colaFIFO()
    cola.push(nodoInicial)
    while cola.tamanio != 0:
        nuevoNodo = cola.pop()
        if len(nuevoNodo.estado.cadenaAcumulada) == maxTam:
            print(nuevoNodo.estado.cadenaAcumulada)
        else:
            hijos = generarHijos(nuevoNodo,funcion)
            for hijo in hijos:
                valorCadena = hijo.estado.valorCadena
                cadenaAcumulada = hijo.estado.cadenaAcumulada
                if cadenaAcumulada not in tablaHash[valorCadena]:
                    tablaHash.append(cadenaAcumulada)
                    cola.push(hijo)
        
###############################
estadoInicial = estado([],0,["P","L","E","N","O","D","E","S","C","A","R","O"])
nodoInicial = nodoLetras(estadoInicial)
BFS(nodoInicial,obtenerValorCadenaPLENODESCARO,12,globales.tablaHashPLENODESCARO)
    
    

    
