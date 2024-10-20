# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:42:07 2023

@author: Manuel Mora Cartagena
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

try:
    Nx = int(input('Selecciona el número de celdas en la componente x = '))
    Ny = int(input('Selecciona el número de celdas en la componente y = '))
    Nz = int(input('Selecciona el número de celdas en la componente z = '))
    print('Selecciona el tipo de red: \n-CS \n-FCC \n-BCC \n-DIAMANTE \n-SAL DE ROCA')
    red = input('Tipo de red: ')
    
    #RED CÚBICA SIMPLE (CS)
    if red == 'CS':
        celda_unidad = np.array([0, 0, 0]) #Define la celda unidad para la red CS
        n_atom = Nx*Ny*Nz #Define el número de átomos
        r = np.empty([n_atom, 3]) #Define un array en el que se guardarán las posiciones de cada átomo
        i_atom = 0 #Define el indice de átomos
        for i in range(Nx):
            for j in range(Ny):
                for k in range(Nz):
                    #Define las coordenadas del átomo en cada celda
                    r[i_atom, 0] = celda_unidad[0] + i
                    r[i_atom, 1] = celda_unidad[1] + j
                    r[i_atom, 2] = celda_unidad[2] + k
                    i_atom += 1
        #Gráfico en 3D de la red
        x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
        y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
        z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos            
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='blue')
        ax.set_title('Red cúbica simple (CS)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()
        print('Número total de átomos = ' + str(n_atom))      
    
    #RED CÚBICA CENTRADA EN LAS CARAS (FCC)
    if red == 'FCC': 
        celda_unidad = np.array([[0, 0, 0],[0.5, 0.5, 0],[0.5, 0, 0.5],[0, 0.5, 0.5]]) #Define la celda unidad para la red FCC
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
        #Gráfico en 3D de la red
        x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
        y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
        z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos            
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='green')
        ax.set_title('Red cúbica centrada en las caras (FCC)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()
        print('Número total de átomos = ' + str(n_atom))
    
    #RED CÚBICA CENTRADA EN EL CUERPO (BCC)
    if red == 'BCC':
        celda_unidad = np.array([[0, 0, 0], [0.5, 0.5, 0.5]]) #Define la celda unidad para la red BCC
        n_atom = 2*Nx*Ny*Nz #Define el número de átomos
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
                    i_atom += 2
        #Gráfico en 3D de la red
        x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
        y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
        z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos            
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='red')
        ax.set_title('Red cúbica centrada en el cuerpo (BCC)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()
        print('Número total de átomos = ' + str(n_atom))
    
    
    #RED DE DIAMANTE
    if red == 'DIAMANTE':
        celda_unidad = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5], [0.25, 0.25, 0.25], [0.75, 0.75, 0.25], [0.75, 0.25, 0.75], [0.25, 0.75, 0.75]]) #Define la celda unidad para la red de diamante
        n_atom = 8*Nx*Ny*Nz #Define el número de átomos
        r = np.empty([n_atom, 3]) #Define un array en el que se guardarán las posiciones de cada átomo
        i_atom = 0 #Define el indice de átomos
        for i in range(Nx):
            for j in range(Ny):
                for k in range(Nz):
                    #Define las coordenadas del primer átomo en cada celda
                    r[i_atom, 0] = celda_unidad[0, 0] + i
                    r[i_atom, 1] = celda_unidad[0, 1] + j
                    r[i_atom, 2] = celda_unidad[0, 2] + k
                    #Define las coordenadas del segundo átomo en cada celda
                    r[i_atom+1, 0] = celda_unidad[1, 0] + i
                    r[i_atom+1, 1] = celda_unidad[1, 1] + j
                    r[i_atom+1, 2] = celda_unidad[1, 2] + k
                    #Define las coordenadas del tercer átomo en cada celda
                    r[i_atom+2, 0] = celda_unidad[2, 0] + i
                    r[i_atom+2, 1] = celda_unidad[2, 1] + j
                    r[i_atom+2, 2] = celda_unidad[2, 2] + k
                    #Define las coordenadas del cuarto átomo en cada celda
                    r[i_atom+3, 0] = celda_unidad[3, 0] + i
                    r[i_atom+3, 1] = celda_unidad[3, 1] + j
                    r[i_atom+3, 2] = celda_unidad[3, 2] + k
                    #Define las coordenadas del quinto átomo en cada celda
                    r[i_atom+4, 0] = celda_unidad[4, 0] + i
                    r[i_atom+4, 1] = celda_unidad[4, 1] + j
                    r[i_atom+4, 2] = celda_unidad[4, 2] + k
                    #Define las coordenadas del sexto átomo en cada celda
                    r[i_atom+5, 0] = celda_unidad[5, 0] + i
                    r[i_atom+5, 1] = celda_unidad[5, 1] + j
                    r[i_atom+5, 2] = celda_unidad[5, 2] + k
                    #Define las coordenadas del séptimo átomo en cada celda
                    r[i_atom+6, 0] = celda_unidad[6, 0] + i
                    r[i_atom+6, 1] = celda_unidad[6, 1] + j
                    r[i_atom+6, 2] = celda_unidad[6, 2] + k
                    #Define las coordenadas del octavo átomo en cada celda
                    r[i_atom+7, 0] = celda_unidad[7, 0] + i
                    r[i_atom+7, 1] = celda_unidad[7, 1] + j
                    r[i_atom+7, 2] = celda_unidad[7, 2] + k
                    i_atom += 8
        #Gráfico en 3D de la red
        x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
        y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
        z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos            
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='purple')
        ax.set_title('Red de diamante')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()
        print('Número total de átomos = ' + str(n_atom))
        
    #RED SAL DE ROCA
    if red == 'SAL DE ROCA':
        celda_unidad = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5], [0, 0, 0.5], [0.5, 0.5, 0.5], [0.5, 0, 1], [0, 0.5, 1]]) #Define la celda unidad para la red de diamante
        n_atom = 8*Nx*Ny*Nz #Define el número de átomos
        r = np.empty([n_atom, 3]) #Define un array en el que se guardarán las posiciones de cada átomo
        i_atom = 0 #Define el indice de átomos
        for i in range(Nx):
            for j in range(Ny):
                for k in range(Nz):
                    #Define las coordenadas del primer átomo en cada celda
                    r[i_atom, 0] = celda_unidad[0, 0] + i
                    r[i_atom, 1] = celda_unidad[0, 1] + j
                    r[i_atom, 2] = celda_unidad[0, 2] + k
                    #Define las coordenadas del segundo átomo en cada celda
                    r[i_atom+1, 0] = celda_unidad[1, 0] + i
                    r[i_atom+1, 1] = celda_unidad[1, 1] + j
                    r[i_atom+1, 2] = celda_unidad[1, 2] + k
                    #Define las coordenadas del tercer átomo en cada celda
                    r[i_atom+2, 0] = celda_unidad[2, 0] + i
                    r[i_atom+2, 1] = celda_unidad[2, 1] + j
                    r[i_atom+2, 2] = celda_unidad[2, 2] + k
                    #Define las coordenadas del cuarto átomo en cada celda
                    r[i_atom+3, 0] = celda_unidad[3, 0] + i
                    r[i_atom+3, 1] = celda_unidad[3, 1] + j
                    r[i_atom+3, 2] = celda_unidad[3, 2] + k
                    #Define las coordenadas del quinto átomo en cada celda
                    r[i_atom+4, 0] = celda_unidad[4, 0] + i
                    r[i_atom+4, 1] = celda_unidad[4, 1] + j
                    r[i_atom+4, 2] = celda_unidad[4, 2] + k
                    #Define las coordenadas del sexto átomo en cada celda
                    r[i_atom+5, 0] = celda_unidad[5, 0] + i
                    r[i_atom+5, 1] = celda_unidad[5, 1] + j
                    r[i_atom+5, 2] = celda_unidad[5, 2] + k
                    #Define las coordenadas del séptimo átomo en cada celda
                    r[i_atom+6, 0] = celda_unidad[6, 0] + i
                    r[i_atom+6, 1] = celda_unidad[6, 1] + j
                    r[i_atom+6, 2] = celda_unidad[6, 2] + k
                    #Define las coordenadas del octavo átomo en cada celda
                    r[i_atom+7, 0] = celda_unidad[7, 0] + i
                    r[i_atom+7, 1] = celda_unidad[7, 1] + j
                    r[i_atom+7, 2] = celda_unidad[7, 2] + k
                    i_atom += 8
        #Gráfico en 3D de la red
        x = r[:,0] #Define un array que tiene las posiciones x de todos los átomos
        y = r[:,1] #Define un array que tiene las posiciones y de todos los átomos
        z = r[:,2] #Define un array que tiene las posiciones z de todos los átomos            
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='orange')
        ax.set_title('Red sal de roca')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()
        print('Número total de átomos = ' + str(n_atom))
           
    #Escribo en un fichero de salida
    try:
        if os.path.exists('ejercicio1.txt'):
            fichero = open('ejercicio1.txt', 'w')
            fichero.write(str(n_atom) + '\n')
            for i in range(n_atom):
                fichero.write(str(r[i][0]) + ' ' + str(r[i][1]) + ' '+ str(r[i][2]) + '\n')
            fichero.close()
        else:
            fichero = open('ejercicio1.txt', 'x')
            fichero.write(str(n_atom))
            for i in range(n_atom):
                fichero.write(str(r[i][0]) + ' ' + str(r[i][1]) + ' '+ str(r[i][2]) + '\n')
            fichero.close()
    except:
        print('Error en la seleeción de red')
except:
    print('Error en la selección de número de celdas')    
    

