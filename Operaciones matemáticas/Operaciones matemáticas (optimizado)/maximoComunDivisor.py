#
# Archivo: maximoComunDivisor.py
#
# Descripción: Programa que dado dos números, devuelve el máximo
#              común divisor entre ellos.
#
# Fecha de creación: 01/10/2017
# Última modificación: 23/11/2017

def maximoComunDivisor(m,n):
    """
    Entrada
        * m: primer número.
        * n: segundo número.
    Salida
        * mcd: máximo común divisor de los dos números. """
    m = abs(m)
    n = abs(n)
    minim = min(m,n)
    maximo = max(m,n)
    if minim == 0:
        return maximo
    elif minim == 1:
        return 1
    else:
        try:
            assert(m == int(m))
            assert(n == int(n))
        except:
            print("No son números enteros")
            sys.exit()
            
        m = int(m)
        n = int(n)
        for i in range(minim):
            mcd = minim-i
            if mcd == 1:
                return mcd
            else:
                if m%mcd == 0 and n%mcd == 0:
                    return mcd                                     
