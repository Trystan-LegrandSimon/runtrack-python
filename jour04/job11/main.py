#!/usr/bin/python3

def augmenter_elements(liste):
    # Parcourir la liste et augmenter chaque élément de 1
    for i in range(len(liste)):
        liste[i] += 1

# Créer la liste d'entiers
L = [7, 11, 42, 39, 2]

# Afficher la liste avant la modification
print(f"Liste avant la modification : {L}")

# Appel de la fonction pour augmenter chaque élément de 1
augmenter_elements(L)

# Afficher la liste après la modification
print(f"Liste après la modification : {L}")
