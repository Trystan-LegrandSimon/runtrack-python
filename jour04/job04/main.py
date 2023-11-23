#!/usr/bin/python3

def creer_liste_fruits(nouveau_fruit):
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, nouveau_fruit)
    return fruits

liste_de_fruits = creer_liste_fruits("mangue")
print(liste_de_fruits)