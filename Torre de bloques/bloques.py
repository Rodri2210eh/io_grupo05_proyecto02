import sys
import numpy as np


global shapes
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
    second_sorted = first_sorted[np.argsort(first_sorted[:, 1])] # sorted by second column (width)
    shapes = second_sorted[::-1]
    print(shapes)

def rotate_shape(shape_index):
    rotations = []
    while len(rotations) < 3:
        F = shapes[shape_index][0]
        P = shapes[shape_index][1]
        A = shapes[shape_index][2]
        if F <= P and P <= A:
            shapes[shape_index] = [P, A, F]
            rotations.append(shapes[shape_index].tolist())
        if F <= A:
            shapes[shape_index] = [F, A, P]
            rotations.append(shapes[shape_index].tolist())
        if F <= P:
            shapes[shape_index] = [F, P, A]
            rotations.append(shapes[shape_index].tolist())
        if A <= P:
            shapes[shape_index] = [A, P, F]
            rotations.append(shapes[shape_index].tolist())
        if F <= P and A <= P:
            shapes[shape_index] = [A, F, P]
            rotations.append(shapes[shape_index].tolist())

    rotations = [list(i) for i in set(map(tuple, rotations))]
    print(rotations)


def dynamic_programming(filename):
    shapes = parse_file(filename)
    order_shapes()
    rotate_shape(0)
    rotate_shape(1)
    rotate_shape(2)
    rotate_shape(3)
    

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
