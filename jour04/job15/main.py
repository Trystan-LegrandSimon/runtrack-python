#!/usr/bin/python3

def arrondir_et_trier(liste):
    print(f"La liste de base est : \n-> {liste}\n")

    def arrondir(nombre):
        partie_entiere = int(nombre)
        decimale = nombre - partie_entiere

        if decimale >= 0.5:
            return partie_entiere + 1
        else:
            return partie_entiere

    def tri_selection(liste):
        nombre_elements_liste = 0

        for element in liste:
            nombre_elements_liste += 1

        for i in range(nombre_elements_liste):
            min_idx = i

            for j in range(i+1, nombre_elements_liste):
                if liste[min_idx] > liste[j]:
                    min_idx = j

            liste[i], liste[min_idx] = liste[min_idx], liste[i]

        return liste

    liste_arrondie = [arrondir(nombre) for nombre in liste]
    liste_triee = tri_selection(liste_arrondie)

    print(f"La nouvelle liste qui est arrondi est : \n-> {liste_triee}")
    return liste_triee

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
arrondir_et_trier(L)