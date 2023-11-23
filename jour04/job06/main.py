#!/usr/bin/python3

def echanger_premiere_et_derniere(liste):
    if len(liste) >= 2:  # Vérifier que la liste a au moins deux éléments
        premiere_valeur = liste[0]
        derniere_valeur = liste[-1]

        liste[0] = derniere_valeur
        liste[-1] = premiere_valeur

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5]

print(f"Liste avant l'échange : {ma_liste}")

# Appel de la fonction pour échanger les valeurs
echanger_premiere_et_derniere(ma_liste)

print(f"Liste après l'échange : {ma_liste}")