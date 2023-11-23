#!/usr/bin/python3

def remplacer_element_par_somme(voisins, liste):
    somme_voisins = liste[voisins[0]] + liste[voisins[1]]
    liste[3] = somme_voisins

# Créer une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Afficher la deuxième valeur de la liste
deuxieme_valeur = L[1]
print(f"Deuxième valeur de la liste : {deuxieme_valeur}")

# Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
remplacer_element_par_somme([2, 4], L)

# Afficher à nouveau le tableau
print("Tableau après la modification : ", L)

# Afficher la dernière valeur de la liste
derniere_valeur = L[-1]
print(f"Dernière valeur de la liste : {derniere_valeur}")