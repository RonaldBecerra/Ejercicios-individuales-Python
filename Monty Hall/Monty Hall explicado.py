from random import choice   # "choice" es una función predeterminada para elegir un valor aleatorio de una lista.
from random import shuffle  # "shuffle" es una función predeterinada para barajar los contenidos de una lista.

conjunto = ['Auto','Cabra','Cabra']   # Ésta es la lista de puertas con sus contenidos. En este momento, el carro está en la puerta 1.

class globales:
    vecesCambiando = 0      # Aquí acumularemos la cantidad de veces que gana cambiando

globales = globales()

# Función para el jugador que siempre se cambia
def jugarCambiando(conjunto):

    shuffle(conjunto)   # Barajamos los contenidos de las puertas, de modo que no siempre aparezcan en la misma posicion.
    
    numeros = [0,1,2]   # Índices de las puertas que el jugador puede elegir (el cero se refere a la puerta1, el 1 se refiere a la puerta2 ...)
                        # Ello porque este lenguaje siempre comienza a enumerar desde cero, no desde 1.
                        
                        # Entonces, para saber el contenido de la puerta 1, tendríamos que poner conjunto[0].
    
    eleccionInicial = choice(numeros)  # Aquí se determina qué número elige el jugador. 
                                       # Por ejemplo, supongamos que eleccionInicial es igual a 0. Mantendré este ejemplo para el resto de los casos.
    
    numeros.remove(eleccionInicial)    # Removemos ese número elegido para que no se repita en la elección siguiente
                                       # (porque dijimos que este jugador va a cambiar) y para que tampoco lo revele el presentador.
                                       # Por ejemplo, si el concursante eligió 0, la lista "numeros" quedaría ahora como [1,2]

    # Caso en que el jugador ha elegido la puerta correcta            
    if conjunto[eleccionInicial] == 'Auto':
        azar = choice(numeros)         # El presentador escoge el número de cualquiera de las otras dos puertas restantes (que tienen cabras) 
                                       # Ejemplo, el presentador elige 1.
                                       
        numeros.remove(azar)           # Removemos ese número de la lista "numeros", para que ya no sea posible escogerlo.
                                       # Como en el ejemplo el presentador escogió el 1, la lista de "numeros" queda ahora como [2]

    # Caso contrario: el jugador escogió una puerta con cabra. Eso significa que las otras dos puertas tiene un Auto y una Cabra.
    # Ahora tenemos que determinar cuál de las dos puertas restantes es la que tiene cabra, para que el presentador la revele
    else:
        if conjunto[numeros[0]] == 'Cabra':  # Aclaración: numeros[0] no se refiere al valor 0, sino al primer elemento que está en la lista "numeros".
                                             # Por ejemplo, si la lista quedó como [1,2], entonces numeros[0] = 1
                                             
            numeros.remove(numeros[0])       # Como esa puerta resultó tener cabra, ésa es la que vamos a revelar. 
                                             # En nuestro ejemplo de numeros = [1,2], como se eliminó el primer elemento, la lista quedó como [2].
        else:
            numeros.remove(numeros[1])       # Caso contrario. Resulta que conjunto[numeros[0]] tiene el auto, por lo que la puerta que debemos revelar es la otra.
                                             # Así que si "numeros" era [1,2], ahora queda como [1].

    # Nota que en este punto la lista "numeros" sólo tiene un elemento, ya que se removió de ella tanto la primera elección del 
    # concursante, como la puerta que revela el presentador. Por ejemplo, podría haber quedado [2].
    
    eleccionFinal = conjunto[numeros[0]] # Como el concursante va a cambiar su elección, entonces tiene que escoger la única puerta que quedó
                                         # en la lista numeros. Lo invocamos como numeros[0], por ser el primero (y el único).
                                         
    if eleccionFinal == 'Auto':          # Si la elección final tiene el premio, le añadimos una unidad al contador que acumula las veces
        globales.vecesCambiando +=1      # que se ha ganado cambiando.



for i in range(0,1000000):
    jugarCambiando(conjunto)
print("")
print("            1000000 INTENTOS")
print("            ----------------")
print("")
probabilidad = globales.vecesCambiando/1000000
print("La probabilidad de acertar si siempre se cambia es: "+str(probabilidad))





        
        
