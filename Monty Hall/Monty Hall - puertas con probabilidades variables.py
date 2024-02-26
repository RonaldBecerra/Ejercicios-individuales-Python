"""
Se desea ver cuál es la probabilidad de ganar cambiando y no haciéndolo
en el juego de Monty Hall en el caso de que las puertas no tengan inicialmente
la misma probabilidad de contener el carro, sino cada una una
probabilidad asignada por el usuario
"""
import sys, random

def determinarProbabilidadesPuertas():
    TOL = 0.001
    probPuertas = [1/3,1/3,1/3]

    print("Ingrese las probabilidades de las puertas")
    print("Puede hacerlo con fracciones, o indicando un símbolo de % al final")
    print("")
    for i in range(3):
        while True:
            try:
                # El método "strip" elimina los espacios en blanco al final
                entrada = input("> Probabilidad puerta "+str(i+1)+" = ").strip()
                
                if entrada[len(entrada)-1] == "%":
                    entrada = entrada[:-1]
                    probabilidad = float(eval(entrada))/100
                else:
                    probabilidad = float(eval(entrada))
     
                assert(0 <= probabilidad and probabilidad <= 1)
                probPuertas[i] = probabilidad
                break
            except:
                print("Valor no válido\n")

    try:
        assert(abs(sum(probPuertas) - 1) < TOL)
        print("")
    except:
        print("La suma de las probabilidades no es cercana a 1 o 100%")
        sys.exit()

    return probPuertas

def asignarContenidosAPuertas(probPuertas):
    aleatorio = random.uniform(0,1)

    if aleatorio < probPuertas[0]:
        return ["carro", "cabra", "cabra"], 0
    if aleatorio < probPuertas[0] + probPuertas[1]:
        return ["cabra", "carro", "cabra"], 1
    return ["cabra", "cabra", "carro"], 2

def jugarSeleccionandoPuerta(numPuertaJugador, probPuertas):
    puertas, premio = asignarContenidosAPuertas(probPuertas)

    # Determinar las puertas que el presentador tiene disponibles para revelar
    puertasRevelar = [0,1,2]
    puertasRevelar.remove(numPuertaJugador)
    try:
        puertasRevelar.remove(premio)
    except:
        pass
    puertaAbierta = random.choice(puertasRevelar)

    # Verificación de error de puerta abierta
    try:
        assert(puertas[puertaAbierta] == "cabra")
    except:
        print("La puerta abierta no tiene cabra")
        sys.exit()

    # Determinar la puerta a la que el jugador se puede cambiar
    puertasSeleccionables = [0,1,2]
    puertasSeleccionables.remove(numPuertaJugador)
    puertasSeleccionables.remove(puertaAbierta)

    # Resultados
    seGanaManteniendo = 1 if puertas[numPuertaJugador] == "carro" else 0
    seGanaCambiando   = 1 if puertas[puertasSeleccionables[0]] == "carro" else 0

    # Verificación de error de que los resultados no son complementarios
    try:
        assert(seGanaManteniendo != seGanaCambiando)
    except:
        print("No se cumple que una de las dos puertas finales tiene cabra y la otra, carro")
        sys.exit()

    return {"noCambiando": seGanaManteniendo, "cambiando": seGanaCambiando, "puertaAbierta": str(puertaAbierta)}

def crearDiccionarioResultados(puertaJugador):
    diccionario = {}
    for i in range(3):
        if i == puertaJugador:
            continue
        diccionario[str(i)] = {"noCambiando":0, "cambiando":0}
    return diccionario

def jugar():
    probPuertas = determinarProbabilidadesPuertas()
    NUM_INTENTOS = 1000000

    for puertaJugador in range(3):
        diccionarioResultados = crearDiccionarioResultados(puertaJugador)
        
        for i in range(NUM_INTENTOS):
            intentoActual = jugarSeleccionandoPuerta(puertaJugador, probPuertas)
            elemDiccionario = diccionarioResultados[intentoActual["puertaAbierta"]]
            elemDiccionario["cambiando"] += intentoActual["cambiando"]
            elemDiccionario["noCambiando"] += intentoActual["noCambiando"]

        print("\nCuando se selecciona la puerta "+str(puertaJugador+1)+":")
        for clave in diccionarioResultados:
            elemDiccionario = diccionarioResultados[clave]
            totalIntentos = elemDiccionario["cambiando"] + elemDiccionario["noCambiando"]
            print("    Al abrir la puerta "+str(int(clave)+1)+":")
            print("        Prob. de ganar CAMBIANDO es: "+str(elemDiccionario["cambiando"]/totalIntentos))
            print("        Prob. de ganar manteniendo es: "+str(elemDiccionario["noCambiando"]/totalIntentos))
            

    
    
    

    
    
    
        
        
    
