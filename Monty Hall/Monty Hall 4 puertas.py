from random import choice

class resultados:
    def __init__(self):
        self.intentosTotales = 0  # Cantidad de intentos que se juega
        self.ganadasTotales = 0   # Cantidad de juegos en los que se gana
        
        self.intentosPrimeraPuertaTotales = 0  # Intentos totales en los que el concursante se queda con su primera elección
        self.intentosSegundaPuertaTotales = 0  # Intentos totales en los que el concursante se queda con su segunda elección 
        self.intentosTerceraPuertaTotales = 0  # Intentos totales en los que el concursante se queda con su tercera elección
        
        self.ganadasPrimeraPuertaTotales = 0   # Cantidad de juegos totales en los que se gana con la primera elección
        self.ganadasSegundaPuertaTotales = 0   # Cantidad de juegos totales en los que se gana con la segunda elección
        self.ganadasTerceraPuertaTotales = 0   # Cantidad de juegos totales en los que se gana con la tercera elección

        self.intentosSegundaPuertaAbrioPrimera = 0 # Intentos en los que el concursante se queda con su segunda elección, y el presentador revela la que había escogido antes
        self.intentosSegundaPuertaAbrioOtra = 0    # Intentos en los que el concursante se queda con su segunda elección, y el presentador otra que no sea la original
        self.intentosTerceraPuertaAbrioPrimera = 0 # Intentos en los que el concursante cambia dos veces, y el presentador revela la que había escogido al principio
        self.intentosTerceraPuertaAbrioOtra = 0    # Intentos en los que el concursante cambia dos veces, y el presentador revela otra que no sea la original

        self.ganadasSegundaPuertaAbrioPrimera = 0  # Cantidad de juegos totales en los que se gana con la segunda elección, dado que el presentador reveló la original
        self.ganadasSegundaPuertaAbrioOtra = 0     # Cantidad de juegos totales en los que se gana con la segunda elección, dado que el presentador reveló otra
        self.ganadasTerceraPuertaAbrioPrimera = 0  # Cantidad de juegos totales en los que se gana con la tercera elección, dado que el presentador reveló la original
        self.ganadasTerceraPuertaAbrioOtra = 0     # Cantidad de juegos totales en los que se gana con la tercera elección, dado que el presentador reveló otra
       

def partidaSePuedeRevelarPrimera(puertaUtilizar,resultados):
    """ Una vez que el concursante cambia la primera puerta,
        el presentador puede revelar esa primera elección.

        "puertaUtilizar" es un número entero del 1 al 3, que significa con
        cuál elección el concursante se va a quedar: su primera puerta,
        su segunda o suu tercera. """

    resultados.intentosTotales += 1 # Hubo un intento más
    
    # Distribuimos los premios entre las puertas
    listaPremios = ["car","goat","goat","goat"]
    puertas = []
    while listaPremios != []:
        elemento = choice(listaPremios)
        puertas.append(elemento)
        listaPremios.remove(elemento)

    # Determinamos cuáles son los números de puertas que el presentador puede revelar (las que tienen cabras)
    presentadorPuedeRevelar = []
    for i in range(4):
        if puertas[i] == "goat":
            presentadorPuedeRevelar.append(i)

    # Determinar la primera puerta que escoge el concursante
    posiblesElecciones = [0,1,2,3]
    eleccion1 = choice(posiblesElecciones)

    ###### Caso en que el concursante se queda con su primera elección
    if puertaUtilizar == 1:
        resultados.intentosPrimeraPuertaTotales += 1
        if puertas[eleccion1] == "car":
            resultados.ganadasTotales += 1
            resultados.ganadasPrimeraPuertaTotales += 1
        return None

    # El presentador no puede revelar la puerta que el concursante escogió
    if eleccion1 in presentadorPuedeRevelar:
        presentadorPuedeRevelar.remove(eleccion1)
    posiblesElecciones.remove(eleccion1) # El concursante ya no puede volver a escoger de momento la misma puerta que tenía al principio

    # Se escoge cuál es la primera puerta que el presentador revela
    puertaRevelada1 = choice(presentadorPuedeRevelar) 
    presentadorPuedeRevelar.remove(puertaRevelada1)   # El presentador ya no puede volver a revelar esa misma puerta
    posiblesElecciones.remove(puertaRevelada1)        # El concursante ya no puede escoger la puerta que acaba de ser revelada

    # Determinar la segunda puerta que escoge el concursante
    eleccion2 = choice(posiblesElecciones)
    posiblesElecciones.remove(eleccion2) # El concursante ya no puede volver a escoger esta segunda puerta,
    posiblesElecciones.append(eleccion1) # pero tal vez sí podría volver a escoger la del principio.

    # El presentador ya no puede revelar la segunda puerta que escogió el concursante
    if eleccion2 in presentadorPuedeRevelar:
        presentadorPuedeRevelar.remove(eleccion2)
    # Pero tal ve podría revelar la primera que el jugador había escogido, en caso de que tenga cabra
    if puertas[eleccion1] == "goat":
        presentadorPuedeRevelar.append(eleccion1)

    # Se escoge cuál es la segunda puerta que el presentador revela
    puertaRevelada2 = choice(presentadorPuedeRevelar)
    posiblesElecciones.remove(puertaRevelada2)       # El concursante ya no puede escoger la puerta que acaba de ser revelada

    ###### Caso en que el concursante se queda con su segunda elección
    if puertaUtilizar == 2:
        resultados.intentosSegundaPuertaTotales += 1
        
        # Determinar qué tipo de intento es éste
        if puertaRevelada2 == eleccion1:
            resultados.intentosSegundaPuertaAbrioPrimera += 1
        else:
            resultados.intentosSegundaPuertaAbrioOtra += 1

        # Determinar si hubo victoria o no, y sumar un intento más al caso correspondiente
        if puertas[eleccion2] == "car":
            resultados.ganadasTotales += 1
            resultados.ganadasSegundaPuertaTotales += 1
            if puertaRevelada2 == eleccion1:
                resultados.ganadasSegundaPuertaAbrioPrimera += 1
            else:
                resultados.ganadasSegundaPuertaAbrioOtra += 1

        return None

    # El concursante escoge la tercera puerta
    resultados.intentosTerceraPuertaTotales += 1
    eleccion3 = choice(posiblesElecciones)

    if puertaRevelada2 == eleccion1:
        resultados.intentosTerceraPuertaAbrioPrimera += 1
    else:
        resultados.intentosTerceraPuertaAbrioOtra += 1

    if puertas[eleccion3] == "car":
        resultados.ganadasTotales += 1
        resultados.ganadasTerceraPuertaTotales += 1
        if puertaRevelada2 == eleccion1:
            resultados.ganadasTerceraPuertaAbrioPrimera += 1
        else:
            resultados.ganadasTerceraPuertaAbrioOtra += 1
            
            
        
    

    
posiblesEstrategias = [1,2,3]
resultados = resultados()
for i in range(10000000):
    puertaUtilizar = choice(posiblesEstrategias)
    partidaSePuedeRevelarPrimera(puertaUtilizar,resultados)

# Imprimir resultados
print("0) La probabilidad de ganar usando aleatoriamente cualquier estrategia es: "+str(resultados.ganadasTotales / resultados.intentosTotales))
print("1) La probabilidad de ganar manteniendo la primera puerta es: "+str(resultados.ganadasPrimeraPuertaTotales / resultados.intentosPrimeraPuertaTotales))

print("2) La probabilidad de ganar en total manteniendo la segunda puerta es: "+str(resultados.ganadasSegundaPuertaTotales / resultados.intentosSegundaPuertaTotales))
print("   2.1) La probabilidad de ganar manteniendo la segunda puerta una vez que se reveló la original es: "+str(resultados.ganadasSegundaPuertaAbrioPrimera / resultados.intentosSegundaPuertaAbrioPrimera))
print("   2.2) La probabilidad de ganar manteniendo la segunda puerta una vez que se reveló otra que no es la original es: "+str(resultados.ganadasSegundaPuertaAbrioOtra / resultados.intentosSegundaPuertaAbrioOtra))

print("3) La probabilidad de ganar en total con la tercera puerta es: "+str(resultados.ganadasTerceraPuertaTotales / resultados.intentosTerceraPuertaTotales))
print("   3.1) La probabilidad de ganar con la tercera puerta una vez que se reveló la original es: "+str(resultados.ganadasTerceraPuertaAbrioPrimera / resultados.intentosTerceraPuertaAbrioPrimera))
print("   3.2) La probabilidad de ganar con la tercera puerta una vez que se reveló otra que no es la original es: "+str(resultados.ganadasTerceraPuertaAbrioOtra / resultados.intentosTerceraPuertaAbrioOtra))
    
