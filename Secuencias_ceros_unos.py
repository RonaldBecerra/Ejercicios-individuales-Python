# La idea aquí es calcular el número de secuencias de ceros y
# unos de tamaño N que no contienen el patrón 010

LIM = 5

#################################################################################
##########################  F U E R Z A   B R U T A  ############################
#################################################################################

# Arreglo donde cada elemento i indica el número de secuencias 
# de tamaño i que no contienen el patrón 010
num_secuencias = [0] * (LIM+1)

# Arreglo donde cada elemento i es una lista, que guardará las secuencias de
# tamaño i que no contienen el patrón 010
lista_secuencias_validas = []
for i in range(LIM+1):
    lista_secuencias_validas.append([])


def generar_secuencias(N, n=0, sec="", secPrevValida=True):
    """
    Parámetros:
        N:   tamaño máximo que puede tener la secuencia
        n:   tamaño actual de la secuencia
        sec: secuencia actual de ceros y unos
        secPrevValida: verdadero si la secuencia acumulada antes no contenía el patrón 010
    """
    secValida = secPrevValida
    if secValida:
        if sec[-3:] != "010":
            num_secuencias[n] += 1
            #lista_secuencias_validas[n].append(sec)
        else:
            secValida = False

    if n < N:
        generar_secuencias(N, n+1, sec + "0", secValida)
        generar_secuencias(N, n+1, sec + "1", secValida)

generar_secuencias(LIM)
# Función lambda para imprimir el arreglo número de secuencias
print(*map(lambda i: [i, num_secuencias[i]], range(LIM+1)), sep="\n")

#################################################################################
###########################  R E C U R R E N C I A  #############################
#################################################################################

"""
Sugerido por Bing Chat, aunque tuve que indicarle algunos errores.

Usamos una técnica llamada programación dinámica, que consiste en dividir el problema en
subproblemas más pequeños y guardar sus soluciones para reutilizarlas.

Definimos una función f(n, b) que nos dice el número de secuencias de tamaño n que terminan
en el bit b (0 o 1) y que no contienen el patrón 010.
(Aunque yo le agrego que b signifique cualquier subcadena, no sólo un bit).

Entonces, la respuesta al problema original sería f(n, 0) + f(n, 1),
es decir, el número de secuencias que terminan en 0 más el número de
secuencias que terminan en 1.

Para calcular f(n, b), podemos usar la siguiente recurrencia:

- Si b = 0, entonces f(n, 0) = f(n-1, 0) + f(n-1, 11), porque podemos agregar un 0 al final
  de una secuencia válida de tamaño n-1 que termine en 0, o de una secuencia válida de tamaño
  n-1 que termine en 11, Pero nota que f(n-1, 11) = f(n-2, 1), porque sólo hay que agregarles
  un 1 a las segundas para obtener las primeras.

- Si b = 1, entonces f(n, 1) = f(n-1, 0) + f(n-1, 1), porque podemos agregar un 1
  al final de cualquier secuencia válida de tamaño n-1.

Además, necesitamos unos casos base para iniciar la recurrencia:

f(1, 0) = f(1, 1) = 1, porque hay una sola secuencia válida de tamaño 1 que termina en cada bit.
f(2, 0) = f(2, 1) = 2, porque hay dos secuencias válidas de tamaño 2 que terminan en cada bit:
                       00, 10 para el bit 0 y 01, 11 para el bit 1.
"""
def contar_secuencias(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    # Crear una tabla para guardar los valores de f(n, b)
    tabla = [[0 for b in range(2)] for i in range(n+1)]

    # Casos base
    tabla[1][0] = tabla[1][1] = 1
    tabla[2][0] = tabla[2][1] = 2

    if n > 2:
        # Recurrencia
        for i in range(3, n+1):
            tabla[i][0] = tabla[i-1][0] + tabla[i-2][1]
            tabla[i][1] = tabla[i-1][0] + tabla[i-1][1]
            
    # Respuesta
    return tabla[n][0] + tabla[n][1]

print("")
# Probar la función con algunos valores de n
for i in range(LIM+1):
    print([i, contar_secuencias(i)])


#################################################################################
#############################  D E P R E C A D O  ###############################
#################################################################################
def contiene_patron_010(sec):
    """
    Determina si una secuencia dada tiene el patrón 010
    
    Parámetro:
        sec: Secuencia a analizar.
    """
    patron = ""
    for elem in sec:
        if elem == "0":
            if patron == "":
                patron = elem
            elif patron == "01":
                return True
        elif elem == "1":
            if patron == "0":
                patron += elem
            elif patron == "01":
                patron = ""         
    return False
         
