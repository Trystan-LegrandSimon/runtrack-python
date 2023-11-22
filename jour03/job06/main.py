#!/usr/bin/python3

def negatif_positif(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

# Appel de la fonction avec différents paramètres
negatif_positif(5)
negatif_positif(-3)
negatif_positif(0)
