# Tribonacci recursivo, pero no de cola.
# (Se lo pedí a Google Bard como recursivo de cola, pero me arrojó esto).
def tribonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return tribonacci_recursive(n - 1) + tribonacci_recursive(n - 2) + tribonacci_recursive(n - 3)

# Tribonacci recursivo de cola sugerido por Assistant
# También los sugirió así Bing Chat, sólo que para él esto es una función auxiliar, para que
# así los parámetros a, b y c no existan en la función que el usuario invoca.
def tribonacci_recursivo(n, a=0, b=1, c=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    return tribonacci_recursivo(n-1, b, c, a+b+c)

# Tribonacci como bucle sugerido por Assistant / ChatGPT
def tribonacci_iterativo_assistant(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b, c = 0, 1, 1
    for i in range(n-2): # También se puede poner range(2,n)
        a, b, c = b, c, a+b+c
    return c

# Tribonacci como bucle sugerido por Bing Chat
# Nota que la diferencia es que no retorna inmediatamente en los casos base.
def tribonacci_iterativo_bing(n):
    a = 0
    b = 1
    c = 1
    while n > 0:
        a, b, c = b, c, a+b+c
        n -= 1
    return a

# Tribonacci como bucle sugerido por Google Bard
# Esta solución sería la mejor si result fuera de entrada-salida, para
# que así no haya que repetir cálculos cuando se vuelva a llamar la función
# con otro número más grande.
def tribonacci_iterativo_bard(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    result = [0, 1, 1]
    for i in range(3, n):
        result.append(result[i - 1] + result[i - 2] + result[i - 3])
        
    return result[n - 1]
