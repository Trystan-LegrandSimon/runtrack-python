#!/usr/bin/python3

def draw_rectangle(height = 0):

    try:
        if height == 0:
            raise ValueError()
        
        print(f"hauteur : {height} \n")

        for i in range(height):

            if i == height - 1:
                print( '/' + '_' * (2 * i) + '\\')
            else:
                print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')
    except:
        print(" ⚠️​  ", "ERREUR : Veuillez rentrer votre une largeur puis une hauteur.")

draw_rectangle(5)