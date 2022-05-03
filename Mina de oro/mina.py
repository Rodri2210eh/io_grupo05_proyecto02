import sys
from Dinamico import Dinamico

def readArchive(filename):
    """
    Function to read a file, and create a matriz with each line on the file
    receive the filename
    return a matrix of numbers
    """
    values = []
    file = open(filename,"r")
    lines = file.readlines()
    print("lines =",lines)
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(", ")
        values.append([round(float(element), 5) if element.isdigit() else element for element in line])
    return values

def main():
    filename = sys.argv[2]
    goldMine = readArchive(filename)
    algoritmo = int(sys.argv[1])
    imprimirMatriz(goldMine)
    print(algoritmo)
    if algoritmo == 1:
        algoritmoFuerzaBruta(goldMine)
    elif algoritmo == 2:
        algoritmoDinamico(goldMine)
    else:
        print("Algoritmo desconocido por favor ingrese un algoritmo válido")

def algoritmoFuerzaBruta(goldMine):
    pass


def algoritmoDinamico(goldMine):
    row = len(goldMine)
    column = len(goldMine[0])
    algoritmo = Dinamico(goldMine, row, column)
    maxGold = algoritmo.getMaxGold()
    print(maxGold)

def imprimirMatriz(matriz):
    printMatriz = '\n'.join([' '.join(['{:10}'.format(item) for item in row]) for row in matriz])
    print(printMatriz)

if __name__ == '__main__':
    
    main()