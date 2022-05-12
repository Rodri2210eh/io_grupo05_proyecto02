import sys
import numpy as np
from itertools import permutations

shapes = []
final_result = {}
register = {}
blocks = {}
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def parse_file(filename):
    file = open(filename, "r")
    for line in file:
        line = (line.replace(",", "")).rstrip('\n')   # delete commas and \n
        dimensions = line.split(' ')
        num_dimensions = list(map(int, dimensions))     # convert to int type
        shapes.append(num_dimensions)
    file.close()
    return shapes

"""
Function: order_shapes
Input: -
Output: -
Description: Function that orders the shape in descending order depending on their base
"""
def order_shapes():
    global blocks

    blocks = {k: v for k, v in sorted(blocks.items(), key=lambda item: item[1])}

"""
Function: rotate_blocks
Input: -
Output: -
Description: Function that rotates all the blocks given
"""
def rotate_blocks():
    shape_index = 0
    letter = 1

    while shape_index < len(shapes):
        counter = 1
        all_rotations = list(permutations(shapes[shape_index]))
        for rot in all_rotations:
            block_id = abc[len(shapes) - letter] + str(counter)
            F = rot[0]
            P = rot[1]
            A = rot[2]
            
            if F <= P:
                blocks[block_id] = rot
                counter += 1
        shape_index += 1
        letter += 1

def dynamic_programming(filename):
    global shapes

    parse_file(filename)
    rotate_blocks()
    order_shapes()
    print("blocks", blocks)
    #calculate_phases(0, 1, [])
    #write_solution(filename)

"Check if base is smaller than the other block"
def check_block_stacking(fst_block, scnd_block):
    F1 = fst_block[0]
    F2 = scnd_block[0]
    P1 = fst_block[1]
    P2 = scnd_block[1]
    
    return F1 < F2 and P1 < P2

def calculate_phases(block_index, letter, phase):
    global register
    global blocks
    global abc

    if block_index > len(shapes):
        return
    
    rotated_block = rotate_block(block_index)

    counter = 1

    if block_index == 0 and not phase:
        for r in rotated_block:
            block_id = abc[len(shapes) - letter] + str(counter)
            height = r[2]
            phase.append([block_id, height, "Fin"]) # first phase, the optimal is Fin
            counter += 1
            blocks[block_id] = r
        register[len(shapes)] = phase
        
        calculate_phases(block_index + 1, letter + 1, phase)
    else:
        next_phase = []
        max_num = 0
        max_vals = []
        for r in rotated_block:
            row = []
            block_id = abc[len(shapes) - letter] + str(counter)
            
            blocks[block_id] = r
            row.append(block_id)
            for prev_block in phase:
                if check_block_stacking(blocks[block_id], blocks[prev_block[0]]):
                    height = r[2] + prev_block[-2]  #height + previous height; column sum
                    row.append(height)
                else:
                    row.append(-1)
            
            if -1 in row:
                max_num = -1
            else:
                max_num = max(row[1:])

            max_vals = [i for i, j in enumerate(row[1:]) if j == max_num]
            row.append(max_num)
            for maxi in max_vals:
                row.append(phase[maxi][0])
            next_phase.append(row)
            counter += 1

        register[len(shapes) - block_index] = next_phase
        
        calculate_other_phases(phase, block_index, letter, block_index, [])

        # if last phase
        if block_index == len(shapes):
            phase = ["Ini"]

            for val in register[1]:
                height = val[-2]
                phase.append(height) # the optimal is max
            max_num = max(phase[1:])
            max_vals = [i for i, j in enumerate(phase[1:]) if j == max_num]
            phase.append(max_num)
            for maxi in max_vals:
                phase.append(register[1][maxi][0])
            
            register[0] = [phase]

            find_route()
        else:
            calculate_phases(block_index + 1, letter + 1, next_phase)

def calculate_other_phases(phase, index, letter, block_index, next_phase):
    if block_index == len(shapes):
        return

    max_num = 0
    max_vals = []
    counter = 1
    
    rotated_block = rotate_block(block_index)
    for r in rotated_block:
        row = []
        block_id = abc[len(shapes) - letter] + str(counter)
        blocks[block_id] = r
        row.append(block_id)
        for prev_block in phase:
            if check_block_stacking(blocks[block_id], blocks[prev_block[0]]):
                height = r[2] + prev_block[-2]  #height + previous height; column sum
                row.append(height)
            else:
                row.append(-1)
        if -1 in row:
            max_num = -1
        else:
            max_num = max(row[1:])

        max_vals = [i for i, j in enumerate(row[1:]) if j == max_num]
        row.append(max_num)
        for maxi in max_vals:
            row.append(phase[maxi][0])
        next_phase.append(row)
        counter += 1

    calculate_other_phases(phase, index, letter + 1, block_index + 1, next_phase)

    register[len(shapes) - index] = next_phase    

# only has support for ONE route
def find_route():
    global final_result
    global register

    counter = 0
    route = []
    route.append(register[0][0][0])
    
    for i in range(len(register)):
        index = [route[-1] in a for a in register[i]].index(True)
        route.append(register[i][index][-1])

    final_result = {register[0][0][-2] : route}

def write_solution(filename):
    f = open(filename + "_solution.txt", "w", encoding='utf-8')

    for x in register:
        f.write("\nETAPA " + str(x) + "\n")
        f.write("\ts |\t")
        
        if x == len(shapes): # first phase
            f.write("f*(s) |\t\tx*  |\n")
            f.write("\t-------------------------\n")
            for i in register[x]:
                f.write("\t" + str(i[0]) + "\t\t" + str(i[-2]) + "\t\t" +str(i[-1]) + "\n")
        else:
            for i in range(len(register[x+1])):
                if i == 0:
                    f.write("\t" + str(register[x+1][i][0]) + "|\t")
                else:
                    if register[x+1][i-1][0][0] == register[x+1][i][0][0]:
                        f.write("\t" + str(register[x+1][i][0]) + "|\t")
                    else:
                        break

            f.write("f*(s) |\t\tx*  |\n")
            f.write("\t-------------------------------------\n")

            for i in register[x]:
                for charac in i:
                    f.write("\t" + str(charac) + "\t")
                f.write("\n")

    final_height = [key for key in final_result.keys()][0]
    
    f.write(f'\nAltura máxima: {final_height} \n')
    print("Altura máxima: ", final_height)
    
    for route in final_result.values():
        f.write(f'Camino(s): {route} \nBloques: ')
        print("Camino(s): ", route)
        print("Bloques: ")
        for block_id, block in blocks.items():
            if block_id in route:
                f.write(f'{block_id} {block} ')
                print(block)

    f.close()

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
            dynamic_programming(filename)
        else:
            print("ERROR: Algoritmo inválido.", algorithm)
            sys.exit()

main()
