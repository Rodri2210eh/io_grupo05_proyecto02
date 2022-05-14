from itertools import permutations
import time

blocks = []

def dynamic_programming(filename):
    global blocks

    start_time = time.time()  # starts time

    parse_file(filename)
    rotate_blocks()
    order_shapes()
    calculation(blocks)

    end_time = time.time()
    print("Tiempo de ejecución: " + str(end_time - start_time) + " segundos")

"""
Function: parse_file
Input: name of file
Output: -
Description: Function that gets blocks dimensions from file
"""
def parse_file(filename):
    file = open(filename, "r")
    for line in file:
        line = (line.replace(",", "")).rstrip('\n')   # delete commas and \n
        dimensions = line.split(' ')
        num_dimensions = list(map(int, dimensions))     # convert to int type
        blocks.append(num_dimensions)
    file.close()

"""
Function: order_shapes
Input: -
Output: -
Description: Function that orders the shape in ascending order depending on their height
"""
def order_shapes():
    global blocks

    blocks = sorted(blocks, key=lambda item: item[2])

"""
Function: rotate_blocks
Input: -
Output: -
Description: Function that rotates all the given blocks
"""
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

"""
Function: calculation
Input: array with all blocks
Output: -
Description: Function that calculates the longest sequence of blocks with the highest sequence
"""
def calculation(arr):
    n = len(arr)
  
    # initialize LIS and prev to get blocks
    lis = [1]*n
    prev = (list(range(0, n)))
    
    for i in range (1, n):
        for j in range(0, i):
            if arr[i][2] >= arr[j][2] :
                if check_block_stacking(arr[i], arr[j]):
                    lis[i] = lis[j]+1
                    prev[i] = j

    maximum = 0
    index = 0

    # Pick maximum of all LIS values
    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            index = i
    
    seq = [arr[index]]            #from the max number, go backwards to get sequence
    max_height = seq[0][2]

    while index != prev[index]:
        index = prev[index]
        seq.append(arr[index])
        max_height += arr[index][2]
    
    print("Output: altura máxima", max_height)
    print("Bloques ", seq)


"""
Function: check_block_stacking
Input: first block, second block
Output: boolean if first block < second block
Description: Function that checks if base is smaller than the other block
"""
def check_block_stacking(fst_block, scnd_block):
    F1 = fst_block[0]
    F2 = scnd_block[0]
    P1 = fst_block[1]
    P2 = scnd_block[1]
    
    return F1 < F2 and P1 < P2
