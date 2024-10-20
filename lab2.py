# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:38:48 2023

@author: Manuel Mora Cartagena
"""


import numpy as np
import matplotlib.pyplot as plt


def f(r):
    return -G*M*r/(np.dot(r, r))**1.5



#Constantes
G = 6.6738e-11 #Define la constante de gravitacion universal
M = 1.9891e30 #Define la masa del sol
m = 5.9722e24 #Defina la masa de la tierra
x0 = 1.4719e11 #Define la posición inicial en x (perihelio)
y0 = 0 #Define la posicion inicial en y (perihelio)
vx0 = 0 #Define la velocidad inicial en x (la velocidad es tangencial en el perihelio)
vy0 = 3.0287e4 #Define la velocidad inicial en y (la velocidad es tangencial en el perihelio)
años = 5 #Define el número de años
tf = años*365*24*3600 #Define el tiempo final en horas (5 años)
h = 3600 #Define la variación temporal en horas
t = np.arange(0, tf, h) #Define el intervalo de tiempo en paso de 1 hora
N = len(t) #Define el numero de puntos en los que se itera
tiempo = np.linspace(0, años, N) #Define el intervalo en años

'''
ALGORÍTMO DE VERLET
'''
#Variables para el algorítmo de Verlet
r = np.empty((N, 2)) #Define un array de de dimensiones N para la posicion en x e y
v = np.empty((2*N, 2)) #Define un array de dimension 2N para la velocidad en x y en y
K = np.empty(N) #Define una array de dimension N para la energia cinetica
P = np.empty(N) #Define un array de dimension N para la energia potencial
E = np.empty(N) #Define un array de dimension N para la energia total
'''
Con el algoritmo de Verlet solo es necesario calcular la posicion en posiciones enteras y la velocidad es posiciones semienteras
Sin embargo, si queremos saber la energia total del sistema es necesario calcular la velocidad en ambas posiciones
Esto es así porque la energia cinetica depende de la velocidad y la energia potencial depende de la posicion
Por lo tanto si se quiere calcular la energia total necesitamos ambas energias en los mismos instantes de tiempo
'''
r[0] = [x0, y0] #Añade la posicion inicial al array de posiciones
v[0] = [vx0, vy0] #Añade la velocidad inicial al array de velocidades

#Paso 0
v[1] = v[0] + h/2*f(r[0])
K[0] = 0.5*m*np.dot(v[0], v[0])
P[0] = -G*M*m/(np.dot(r[0], r[0]))**0.5
E[0] = K[0] + P[0]

for i in range(N-1): #Define un bucle para calcular cada variable en cada instante (enteros para r y enteros y semienteros para v)
    r[i+1] = r[i] + h*v[2*i+1] #calcula la posicion en un instante entero
    v[2*i+2] = v[2*i+1] + h*f(r[i+1])/2 #Calcula la velocidad en un instante entero
    v[2*i+3] = v[2*i+1] + h*f(r[i+1]) #Calcula la velocidad en un instante semientero
    K[i+1] = 0.5*m*np.dot(v[2*i+2], v[2*i+2]) #Calcula la energia cinetica en instante entero
    P[i+1] = -G*M*m/(np.dot(r[i+1], r[i+1]))**0.5 #Calcula la energia potencial en un instante entero
    E[i+1] = K[i+1] + P[i+1] #Calcula la energia total en un instante entero

plt.figure(1)
plt.title('Radio en función del tiempo (Verlet)')
plt.plot(tiempo, np.sqrt(r[::,0]**2 + r[::,1]**2), color = 'blue')
plt.xlabel('Tiempo (años)')
plt.ylabel('Radio (m)')
plt.show()

plt.figure(2)
plt.title('Trayectoria $x = f(y)$ (Verlet)')
plt.plot(r[::,0], r[::,1], color = 'red')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.show()

plt.figure(3)
plt.title('Energía en función del tiempo (Verlet)')
plt.plot(tiempo, K, label = 'Energía cinética')
plt.plot(tiempo, P, label = 'Energía potencial')
plt.plot(tiempo, E, label = 'Energía total')
plt.legend(loc = 'best')
plt.xlabel('Tiempo (años)')
plt.ylabel('Energía (J)')
plt.show()

plt.figure(4)
plt.title('Energía total en función del tiempo (Verlet)')
plt.plot(tiempo, E, color = 'green')
plt.xlabel('Tiempo (años)')
plt.ylabel('Energía (J)')
plt.show()

'''
MÉTODO RUNGE-KUTTA ORDEN 2
'''
#Variables para el algorítmo de Runge-Kutta orden 2
r2 = np.empty((N, 2)) #Define un array de de dimensiones N para la posicion en x e y
v2 = np.empty((N, 2)) #Define un array de dimension N para la velocidad en x y en y
K2 = np.empty(N) #Define una array de dimension N para la energia cinetica
P2 = np.empty(N) #Define un array de dimension N para la energia potencial
E2 = np.empty(N) #Define un array de dimension N para la energia total

#Paso 0
r2[0] = [x0, y0] #Añade la posicion inicial al array de posiciones
v2[0] = [vx0, vy0] #Añade la velocidad inicial al array de velocidades
K2[0] = 0.5*m*np.dot(v2[0], v2[0])
P2[0] = -G*M*m/(np.dot(r2[0], r2[0]))**0.5
E2[0] = K2[0] + P2[0]

for i in range(N-1): #Define un bucle para calcular cada variable en cada instante
    k1 = h*v2[i]
    l1 = h*f(r2[i])
    k2 = h*(v2[i] + 0.5*l1)
    l2 = h*f(r2[i] + 0.5*k1)
    r2[i+1] = r2[i] + k2
    v2[i+1] = v2[i] + l2
    K2[i+1] = 0.5*m*np.dot(v2[i+1], v2[i+1])
    P2[i+1] = -G*M*m/(np.dot(r2[i+1], r2[i+1]))**0.5
    E2[i+1] = K2[i+1] + P2[i+1]
    
plt.figure(1)
plt.title('Radio en función del tiempo (RK2)')
plt.plot(tiempo, np.sqrt(r2[::,0]**2 + r2[::,1]**2), color = 'steelblue')
plt.xlabel('Tiempo (años)')
plt.ylabel('Radio (m)')
plt.show()

plt.figure(2)
plt.title('Trayectoria $x = f(y)$ (RK2)')
plt.plot(r2[::,0], r2[::,1], color = 'darkred')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.show()

plt.figure(3)
plt.title('Energía en función del tiempo (RK2)')
plt.plot(tiempo, K2, label = 'Energía cinética')
plt.plot(tiempo, P2, label = 'Energía potencial')
plt.plot(tiempo, E2, label = 'Energía total', color = 'purple')
plt.legend(loc = 'best')
plt.xlabel('Tiempo (años)')
plt.ylabel('Energía (J)')
plt.show()

plt.figure(4)
plt.title('Energía total en función del tiempo (RK2)')
plt.plot(tiempo, E2, color = 'purple', label = 'Energía total con RK2')
plt.legend(loc = 'best')
plt.xlabel('Tiempo (años)')
plt.ylabel('Energía (J)')
plt.show()   

plt.figure(4)
plt.title('Energía total en función del tiempo')
plt.plot(tiempo, E2, color = 'purple', label = 'Energía total con RK2')
plt.plot(tiempo, E, color = 'green', label = 'Energía total con Verlet')
plt.legend(loc = 'best')
plt.xlabel('Tiempo (años)')
plt.ylabel('Energía (J)')
plt.show()   
