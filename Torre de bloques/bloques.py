import sys
import numpy as np
import pandas as pd

shapes = []

def parse_file(filename):
    file = open(filename, "r")
    for line in file:
        line = (line.replace(",", "")).rstrip('\n')   # delete commas and \n
        dimensions = line.split(' ')
        num_dimensions = list(map(int, dimensions))     # convert to int type
        shapes.append(num_dimensions)
    return shapes

"""
Function: order_shapes
Input: -
Output: -
Description: Function that orders the shape in descending order depending on their base
"""
def order_shapes():
    global shapes

    arr_shapes = np.array(shapes)
    first_sorted = arr_shapes[np.argsort(arr_shapes[:, 0])] # sorted by first column (length)
    shapes = first_sorted[np.argsort(first_sorted[:, 1])] # sorted by second column (width)
    #shapes = second_sorted[::-1]

def rotate_block(shape_index):
    rotations = []
    while len(rotations) < 3 and shape_index < len(shapes):
        F = shapes[shape_index][0]
        P = shapes[shape_index][1]
        A = shapes[shape_index][2]
        if F <= P:
            shape_rot = [F, P, A]
            rotations.append(shape_rot)
            #print("rotation 3", shapes[shape_index])
        if F < P and P < A:
            shape_rot = [P, A, F]
            rotations.append(shape_rot)
            #print("rotation 1", shapes[shape_index])
        if F <= A:
            shape_rot = [F, A, P]
            rotations.append(shape_rot)
            #print("rotation 2", shapes[shape_index])
        if A <= P:
            shape_rot = [A, P, F]
            rotations.append(shape_rot)
            #print("rotation 4", shapes[shape_index])
        if F < P and A < P:
            shape_rot = [A, F, P]
            rotations.append(shape_rot)
            #print("rotation 5", shapes[shape_index])

    rotations = [list(i) for i in set(map(tuple, rotations))]
    return rotations


def dynamic_programming(filename):
    global shapes

    parse_file(filename)
    order_shapes()

    abc = ["A", "B", "C", "D", "E"] # temporal identifier for blocks, change to randomized characters

    last_step = [[]]

    f = open("solution.txt", "w")
    counter = 1
    f.write("ETAPA " + str(len(shapes)) + "\n")
    f.write("\ts |\t\tf*(s) |\t\tx*  |\n")
    f.write("\t----------------------------\n")

    calculate_phases(0, 1, [], {})

def calculate_phases(block_index, letter, phase, register):
    if block_index > len(shapes):
        return
    
    rotated_block = rotate_block(block_index)

    counter = 1
    abc = ["A", "B", "C", "D", "E"] # temporal identifier for blocks, change to randomized characters

    if block_index == 0 and not phase:
        for r in rotated_block:
            block_id = abc[len(shapes) - letter] + str(counter)
            height = r[2]
            phase.append([block_id, height, "END"]) # first phase, the optimal is END
            counter += 1
        register[len(shapes)] = phase
        
        calculate_phases(block_index + 1, letter + 1, phase, register)
    else:
        next_phase = []

        for r in rotated_block:
            row = []
            block_id = abc[len(shapes) - letter] + str(counter)
            row.append(block_id)
            for block in phase:
                # check_block_stacking(r, block[1:-2]) # c y luego d
                height = r[2] + block[-2]  #height + previous height; column sum
                row.append(height) # first phase, the optimal is END
            max_val = max(row[1:])
            row.append(max_val)
            row.append(phase[row.index(max_val) - 1][0])
            next_phase.append(row)
            counter += 1
        register[len(shapes) - block_index] = next_phase

        # if last phase
        if block_index == len(shapes):
            phase = ["Start"]

            for val in register[1]:
                height = val[-2]
                phase.append(height) # the optimal is max
            max_val = max(phase[1:])
            phase.append(max_val) # first phase, the optimal is END
            phase.append(register[1][phase.index(max_val) - 1][0])
            register[0] = phase

            print(register)
        else:
            calculate_phases(block_index + 1, letter + 1, next_phase, register)

    
"Check if base is smaller than the other block"
def check_block_stacking(fst_block, scnd_block):
    area1 = fst_block[0] * fst_block[1]     #c
    area2 = scnd_block[0] * scnd_block[1]   #d

    return area1 > area2

def main():
    try:
        algorithm = sys.argv[1]
        filename = sys.argv[2]
    except:
        print("ERROR: Número de argumentos inválido.")
    else:
        if algorithm == "1":
            print("fuerza bruta")
        elif algorithm == "2":
            print("programación dinámica")
            dynamic_programming(filename)
        else:
            print("ERROR: Algoritmo inválido.", algorithm)
            sys.exit()
        print("file name: ", filename)

main()
