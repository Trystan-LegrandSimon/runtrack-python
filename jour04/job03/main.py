#!/usr/bin/python3

def creer_liste_fruits(nouveau_fruit):
    fruits = ["pomme", "cerise", "orange"]
    fruits.append(nouveau_fruit)
    return fruits

liste_de_fruits = creer_liste_fruits("melon")

print(liste_de_fruits)