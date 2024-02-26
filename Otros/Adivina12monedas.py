# Tenemos 12 monedas indistinguibles, de las cuales todas pesan lo mismo
# excepto una que es diferente, que puede pesar más o menos que las demás.
# Contamos con una balanza y tres intentos para determinar cuál es la moneda
# diferente.

import sys

# Clase para guardar la información de una moneda
class m:
    def __init__(self,numero,peso):
        self.numero = numero
        self.peso = peso

# Clase para pesar un conjunto de monedas
def pesar(listaMonedas):
    pesoTotal = 0
    for moneda in listaMonedas:
        pesoTotal += moneda.peso
    return pesoTotal

# Función para determinar cuál de dos monedas es la mala, comparando con una que sabemos que es buena
def descartarDeDos(monedasSospechosas,monedaBuena):
    if monedasSospechosas[0].peso != monedaBuena.peso:
        return monedasSospechosas[0].numero
    else:
        return monedasSospechosas[1].numero

# Función para determinar cuál de tres monedas es la mala
def descartarDeTres(listaTresMonedas):
    if listaTresMonedas[0].peso != listaTresMonedas[1].peso: # En este caso, sabemos que la 2 es buena
        if listaTresMonedas[0].peso != listaTresMonedas[2].peso: 
            return listaTresMonedas[0].numero
        else:
            return listaTresMonedas[1].numero
    else:
        return listaTresMonedas[2].numero
          
# Función principal del programa
def hacerIntentos(numeroMoneda,pesoDiferente):
    # * numeroMoneda = el número de la moneda distinta a las demás
    # * pesoDiferente = el peso que tendrá esa moneda.
    #                   (Puede ser 0 o 2, mientras que las demás pesan 1).
    
    # RETORNAR
    # * monedaMalaSupuesta = 0 # --> Es el número de moneda que el programa deduce que es la mala.
                               #     Debe coincidir con numeroMoneda.
                           
    listaTotalMonedas = list(m(i,1) for i in range(1,13))
    listaTotalMonedas[numeroMoneda-1].peso = pesoDiferente

    # Aquí va el primer intento       
    brazoIzquierdo = sum(listaTotalMonedas[i].peso for i in range(0,4)) # A la izquierda ponemos las monedas 1,2,3,4
    brazoDerecho = sum(listaTotalMonedas[i].peso for i in range(4,8))   # A la derecha ponemos las monedas 5,6,7,8

    if brazoIzquierdo == brazoDerecho: # Si la balanza se equilibra, la moneda mala sólo puede ser 9,10,11,12
        
        # Aquí va el segundo intento
        if listaTotalMonedas[8].peso != listaTotalMonedas[9].peso: # Si al pesar las dos primeras (9 y 10), éstas no coinciden
            # Aquí va el tercer intento
            monedaMalaSupuesta = descartarDeDos([listaTotalMonedas[8],listaTotalMonedas[9]],listaTotalMonedas[10])
            
        else: # Si al pesar las dos primeras, éstas coinciden, la mala es una de las otras dos:
            # Aquí va el tercer intento
            monedaMalaSupuesta = descartarDeDos([listaTotalMonedas[10],listaTotalMonedas[11]],listaTotalMonedas[8])

    else: # Si la balanza no está balanceada
        
        if brazoIzquierdo > brazoDerecho: # Si el brazo de la izquierda es más pesado
            mayorPeso1 = 1
        else: # Si el brazo de la derecha es más pesado
            mayorPeso1 = 2

        # Aquí va el segundo intento
        brazoIzquierdo = sum(listaTotalMonedas[i].peso for i in [0,5,6,7]) # A la izquierda ponemos las monedas 1,6,7,8
        brazoDerecho = sum(listaTotalMonedas[i].peso for i in [4,9,10,11]) # A la derecha ponemos las monedas 5,10,11,12

        if brazoIzquierdo == brazoDerecho: # Si la balanza se equilibra, la moneda mala sólo puede ser 2,3,4
            # Aquí va el tercer intento
            monedaMalaSupuesta = descartarDeTres(list(listaTotalMonedas[i] for i in range(1,4)))

        else:
            if brazoIzquierdo > brazoDerecho:
                mayorPeso2 = 1
            else:
                mayorPeso2 = 2

            if mayorPeso1 == mayorPeso2: # Si se mantuvo el desbalance en el mismo sentido, la mala sólo puede ser la 1 o la 5
                # Aquí va el tercer intento
                monedaMalaSupuesta = descartarDeDos([listaTotalMonedas[0],listaTotalMonedas[4]],listaTotalMonedas[1])
            else: # Si el desbalance cambió al otro lado, la mala sólo puede ser la 6,7,8
                monedaMalaSupuesta = descartarDeTres(list(listaTotalMonedas[i] for i in range(5,8)))

    if monedaMalaSupuesta == numeroMoneda:
        return 1
    print(numeroMoneda)
    print(monedaMalaSupuesta)
    return 0

for numeroMoneda in range(1,13):
    if hacerIntentos(numeroMoneda,0) + hacerIntentos(numeroMoneda,2) != 2:
        print("Falló")
        sys.exit()

print("Se logró")
        
                
                

            
            

        

        
        
        

    
            
        

    

    


    
    

    
        

