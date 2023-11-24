#!/usr/bin/python3

def draw_tapis(n=0):
    try:
        if n == 0:
            raise ValueError()

        print(f"hauteur : {n} \n")

        print('+' + '-' * (n + 1) + "+")
        for i in range(n):
            print('|', end='')

            for j in range(n + 1):
                # Si nous sommes sur la diagonale, afficher un espace
                if i == n - j:
                    print(' ', end='')
                else:
                    print('#', end='')
            print('|')
        print('+' + '-' * (n + 1) + "+")

    except ValueError:
        print(" ⚠️​  ERREUR : Veuillez rentrer une largeur et une hauteur non nulles.")

draw_tapis(10)