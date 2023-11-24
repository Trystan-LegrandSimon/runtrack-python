#!/usr/bin/python3

def my_sort(liste = []):
    try:
        if liste == []:
            raise ValueError()

        coups = 0
        print(f"=> Liste non triée :\n-> {liste}\n")
        
        while True:
            echange = False
            i = 0
            try:
                while True:
                    if liste[i] > liste[i + 1]:
                        liste[i], liste[i + 1] = liste[i + 1], liste[i]
                        coups += 1
                        echange = True
                    i += 1
            except IndexError:
                if not echange:
                    break
        print(f"=> Nombre total de coups nécessaires pour trier la liste :\n-> {coups}\n")
        print(f"=> Liste triée :\n-> {liste}")
        return liste
    
    except ValueError:
        print("⚠️​   ERREUR : Veuillez fournir une liste de nombres.")
        return liste

# Exemple d'utilisation
ma_liste = [64, 25, 12, 22, 11]
my_sort(ma_liste)
