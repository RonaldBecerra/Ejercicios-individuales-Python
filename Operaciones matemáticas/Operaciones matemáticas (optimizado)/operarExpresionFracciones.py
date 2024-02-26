#
# Archivo: operarExpresionFracciones.py
#
# Descripción: Archivo que permite operar dos o más fracciones sin tener que
#              utilizar números en punto flotante. Devuelve un entero o una
#              fracción.
#
# Modo de uso: Se deben escribir fracciones de la forma a/b, operadas por
#           cualquiera de los operadores +,-,*,:, y dejando un espacio entre
#           cada fracción y el operador. No se permite parentización.
#           Ejemplo:
#
#           5/6 + 3/4 * 7/8 - 25/5 : 5/6 + 5
#
#           El programa asume que la entrada es correcta.
#
# Fecha: 01/10/2017
# Última modificación: 23/11/2017

import sys
from OperacionesBasicas_fracciones import *

entrada = input("Escriba la operación\n")

############################################################################
#############  I N I C I A L I Z A R   F R A C C I O N E S  ################
#############          Y   O P E R A C I O N E S            ################
############################################################################


listaFracciones = []
listaOperadores = []

nuFraccion = fraccion()
numerador = True
numero = 0
operador = False
signo = False

for it in range(len(entrada)):
    c = entrada[it]
    if c == " ":
        if not operador:
            if signo:
                numero = (-1)*numero
            if numerador:
                nuFraccion.numerador = numero
            else:
                nuFraccion.denominador = numero
            numero = 0
            signo = False
            listaFracciones.append(nuFraccion)
        else:
            operador = False
            nuFraccion = fraccion() 
    elif c in ["+","*",":"]:
        numerador = True
        listaOperadores.append(c)
        operador = True
    elif c == "-":
        numerador = True
        if entrada[it+1] == " ":
            listaOperadores.append(c)
            operador = True
        else:
            signo = True
    elif c == "/":
        if not numerador:
            print("Error")
            sys.exit()
        else:
            numerador = False
            if signo:
                numero = (-1)*numero
            nuFraccion.numerador = numero
            numero = 0
            signo = False
    else:
        try:
            n = int(c)
            numero *= 10
            numero += n
        except:
            print("Error")
            sys.exit()


if nuFraccion.numerador == None:
    if signo:
        numero = (-1)*numero
    nuFraccion.numerador = numero
elif not numerador:
    nuFraccion.denominador = numero
    
listaFracciones.append(nuFraccion)

############################################################################
#######################        O P E R A R       ###########################
############################################################################




############################################################################
############        P R O G R A M A   P R I N C I P A L        #############
############################################################################

fraccionFinal = operar(listaFracciones,listaOperadores)
print("")
print("El resultado es: ")
if fraccionFinal.denominador == 1:
    print(fraccionFinal.numerador)
else:
    print(str(fraccionFinal.numerador)+"/"+str(fraccionFinal.denominador))
            
                
            
        
        
        
