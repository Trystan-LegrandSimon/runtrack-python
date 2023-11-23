#!/usr/bin/python3

def tri_selection(liste = []):
    
    try:
        if liste == []:
            raise ValueError("Les paramètres ne peuvent pas être vides")
        
        print(f"La liste de base est : {liste}")

        nombre_elements_liste = 0
        for element in liste:
            nombre_elements_liste += 1
        print("Le nombre d'éléments dans la liste est :", nombre_elements_liste)

        # Parcourir tous les éléments de la liste
        for i in range(nombre_elements_liste):
            # Trouver le minimum dans la liste restante
            min_idx = i
            for j in range(i+1, nombre_elements_liste):
                if liste[min_idx] > liste[j]:
                    min_idx = j
            # Échanger le minimum trouvé avec le premier élément de la liste restante
            liste[i], liste[min_idx] = liste[min_idx], liste[i]

        print("Liste triée dans l'ordre croissant :", liste)
        return liste
    
    except:
        print(" ⚠️​  ", "ERREUR : Veuillez rentrer une liste de nombre pour pouvoir les trier dans l'ordre croissant.")

L = [64, 34, 25, 12, 22, 11, 90]
tri_selection(L)