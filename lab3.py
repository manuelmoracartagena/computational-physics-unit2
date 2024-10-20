# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:59:28 2023

@author: Manuel Mora Cartagena
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Define la función para el potencial
def V(r):
    return 4*epsilon*((sigma/r)**n - (sigma/r)**m)


#Inputs
Nx = int(input('Selecciona el número de celdas en la componente x = '))
Ny = int(input('Selecciona el número de celdas en la componente y = '))
Nz = int(input('Selecciona el número de celdas en la componente z = '))
print('Selecciona el tipo de condiciones de contorno: \n1 para condiciones de contorno libres \n2 para condiciones de contorno periódicas')
cc = input()

#Parámetros del problema
n = 12
m = 6
sigma = 2.3151
epsilon = 0.167
a = 3.603 #Parámetro de red

#Genero un red cúbica centrada en las caras (FCC) 
celda_unidad = np.array([[0, 0, 0],[0.5, 0.5, 0],[0.5, 0, 0.5],[0, 0.5, 0.5]]) #Define la celda unidad para la red FCC, multiplico en este caso por el parámetro de red
n_atom = 4*Nx*Ny*Nz #Define el número de átomos
r = np.empty([n_atom, 3]) #Define un array en el que se guardarán las posiciones de cada átomo
i_atom = 0 #Define el indice de átomos
for i in range(Nx):
    for j in range(Ny):
        for k in range(Nz):
            #Define las coordenadas del primer átomo en cada celda
            r[i_atom, 0] = celda_unidad[0, 0] + i
            r[i_atom, 1] = celda_unidad[0, 1] + j
            r[i_atom, 2] = celda_unidad[0, 2] + k
            #Define las coordenadas del segundo átomo en cada 
            r[i_atom+1, 0] = celda_unidad[1, 0] + i
            r[i_atom+1, 1] = celda_unidad[1, 1] + j
            r[i_atom+1, 2] = celda_unidad[1, 2] + k
            #Define las coordenadas del tercer átomo en cada 
            r[i_atom+2, 0] = celda_unidad[2, 0] + i
            r[i_atom+2, 1] = celda_unidad[2, 1] + j
            r[i_atom+2, 2] = celda_unidad[2, 2] + k
            #Define las coordenadas del cuarto átomo en cada 
            r[i_atom+3, 0] = celda_unidad[3, 0] + i
            r[i_atom+3, 1] = celda_unidad[3, 1] + j
            r[i_atom+3, 2] = celda_unidad[3, 2] + k
            i_atom += 4
r *= a #Multiplico por el parámetro de red, ya que corresponde con la anchura de cada celda
#Guardo en arrays las coordenadas de cada átomo
x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos   

if cc == '1': #Condiciones de contorno libres
#Calculo de la energía para condiciones de contorno libres
    E = 0 #Inicia el valor de la energía total del sistema
    E_atomos = [] #Define una lista para añadir el valor de la energía de cada átomo
    for i in range(n_atom):
        Ei = 0 #Inicia el valor de la energía del átomo i
        for j in range(n_atom):
            #Calculo la distancia entre pares para cada coordenada
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dz = z[i] - z[j]
            radio = np.sqrt(dx**2 + dy**2 + dz**2) #Calcula el radio entre pares       
            if radio == 0:
                None
            elif radio <= 3*sigma:
                E += 0.5*V(radio) #Calcula la energía correspondiente a la interacción entre átomos i-j para E total
                Ei += 0.5*V(radio) #Calcula la energía correspondiente a la interacción entre átomos i-j para E de i
            else:
                None 
        E_atomos.append(Ei) #Añade la energía del átomo i a la lista de energías de cada átomo
    print('La energía del sistema es ' + str(E))
    print('La energía por átomo es ' + str(E/n_atom))
elif cc == '2': #Condiciones de contorno periódicas
#Cálculo de la energía para condiciones de contorno periódicas
    E = 0 #Inicia el valor de la energía total del sistema
    E_atomos = [] #Define una lista para añadir el valor de la energía de cada átomo
    for i in range(n_atom):
        Ei = 0 #Inicia el valor de la energía del átomo i
        for j in range(n_atom):
            #Calculo la distancia entre pares para cada coordenada
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dz = z[i] - z[j]
            if dx > 0:
                if dx > Nx*a/2:
                    dx -= Nx*a
            if dx < 0:
                if dx < -Nx*a/2:
                    dx += Nx*a 
            if dy > 0:
                if dy > Ny*a/2:
                    dy -= Ny*a
            if dy < 0:
                if dy < -Ny*a/2:
                    dy += Ny*a
            if dz > 0:
                if dz > Nz*a/2:
                    dz -= Nz*a
            if dz < 0:
                if dz < -Nz*a/2:
                    dz += Nz*a
            radio = np.sqrt(dx**2 + dy**2 + dz**2) #Calcula el radio entre pares 
            if radio == 0:
                None
            elif radio <= 3*sigma:
                E += 0.5*V(radio) #Calcula la energía correspondiente a la interacción entre átomos i-j para E total
                Ei += 0.5*V(radio) #Calcula la energía correspondiente a la interacción entre átomos i-j para E de i
            else:
                None
        E_atomos.append(Ei) #Añade la energía del átomo i a la lista de energías de cada átomo
    print('La energía del sistema es ' + str(E))
    print('La energía por átomo es ' + str(E/n_atom))
else: #Error
    print('No has seleccionado correctamente el tipo de condiciones de contorno')
    
                
#Guardo en arrays las coordenadas de cada átomo
x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos            
#Gráfico en 3D de la red
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='blue')
ax.set_title('Red cúbica centrada en las caras (FCC)')
ax.set_xlabel('x ($\AA$)')
ax.set_ylabel('y ($\AA$)')
ax.set_zlabel('z ($\AA$)')
plt.show()
#Gráfico del potencial de cada átomo
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
mapacolor = ax2.scatter(x, y, z, c = E_atomos, cmap = 'cool')
ax2.set_title('Energía potencial de cada átomo')
fig2.colorbar(mapacolor, label = 'Energía potencial (eV)')
ax2.set_xlabel('x ($\AA$)')
ax2.set_ylabel('y ($\AA$)')
#ax2.set_zlabel('z ($\AA$')
plt.show()