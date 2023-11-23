#!/usr/bin/python3

def trouver_valeur_max_min(liste):

    maximum = liste[0]
    minimum = liste[0]

    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
        elif nombre < minimum:
            minimum = nombre

    return maximum, minimum

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Appel de la fonction pour récupérer la valeur, le maximum et le minimum
maximum, minimum = trouver_valeur_max_min(L)

print(f"La liste est : {L}")
print(f"La valeur max est : {maximum}")
print(f"La valeur min est : {minimum}")