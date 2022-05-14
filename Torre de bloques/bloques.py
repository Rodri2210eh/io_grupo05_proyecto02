import sys
from Dinamico import dynamic_programming

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
