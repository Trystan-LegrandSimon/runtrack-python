#!/usr/bin/python3

def supprimer_doublons(liste = 0):
    
    try:
        print(f"La liste de base est : {liste}")

        liste_sans_doublons = []
        for i in liste:
            if i not in liste_sans_doublons:
                liste_sans_doublons.append(i)
            
        print(f"Liste triée dans l'ordre croissant : {liste_sans_doublons}")
        return liste_sans_doublons
    
    except:
        print("Veuillez intégrer votre liste avec les doublons pour que je puisse supprimer les doublons.")


L = [10,20,30,20,10,50,60,40,80,50,40]
supprimer_doublons(L)