#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Archivo: Red neuronal.py
# Descripción: 
# Motivo: Me interesan las redes neuronales.
# Fecha: 12/02/2017

import numpy as np

class Red_neuronal(object):
    def __init__(self):
        # Definimos los parámetros generales
        self.numeroNeuronasEntrada = 2
        self.numeroNeuronasSalida = 1
        self.numeroNeuronasEscondidas = 3

        # Se definen los pesos de manera aleatoria
        # Los pesos w1 están entre la capa de entrada y la escondida
        # Con rand es posible generar una matriz de valores aleatorios entre 0 y 1
        # Primer parámetro: filas; segundo: columnas
        self.W1 = np.random.rand(self.numeroNeuronasEntrada,self.numeroNeuronasEscondidas)

        # Los pesos w2 están entre la capa escondida y la de salida
        self.W2 = np.random.rand(self.numeroNeuronasEscondidas, numeroNeuronasSalida)

        # X es la matriz de entradas
        # W es la matriz de pesos
        # Z será el resultado de actividad neuronal

    def avanzar(self,x):
        # Entregamos muchos parámetros en forma de matriz
        # dot permite multiplicar dos matrices

        self.z2 = np.dot(x, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        ySombrero = self.sigmoid(self.z3)
        return ySombrero

    def sigmoid(self,x):
        # Aplica la función sigmoide sobre una matriz
        return 1/(1+np.exp(-x))

    """Es necesario minimizar el costo del error provocado por los pesos.
    Para esto será necesario corregirlos mediante el descenso del gradiente.
    Para esto es necesario derivar el costo con respecto al peso δC/δW = mínimo costo.
    Los calculamos de manera separada para los pesos W1 y los W2. """

    # Obtenemos la derivada de la función sigmoide
    def sigmoidPrima(self,x):
        return np.exp(-x)/((1+np.exp(-x))**2)

    # Para obtener la función de costo entonces
    def FuncionDeCosto(self,x,y):

        # Obtenemos el valor de y sombrero
        self.yHat = self.avanzar(x)

        # Retornamos el valor 0.5* (y - y*)^2
        J = 0.5 * sum((y-self.yHat)**2)
        return J

    # Obtenemos la derivada de la función de costo
    def FuncionDeCostoPrima(self,x,y):

        # Obtendremos el valor de y sombrero
        self.yHat = self.avanzar(x)

        # Posteriormente obtendremos el valor de delta definido como
        # delta = -(y - y*)
        delta3 = np.multiply(-(y - self.yHat), self.sigmoidPrima(self.z3) )

        # Por último multiplicamos la matriz de activaciones traspuesta
        # para que concuerden las dimensionalidades de las matrices
        # ya que la matriz delta3 es una matriz de 3 filas y 1 columna que representa
        # multiplicados de los resultados tanto esperados como resueltos por el algoritmo
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrima(self.z2)
        dJdW1 = np.dot(x.T, delta2)

        return dJdW1, dJdW2


    
