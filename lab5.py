# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:16:22 2023

@author: Manuel Mora Cartagena
"""

import numpy as np
import matplotlib.pyplot as plt


#Funciones
#Define la función a integrar
def f(x):
    return (np.sin(1/(x*(2-x))))**2


#Define otra función a integrar
def g(x):
    return np.e**-x**2


#Define las funciones para el circulo de radio 1
def circulo_positivo(x):
    return np.sqrt(1 - x**2)

def circulo_negativo(x):
    return -np.sqrt(1 - x**2)


#Define el método Monte Carlo
def Monte_Carlo(maximo, N, f):
    #Parámetros de entrada a la función:
    #maximo -> Valor máximo del rectángulo
    #N -> número de pasos Monte Carlo, es decir, el número de puntos aleatorios
    #Defino una semilla para quitar aleatoridad en cada iteración en el bucle del apartado 3
    semilla = 5 
    np.random.seed(semilla)
    x = np.random.uniform(1e-5, 2, N) #Define un array de N números aleatorios entre 0 y 2 para la coordenada x
    y = np.random.uniform(1e-5, maximo, N) #Define un array de N números aleatorios entre 0 y maximo para la coordenada y
    n = 0 #Define el contador de puntos por debajo de la función
    x_aceptados = []
    y_aceptados = []
    for i in range(N): #Define un bucle para comparar punto a punto
        if y[i] <= f(x[i]): #Si el punto está por debajo de la función añadimos 1 al contador
            n += 1
            x_aceptados.append(x[i])
            y_aceptados.append(y[i])
        else:
            None
    A = (2-0)*maximo #Define el valor del área del rectángulo 
    I = (maximo*(2-0))*(n/N) #Define el valor de la integral
    error = (np.sqrt(I*(A-I)))/np.sqrt(N) #Define el valor del error
    return I, error, x_aceptados, y_aceptados


#Define el método Monte Carlo para circulo de radio 1
def Monte_Carlo_circulo(N):
    #Parámetros de entrada a la función:
    #N -> número de pasos Monte Carlo, es decir, el número de puntos aleatorios
    x = np.random.uniform(-1, 1, N) #Define un array de N números aleatorios entre 0 y 2 para la coordenada x
    y = np.random.uniform(-1, 1, N) #Define un array de N números aleatorios entre 0 y maximo para la coordenada y
    n = 0 #Define el contador de puntos dentro del circulo
    x_aceptados = []
    y_aceptados = []
    for i in range(N): #Define un bucle para comparar punto a punto
        if x[i]**2 + y[i]**2 <= 1: #Si el punto está dentro del circulo añadimos 1 al contador
            n += 1
            x_aceptados.append(x[i])
            y_aceptados.append(y[i])
        else:
            None
    A = 2**2 #Define el valor del área del cuadrado
    I = A*(n/N) #Define el valor de la integral
    error = (np.sqrt(I*(A-I)))/np.sqrt(N) #Define el valor del error
    return I, error, x_aceptados, y_aceptados


#Define el método Monte Carlo para una hiperesfera de dimensión 10
def Monte_Carlo_hiperesfera(N):
    #Parámetros de entrada a la función:
    #N -> número de pasos Monte Carlo, es decir, el número de puntos aleatorios
    r = np.random.uniform(-1, 1, (10, N)) #Define un array de 10 y N columnas de números aleatorios para cada coordenada
    n = 0 #Define el contador de puntos dentro de la hiperesfera
    for i in range(N):
        if r[0, i]**2  + r[1, i]**2 + r[2, i]**2 + r[3, i]**2 + r[4, i]**2 + r[5, i]**2 + r[6, i]**2 + r[7, i]**2 + r[8, i]**2 + r[9, i]**2 <= 1: #Si el punto está dentro de la hiperesfera añadimos 1 al contador
            n += 1
        else:
            None
    A = 2**10 #Define el valor del área del hipercuadrado
    I = A*(n/N)
    error = (np.sqrt(I*(A-I)))/np.sqrt(N) #Define el valor del error
    return I, error


#Inputs
maximo = float(input('Introduce el valor máximo de la función: ')) #Define el valor máximo del rectángulo
N = int(input('Introduce el número de pasos de Monte Carlo: ')) #Define el número de pasos Monte Carlo, es decir, el número de puntos aleatorios



resultados = Monte_Carlo(maximo, N, f) #Define un array con los resultados para f 

#Representación de la función entre 0 y 2
intervalo = np.linspace(1e-5, 1.999, 100)
plt.figure()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('$f(x) = sin^2 \dfrac{1}{x(2-x)}$')
plt.plot(intervalo, f(intervalo), color = 'blue')
plt.show()

#Calculo del valor de la integral y su error
print('El valor de la integral para f(x) es ' + str(np.round(resultados[0], 4)) + ' y su error es ' + str(np.round(resultados[1], 4)))

#Representación  de la función entre 0 y 2 junto con los valores aceptados
intervalo = np.linspace(1e-5, 1.999, 100)
plt.figure()
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('$f(x) = sin^2 \dfrac{1}{x(2-x)}$ junto con los valores aceptados')
plt.plot(intervalo, f(intervalo), color = 'blue', label = 'f(x)')
plt.plot(resultados[2], resultados[3], 'o', color = 'red', label = 'aceptados')
plt.legend(loc = 'best')
plt.show()

#Representación valor de la integral y el error  en función del número de pasos
integrales = []
errores = []
pasos = np.arange(2000, 100500, 500)
for i in pasos:
    valores = Monte_Carlo(maximo, i, f)    
    integrales.append(valores[0])
    errores.append(valores[1])

#Integral
plt.figure()
plt.xlabel('$pasos$')
plt.ylabel('$I$')
plt.title('Valor de la integral en función del número de pasos')
plt.plot(pasos, integrales, color = 'blue', label = 'Integral')
plt.legend(loc = 'best')
plt.show()

#Error
plt.figure()
plt.xlabel('$pasos$')
plt.ylabel('$\sigma$')
plt.title('Error en función del número de pasos')
plt.plot(pasos, errores, color = 'red', label = 'Error')
plt.legend(loc = 'best')
plt.show()



'''
PRECAUCIÓN: ESTE APARTADO TARDA MUCHO TIEMPO
'''
'''
#Representación del valor de la integral y el error en función del valor maximo del rectángulo
integrales_maximos = []
errores_maximos = []
maximos = np.arange(2, 201, 10)
for i in maximos:
    valores_maximos = Monte_Carlo(i, N, f)
    integrales_maximos.append(valores_maximos[0])
    errores_maximos.append(valores_maximos[1])

#Integral
plt.figure()
plt.xlabel('valor máximo')
plt.ylabel('$I$')
plt.title('Valor de la integral en función del valor máximo del rectángulo')
plt.plot(maximos, integrales_maximos, color = 'blue', label = 'Integral')
plt.legend(loc = 'best')
plt.show()

#Error
plt.figure()
plt.xlabel('valor máximo')
plt.ylabel('$\sigma$')
plt.title('Error en función del del valor máximo del rectángulo')
plt.plot(maximos, errores_maximos, color = 'red', label = 'Error')
plt.legend(loc = 'best')
plt.show()
'''

'''
EXTRA 1 : Repito todos los apartados con otra función sin solución analítica sencilla
'''

resultados2 = Monte_Carlo(maximo, N, g) #Define un array con los resultados para g

#Representación de la función entre 0 y 2
intervalo = np.linspace(1e-5, 1.999, 100)
plt.figure()
plt.xlabel('$x$')
plt.ylabel('$g(x)$')
plt.title('$g(x) = e^{-x^2}$')
plt.plot(intervalo, g(intervalo), color = 'blue')
plt.show()


#Calculo del valor de la integral y su error
print('El valor de la integral para g(x) es ' + str(np.round(resultados2[0], 4)) + ' y su error es ' + str(np.round(resultados2[1], 4)))

#Representación  de la función entre 0 y 2 junto con los valores aceptados
intervalo = np.linspace(1e-5, 1.999, 100)
plt.figure()
plt.xlabel('$x$')
plt.ylabel('$g(x)$')
plt.title('$g(x) = e^{-x^2}$ junto con los valores aceptados')
plt.plot(intervalo, g(intervalo), color = 'blue', label = 'g(x)')
plt.plot(resultados2[2], resultados2[3], 'o', color = 'red', label = 'aceptados')
plt.legend(loc = 'best')
plt.show()

#Representación valor de la integral y el error en función del número de pasos
integrales2 = []
errores2 = []
pasos = np.arange(2000, 100500, 500)
for i in pasos:
    valores2 = Monte_Carlo(maximo, i, g)    
    integrales2.append(valores2[0])
    errores2.append(valores2[1])

#Integral
plt.figure()
plt.xlabel('$pasos$')
plt.ylabel('$I$')
plt.title('Valor de la integral en función del número de pasos')
plt.plot(pasos, integrales2, color = 'blue', label = 'Integral')
plt.legend(loc = 'best')
plt.show()

#Error
plt.figure()
plt.xlabel('$pasos$')
plt.ylabel('$\sigma$')
plt.title('Error en función del número de pasos')
plt.plot(pasos, errores2, color = 'red', label = 'Error')
plt.legend(loc = 'best')
plt.show()


'''
EXTRA 2 : Calcular el area de una circunferecnia de radio 
'''

resultados_circulo = Monte_Carlo_circulo(N) #Define un array con los resultados para el circulo 

#Calculo del valor de la integral y su error
print('El valor de la integral para el círculo de radio 1 es ' + str(np.round(resultados_circulo[0], 4)) + ' y su error es ' + str(np.round(resultados_circulo[1], 4)))

#Representación del círculo de radio 1
intervalo_circulo = np.arange(-1, 1+1/50000, 1/5000)
plt.figure()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Círculo de radio 1')
plt.plot(intervalo_circulo, circulo_positivo(intervalo_circulo), color = 'blue', label = '$x^2 + y^2 = 1$')
plt.plot(intervalo_circulo, circulo_negativo(intervalo_circulo), color = 'blue')
plt.legend(loc = 'upper left')
plt.show()



#Representación del círculo de radio 1 con los valores aceptados
intervalo_circulo = np.arange(-1, 1+1/50000, 1/5000)
plt.figure()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Círculo de radio 1 junto con aceptados')
plt.plot(intervalo_circulo, circulo_positivo(intervalo_circulo), color = 'blue', label = '$x^2 + y^2 = 1$')
plt.plot(intervalo_circulo, circulo_negativo(intervalo_circulo), color = 'blue')
plt.plot(resultados_circulo[2], resultados_circulo[3], 'o', color = 'red', label = 'aceptados')
plt.legend(loc = 'upper left')
plt.show()


'''
EXTRA 2 (Continuación): Generalización a 10 dimensiones del apartado anterior para una hiperesfera de dimension 10
'''

resultados_hiperesfera = Monte_Carlo_hiperesfera(N)

#Calculo del valor de la integral y su error
print('El valor de la integral para la hiperesfera de dimensión 10 es ' + str(np.round(resultados_hiperesfera[0], 4)) + ' y su error es ' + str(np.round(resultados_hiperesfera[1], 4)))

  
