import sys
from Dinamico import Dinamico
from FuerzaBruta import FuerzaBruta
from time import time

def readArchive(filename):
    """
    Function to read a file, and create a matriz with each line on the file
    receive the filename
    return a matrix of numbers
    """
    values = []
    file = open(filename,"r")
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(", ")
        values.append([round(float(element), 5) if element.isdigit() else element for element in line])
    return values

def main():
    filename = sys.argv[2]
    goldMine = readArchive(filename)
    algoritmo = int(sys.argv[1])
    escribirMatriz(goldMine)
    if algoritmo == 1:
        algoritmoFuerzaBruta(goldMine, filename)
    elif algoritmo == 2:
        algoritmoDinamico(goldMine, filename)
    else:
        print("Algoritmo desconocido por favor ingrese un algoritmo válido")

def algoritmoFuerzaBruta(goldMine, fileName):
    '''
    Metodo para buscar por medio de fuerza bruta el maximo de oro con su camino respectivo
    Recibe el nombre del archivo y la matriz de los caminos
    '''
    startTime = time()
    row = len(goldMine)
    column = len(goldMine[0])
    algoritmo = FuerzaBruta(goldMine, row, column)
    maxGold, caminoOptimo = algoritmo.getMaxGold()
    print("Camino Optimo", caminoOptimo)
    print("Maximo oro", maxGold)
    ejecutionTime = time() - startTime
    finalSolution(goldMine, caminoOptimo, maxGold, fileName, ejecutionTime)


def algoritmoDinamico(goldMine, fileName):
    '''
    Metodo para buscar por medio de un metood dinamico el maximo de oro con su camino respectivo
    Recibe el nombre del archivo y la matriz de los caminos
    '''
    startTime = time()
    row = len(goldMine)
    column = len(goldMine[0])
    algoritmo = Dinamico(goldMine, row, column)
    maxGold, caminoOptimo = algoritmo.getMaxGold()
    print("Camino Optimo: ", caminoOptimo)
    print("Maximo oro: ", maxGold)
    executionTime = time() - startTime
    print("Execution time: " + str(executionTime) + " segundos")
    finalSolution(goldMine, caminoOptimo, maxGold, fileName, executionTime)

def escribirMatriz(matriz):
    '''
    Metodo utilizado para imprimir la matriz de los caminos
    Recibe la matriz a imprimir
    '''
    printMatriz = '\n'.join([' '.join(['{:10}'.format(item) for item in row]) for row in matriz])
    print(printMatriz)
    
def finalSolution(matriz, camino, maxGold, fileName, tiempo):
    '''
    Metodo para escribir el archivo de solucion con el formato deseado
    recibe la matriz a imprimir, el camino, maximo de oro, nombre del archivo y el tiempo de ejecución
    '''
    stringMatriz = '\n'.join([' '.join(['{:10}'.format(item) for item in row]) for row in matriz])
    stringCamino = "Camino optimo: [ "
    solutionFile = open(fileName + "_solution.txt", "w")
    solutionFile.write("\n Matriz a ejecutar: \n\n")
    solutionFile.write(stringMatriz)
    solutionFile.write("\n\n\n\n")
    
    for par in camino:
        stringCamino += "( "
        if len(par) == 2:
            stringCamino += str(par[0]) + ", " + str(par[1])
        stringCamino += " )"
    stringCamino += " ]"
    print(stringCamino)
    solutionFile.write(stringCamino)
    solutionFile.write("\n Maximo de oro: ")
    solutionFile.write(str(maxGold))
    solutionFile.write("\n Duración de la ejecución: ")
    solutionFile.write(str(tiempo))
    solutionFile.write(" segundos")
        

if __name__ == '__main__':
    
    main()