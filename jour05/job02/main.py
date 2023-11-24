#!/usr/bin/python3

def draw_rectangle(width = 0, height = 0):

    try:
        if width == 0 and height == 0:
            raise ValueError()
        
        print(f"largeur : {width}")
        print(f"hauteur : {height}")

        print('|' + '-' * (width - 2) + '|')
        for _ in range(height - 2):
            print('|' + ' ' * (width - 2) + '|')
        print('|' + '-' * (width - 2) + '|')

    except:
        print(" ⚠️​  ", "ERREUR : Veuillez rentrer votre une largeur puis une hauteur.")

draw_rectangle(10, 3)