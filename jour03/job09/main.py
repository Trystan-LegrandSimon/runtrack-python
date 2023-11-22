#!/usr/bin/python3

def moyenne(note1, note2, note3):
    moyenne = (note1 + note2 + note3) / 3
    return moyenne

# Demander à l'utilisateur de saisir trois notes
note1 = float(input("1. Entrez la première note : "))
note2 = float(input("2. Entrez la deuxième note : "))
note3 = float(input("3. Entrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

# Afficher la moyenne calculée
print(f"La moyenne de l'étudiant est : {moyenne_etudiant}")

if 20 >= moyenne_etudiant >= 15:
    print("Très bon élève")
elif 14 >= moyenne_etudiant >= 11:
    print("Bon élève")
elif 10 >= moyenne_etudiant >= 8:
    print("Élève moyen")
elif 7 >= moyenne_etudiant >= 0:
    print("Élève devant faire des efforts")

