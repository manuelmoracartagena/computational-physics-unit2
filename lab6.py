# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:41:46 2023

@author: Manuel Mora Cartagena
"""


import numpy as np
import matplotlib.pyplot as plt


#Funciones
def E(nx, ny, nz):
    return (np.pi**2*hbar**2*(nx**2+ny**2+nz**2))/(2*m*L)

#Parámetros
hbar = 1 #Define el valor de h barra
m = 1 #Define la masa del gas
L = 1 #Define la longitud de la caja
contador = 1 #Define un contador para saber en que paso Monte Carlo se está en cada iteración

#Inputs
N = int(input('Introduce el número de particulas: ')) #Define el número de particulas del sistema
KT = float(input('Introduce el valor de KT: ')) #Define el valor de la temperatura
pasos_totales = int(input('Introduce el valor de pasos Monte Carlo: ')) #Define el número de pasos Monte Carlo

#Calculo la energía inicial del sistema con todas las partículas en el estado de mínima energía
E0 = N*E(1, 1, 1)
energias = [] #Define una lista para guardar la energía en cada paso Monte Carlo
energias.append(E0) #Añado la energía inicial a la lista de energias
numeros = np.ones((N, 3)) #Define un array de N filas y 3 columnas para los numeros cuánticos de todas las partículas

#Méotodo Metropolis Monte Carlo
continua = True
while continua:
    if contador >= pasos_totales:
        continua = False
    else:
        continua = True
        i = np.random.randint(0, N) #Define el número aleatorio para la partícula que va a cambiar de estado
        j = np.random.randint(0, 3) #Define el número aleatorio para la dirección del número cuántico que va a cambiar de estado
        cambio = np.random.choice([-1 ,1]) #Define aleatoriamente si el siguiente estado es +1 o -1
        R = np.random.uniform(0, 1) #Define un valor aleatorio entre 0 y 1 para la distrbución de Boltzmann
        if numeros[i, j] == 1:
            if cambio == -1:
                energias.append(E0)
                contador += 1
            else:
                E1 = E0 + (np.pi**2*hbar**2*(2*numeros[i, j] + 1))/(2*m*L)
                if E1 < E0:
                    E0 = E1
                    energias.append(E0)
                    numeros[i, j] += cambio
                    contador += 1
                elif np.exp(-(E1-E0)/(KT)) > R:
                    E0 = E1
                    energias.append(E0)
                    numeros[i, j] += cambio
                    contador += 1
                else:
                    energias.append(E0)
                    contador += 1
        else:
            if cambio == 1:
                E1 = E0 + (np.pi**2*hbar**2*(2*numeros[i, j] + 1))/(2*m*L)
                if E1 < E0:
                    E0 = E1
                    energias.append(E0)
                    numeros[i, j] += cambio
                    contador += 1 
                elif np.exp(-(E1-E0)/(KT)) > R:
                    E0 = E1
                    energias.append(E0)
                    numeros[i, j] += cambio
                    contador += 1
                else:
                    energias.append(E0)
                    contador += 1
            else:
                E1 = E0 + (np.pi**2*hbar**2*(-2*numeros[i, j] + 1))/(2*m*L)
                if E1 < E0:
                    E0 = E1
                    energias.append(E0)
                    numeros[i, j] += cambio
                    contador += 1
                elif np.exp(-(E1-E0)/(KT)) > R:
                    E0 = E1
                    energias.append(E0)
                    numeros[i, j] += cambio
                    contador += 1
                else:
                    energias.append(E0)
                    contador += 1

#Gráficas
pasos = np.arange(0, pasos_totales)  
plt.figure()
plt.xlabel('$Pasos$')
plt.ylabel('$Energía$')
plt.title('Energía total del sistema en función del número de pasos')
plt.plot(pasos, energias, color = 'blue')
plt.show()
      
        
    
