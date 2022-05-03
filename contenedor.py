import sys
import os.path
import numpy as np


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

    #lista de costos y beneficios
    list_weight_benefit = []
    for item in lines[1:]:
        list_weight_benefit.append(item.strip().split(","))
    print(list_weight_benefit)

    number_of_elements= len(list_weight_benefit);

    # logica del programa

    if sys.argv[1] == "1":
        # Solucion por fuerza bruta
        print('fuerza bruta')
    else:
        # Solucion por progra dinamica
        matrixV = np.zeros((int(number_of_elements)+1, int(max_weight)+1))  #el mas 1 es para contar el 0

        for i in range(1, int(number_of_elements)):
            for w in range(int(max_weight)):

                wi = int(list_weight_benefit[i][0])
                bi = int(list_weight_benefit[i][1])

                if wi > w:
                    matrixV[i][w] = matrixV[i-1][w]
                else:
                    if bi + int(matrixV[i-1][w-wi]) > matrixV[i-1][w]:
                        matrixV[i][w] = bi+int(matrixV[i-1][w-wi])
                    else:
                        matrixV[i][w] = matrixV[i-1][w]
        print("matriz final")
        print(matrixV)

main()
