import sys
import os.path
import numpy as np
import time


def main():
    # Validaciones

    if sys.argv[1] != "1" and sys.argv[1] != "2":
        print("El meotodo seleccionado es invalido")
        return

    if len(sys.argv) != 3:
        print("No esta ingresando la cantidad necesaria de parametros")
        return

    # Asingacion de variables

    fileName = sys.argv[2]

    if not os.path.isfile(fileName):  # verifica que el archivo este en la carpeta
        print("El archivo no existe.")
        return

    f = open(fileName, "r")
    lines = f.readlines()

    # lines[0] -  tamano maximo de la mochila
    max_weight = lines[0]

    # lista de costos y beneficios
    list_weight_benefit = []
    for item in lines[1:]:
        list_weight_benefit.append(item.strip().split(","))
    # print(list_weight_benefit)

    number_of_elements = len(list_weight_benefit);

    # logica del programa

    startTime = time.time()     #incia la cuenta de tiempo

    if sys.argv[1] == "1":
        # Solucion por fuerza bruta
        print('fuerza bruta')
    else:
        # Solucion por progra dinamica
        matrixV = np.zeros((int(number_of_elements) + 1, int(max_weight) + 1))  # el mas 1 es para contar el 0

        #  EN list_weight_benefit se le resta 1 a los indices para que calce

        for i in range(1, int(number_of_elements) + 1):
            wi = int(list_weight_benefit[i - 1][0])
            bi = int(list_weight_benefit[i - 1][1])
            for w in range(1, int(max_weight) + 1):
                if wi > w:
                    matrixV[i][w] = matrixV[i - 1][w]
                else:
                    w_wi = w - wi
                    if bi + int(matrixV[i - 1][w_wi]) > matrixV[i - 1][w]:
                        matrixV[i][w] = bi + int(matrixV[i - 1][w_wi])
                    else:
                        matrixV[i][w] = matrixV[i - 1][w]
        # print(matrixV)

        # calculo para encontrar los elementos
        i = int(number_of_elements)
        k = int(max_weight)
        maxiBenefit = matrixV[i][k]
        elemIncluded = 'incluidos:'
        for x in range(1, int(number_of_elements) + 1):
            if matrixV[i][k] != matrixV[i - 1][k]:
                elemIncluded += str(i) + ','
                k -= int(list_weight_benefit[i - 1][0])

                i -= 1
            else:
                i -= 1
        endTime = time.time()

        # salidas
        print("output:")
        print("Beneficio máximo:" + str(maxiBenefit))
        print(elemIncluded)
        print("Tiempo de ejecución: " + str(endTime - startTime) + " segundos")

main()
