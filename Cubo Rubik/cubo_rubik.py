#
# Archivo: cubo_rubik.py
#
# Descripción: Para entender cómo se mueven las caras de las piezas
#              de un cubo 3 x 3 después de aplicar un movimiento o
#              una secuencia de movimientos.
#
# Fecha de elaboración: 24 de febrero de 2024

import copy, pprint, sys, itertools
import numpy as np

# Inicializar arreglos que permitirán construir el cubo
nombres_caras = ["F","U","L","R","D","B"] # Nombres de las caras del cubo
posiciones_h = ["L","R"] # Posiciones horizontales
posiciones_v = ["U","D"] # Posiciones verticales

# En un movimiento de una cara, hay una serie de cuadros en la cara
# adyacente que se mueven también. Aquí listamos cuáles son por cada cara.
# Tienen que estar colocados en sentido horario del movimiento
secuencia_mov = {
    "U": ['FRU','FU','FLU','LRU','LU','LLU','BRU','BU','BLU','RRU','RU','RLU'],
    "D": ["FLD","FD","FRD","RLD","RD","RRD","BLD","BD","BRD","LLD","LD","LRD"],
    "R": ['FRD','FR','FRU','URD','UR','URU','BLU','BL','BLD','DRD','DR','DRU'],
    "L": ["FLU","FL","FLD","DLU","DL","DLD","BRD","BR","BRU","ULU","UL","ULD"],
    "F": ["ULD","UD","URD","RLU","RL","RLD","DRU","DU","DLU","LRD","LR","LRU"],
    "B": ["URU","UU","ULR","LLU","LL","LLD","DLD","DD","DRD","RRD","RR","RRU"]
}

# Indica en orden cuáles son las posiciones de los cuadros de una cara,
# yendo de izquierda a derecha en las columnas, y de arriba a abajo en las filas
cuadros_cara = ["LU","U","RU","L","C","R","LD","D","RD"]
    
# Función para inicializar el cubo completo
def construir_cubo():
    cubo = {}

    # Construir caras del cubo
    for cara in nombres_caras:
        diccionario_cara = {}
        
        # Piezas de la cruz de la cara (La "C" es por el centro)
        for elem in ["C"] + posiciones_h + posiciones_v:
            diccionario_cara[elem] = cara + elem

        # Piezas de los vértices de la cara
        for elem in [x+y for x in posiciones_h for y in posiciones_v]:
            diccionario_cara[elem] = cara + elem   
        
        cubo[cara] = diccionario_cara
    return cubo   

# Aplicar movimiento a cubo
def aplicar_movimiento(movimiento, cubo):
    sentido_horario = (len(movimiento) == 1)
    cara = movimiento[0]
    
    # 1) Rotar las casillas correspondientes de las caras adyacentes,
    # que son hileras de tres piezas
    
    ##### 1.1) Obtener la lista de las posiciones que se van a mover
    sec = secuencia_mov[cara]
    ##### 1.2) Obtener la lista de los valores actuales en dichas posiciones
    valores = list(cubo[s[0]][s[1:]] for s in sec)

    ##### 1.3) Reordenar lista de valores
    if sentido_horario: # Los 3 últimos elementos colocarlos al principio
        valores = valores[-3:] + valores[:-3]
    else: # Los 3 primeros elementos colocarlos al final
        valores = valores[3:] + valores[:3]

    ##### 1.4) Actualizar las posiciones de los valores
    for i in range(len(sec)):
        cadena = sec[i]
        cubo[cadena[0]][cadena[1:]] = valores[i]

    # 2) Rotar las piezas de la cara que se va a mover

    ##### 2.1) Obtener lista de los valores actuales de lo que se va a mover
    valores = list(cubo[cara][cadena] for cadena in cuadros_cara)

    ##### 2.2) Convertir esa lista en matriz para poder rotarla
    valores = np.reshape(np.array(valores), (3, 3))

    ##### 2.3) Rotar la matriz
    valores = np.rot90(valores, k=-1) if sentido_horario else np.rot90(valores)

    ##### 2.4) Devolver esa matriz a su forma de lista aplanada
    valores = list(itertools.chain(*valores.tolist()))
    
    ##### 2.5) Actualizar las posiciones de los valores
    for i in range(len(cuadros_cara)):
        cadena = cuadros_cara[i]
        cubo[cara][cadena] = valores[i]

# Para porder imprimir, por cada cuadro, en qué posición
# estuvo durante una secuencia de movimientos
def rastrear_movimiento_cuadros(sec_movimientos,cubo):
    # Crear diccionario con las listas de las posiciones,
    # que incluye la posición inicial de cada pieza:
    diccionario = {}
    for cara in cubo:
        for cuadro in cubo[cara]:
            diccionario[cara+cuadro] = [cubo[cara][cuadro]]

    # Aplicar los movimientos e ir rastreando las posiciones
    for mov in sec_movimientos:
        aplicar_movimiento(mov, cubo)
        for cara in cubo:
            for cuadro in cubo[cara]:
                diccionario[cubo[cara][cuadro]].append(cara+cuadro)

    return diccionario

# Para simplificar el análisis de entender los datos de un
# rastreador de movimiento, esto devuelve un diccionario que se
# separa en dos partes:
#
# 1) Una almacena los cuadros que volvieron a la misma posición original.
# 2) La otra almacena los cuadros que fueron movidos de posición.
#
# Las casillas que nunca cambiaron de posición durante toda la secuencia de movimientos
# no son almacenadas aquí.
def analizar_datos(rastreador_movimiento):
    diccionario = {"mismo_sitio":{}, "movido":{}}
    for elem in rastreador_movimiento:
        lista = rastreador_movimiento[elem]
        # No incluimos las casillas que nunca cambiaron de posición
        if len(set(lista)) != 1:
            if lista[0] == lista[-1]:
                diccionario["mismo_sitio"][elem] = lista
            else:
                diccionario["movido"][elem] = lista
    return diccionario

# Programa principal para hacer pruebas
cubo = construir_cubo()
secuencia_movimientos = ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]
dict1 = rastrear_movimiento_cuadros(secuencia_movimientos, cubo)
dict2 = analizar_datos(dict1)
pprint.pprint(dict2)






    
