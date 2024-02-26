class globales:
    factoriales = [1,1]           # Irá almacenando los factoriales calculados
    maximoFactorialGuardado = 1   # Valor de entrada máximo para el cual se ha calculado el factorial

# Función para determinar el factorial de manera optimizada
# (va guardando los valores calculados).
def fact(n,globales):
    maximo = globales.maximoFactorialGuardado
    factoriales = globales.factoriales
    if n <= maximo:
        return factoriales[n]
    else:
        res = factoriales[maximo]
        for i in range(maximo, n+1):
            res *= i
            factoriales.append(res)
        globales.maximoFactorialGuardado = n
        return res
