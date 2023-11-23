#!/usr/bin/python3

def somme_valeurs_paires(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Appel de la fonction pour calculer la somme des valeurs paires dans la liste
somme_paires = somme_valeurs_paires(L)

print(f"La liste est : {L}")
print(f"Somme des valeurs paires dans la liste : {somme_paires}")