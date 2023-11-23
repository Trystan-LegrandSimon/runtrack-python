#!/usr/bin/python3

def compter_multiples_de_trois(liste):
    compte = 0
    for nombre in liste:
        if nombre % 3 == 0:
            compte += 1
    return compte

# Liste donnée
L = [8, 24, 48, 2, 16]

# Appel de la fonction pour compter les multiples de 3 dans la liste
nombre_de_multiples_de_trois = compter_multiples_de_trois(L)

print(f"La liste est : {L}")
print(f"Nombre de multiples de 3 dans la liste : {nombre_de_multiples_de_trois}")
