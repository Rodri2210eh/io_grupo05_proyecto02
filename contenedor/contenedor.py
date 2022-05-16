import sys
import os.path
import numpy as np
import time


def main():
    
    start_time = time.time()  # incia la cuenta de tiempo

    # ------ Validaciones -------

    if sys.argv[1] != "1" and sys.argv[1] != "2":
        print("El metodo seleccionado es invalido")
        return

    if len(sys.argv) != 3:
        print("No  ingreso la cantidad necesaria de parametros")
        return

    # ------- Asignacion de variables   ----------

    file_name = sys.argv[2]

    if not os.path.isfile(file_name):  # verifica que el archivo este en la carpeta
        print("El archivo no existe.")
        return

    f = open(file_name, "r")
    lines = f.readlines()

    # lines[0] -  tamano maximo de la mochila
    max_weight = lines[0]

    # lista de costos y beneficios
    list_weight_benefit = []
    for item in lines[1:]:
        list_weight_benefit.append(item.strip().split(","))
    # print(list_weight_benefit)

    number_of_elements = len(list_weight_benefit)

    # -------------  logica del programa  ----------------------------

    if sys.argv[1] == "1":  # Solucion por fuerza bruta

        position_list = []
        for x in range(1, number_of_elements + 1):
            position_list.append(x)
        # print(position_list)

        combination_list = [[]]  # crea la lista de posibles combinaciones
        for x in position_list:
            n_sub_conj = [subConj + [x] for subConj in combination_list]
            combination_list.extend(n_sub_conj)
        # print(combination_list)

        # calcula los pesos y beneficios
        benefits_list = []
        elem_included_list = []

        for i in combination_list:
            sum_weights = 0
            sum_benefits = 0
            elem_included = 'incluidos:'
            for j in i:
                sum_weights += int(list_weight_benefit[j - 1][0])
                sum_benefits += int(list_weight_benefit[j - 1][1])
                elem_included += str(j) + ','
            if sum_weights <= int(max_weight):
                benefits_list.append(sum_benefits)
                elem_included_list.append(elem_included)
        maxi_benefit = max(benefits_list)
        position = benefits_list.index(max(benefits_list))
        elem_included = elem_included_list[position]

    else:  # Solucion por progra dinamica

        matrix_v = np.zeros((int(number_of_elements) + 1, int(max_weight) + 1))  # el mas 1 es para contar el 0

        #  En list_weight_benefit se le resta 1 a los indices para que se ajuste

        for i in range(1, int(number_of_elements) + 1):
            wi = int(list_weight_benefit[i - 1][0])
            bi = int(list_weight_benefit[i - 1][1])
            for w in range(1, int(max_weight) + 1):
                if wi > w:
                    matrix_v[i][w] = matrix_v[i - 1][w]
                else:
                    w_wi = w - wi
                    if bi + int(matrix_v[i - 1][w_wi]) > matrix_v[i - 1][w]:
                        matrix_v[i][w] = bi + int(matrix_v[i - 1][w_wi])
                    else:
                        matrix_v[i][w] = matrix_v[i - 1][w]
        # print(matrix_v)

        # calculo para encontrar los elementos
        i = int(number_of_elements)
        k = int(max_weight)
        maxi_benefit = matrix_v[i][k]
        elem_included = 'incluidos:'
        for x in range(1, int(number_of_elements) + 1):
            if matrix_v[i][k] != matrix_v[i - 1][k]:
                elem_included += str(i) + ','
                k -= int(list_weight_benefit[i - 1][0])
                i -= 1
            else:
                i -= 1

    # --------- salidas ------------

    end_time = time.time()
    print("output:")
    print("Beneficio máximo:" + str(maxi_benefit))
    print(elem_included)
    print("Tiempo de ejecución: " + str(end_time - start_time) + " segundos")


main()
