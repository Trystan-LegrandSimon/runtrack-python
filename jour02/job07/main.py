#!/usr/local/bin/python3

chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de caractères par ligne dans la pyramide
caracteres_par_ligne = 1

# Boucle pour construire la pyramide
for i in range(len(chaine)):
    print(chaine[i], end=" ")
    if i + 1 == caracteres_par_ligne * (caracteres_par_ligne + 1) / 2:
        print()  # Passer à la ligne suivante
        caracteres_par_ligne += 1
