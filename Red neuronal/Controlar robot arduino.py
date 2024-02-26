"""
http://www.aprendemachinelearning.com/crear-una-red-neuronal-en-python-desde-cero/

Nuestros datos de entrada serán:

Sensor de distancia al obstáculo
- si es 0 no hay obstáculos a la vista
- si es 0,5 se acerca a un obstáculo
- si es 1 está demasiado cerca de un obstáculo

Posición del obstáculo (izquierda,derecha)
- El obstáculo es visto a la izquierda será -1
- visto a la derecha será 1

Las salidas serán

Girar
    derecha 1 / izquierda -1
Dirección
    avanzar 1 / retroceder -1


Entrada:        Salida:
Sensor  Pos    
Dist    Osbt    Giro    Dir     Acción

0	0	0	1	Avanzar
0	1	0	1	Avanzar
0	-1	0	1	Avanzar
0.5	1	-1	1	Giro a la izquierda
0.5	-1	1	1	Giro a la derecha
0.5	0	0	1	Avanzar
1	1	0	-1	Retroceder
1	-1	0	-1	Retroceder
1	0	0	-1	Retroceder
-1	0	0	1	Avanzar
-1	-1	0	1	Avanzar
-1	1	0	1	Avanzar

"""
class globales:
    e = 2.718281828459045235360

# Función Sigmoide: caso especial de función logística
def g(z):
    1/(1+globales.e**(-z))

# Derivada de función Sigmoide
def g_prima(z):
    
