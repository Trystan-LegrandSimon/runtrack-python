#!/usr/bin/python3

def produit_dans_intervalle(liste):
    # Initialiser le produit à 1
    produit = 1

    # Parcourir la liste et multiplier les valeurs dans l'intervalle [25, 90]
    for nombre in liste:
        if 25 <= nombre <= 90:
            produit *= nombre

    return produit

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Appel de la fonction et affichage du résultat
resultat = produit_dans_intervalle(L)
print(f"La liste est : {L}")
print(f"Le produit des valeurs dans l'intervalle [25, 90] est : {resultat}")