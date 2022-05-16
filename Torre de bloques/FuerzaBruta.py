from itertools import permutations
import time

blocks = []
start_time = time.time()  # starts time


def brute_force_programming(filename):
    global blocks
    parse_file(filename)
    rotate_blocks()
    combination_list = combinations()
    calculation(combination_list)


def parse_file(filename):
    file = open(filename, "r")
    for line in file:
        line = (line.replace(",", "")).rstrip('\n')  # delete commas and \n
        dimensions = line.split(' ')
        num_dimensions = list(map(int, dimensions))  # convert to int type
        blocks.append(num_dimensions)
    file.close()


def rotate_blocks():
    global blocks

    shape_index = 0
    letter = 1
    temp_blocks = []

    while shape_index < len(blocks):
        counter = 1
        all_rotations = list(permutations(blocks[shape_index]))
        for rot in all_rotations:
            F = rot[0]
            P = rot[1]

            if F <= P:
                temp_blocks.append(rot)
                counter += 1
        shape_index += 1
        letter += 1
    blocks = temp_blocks
    # print(blocks)


def combinations():
    position_list = []
    for i in range(0, len(blocks) - 1):
        position_list.append(i)

    combination_list = [[]]  # crea la lista de posibles combinaciones
    for x in position_list:
        n_sub_conj = [subConj + [x] for subConj in combination_list]
        combination_list.extend(n_sub_conj)
    # print(combination_list)
    return combination_list


def calculation(combination_list):
    a_list = []
    elem_list = []

    for i in combination_list:
        sum_a = 0
        old_f = 1000  # un numero alto para que siempre se cumpla la condicion
        old_p = 1000
        sum_element = ''
        for j in i:
            new_f = int(blocks[j][0])
            new_p = int(blocks[j][1])

            if new_f < old_f and new_p < old_p:  # si la condicion no se cumple
                old_p = new_p
                old_f = new_f
                sum_a += int(blocks[j][2])
                sum_element += str(blocks[j]) + "+"

            else:
                break
        a_list.append(sum_a)
        elem_list.append(sum_element)

    # Salida

    end_time = time.time()
    print("Output:")
    print("altura maxima:" + str(max(a_list)))
    position = a_list.index(max(a_list))
    elem_included = elem_list[position]
    print("Bloques:" + str(elem_included))
    end_time = time.time()
    print("Tiempo de ejecución: " + str(end_time - start_time) + " segundos")
