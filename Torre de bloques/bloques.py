import sys
from Dinamico import dynamic_programming
from FuerzaBruta import brute_force_programming

def main():
    try:
        algorithm = sys.argv[1]
        filename = sys.argv[2]
    except:
        print("ERROR: Número de argumentos inválido.")
    else:
        if algorithm == "1":
            brute_force_programming(filename)
        elif algorithm == "2":
            dynamic_programming(filename)
        else:
            print("ERROR: Algoritmo inválido.", algorithm)
            sys.exit()

main()
