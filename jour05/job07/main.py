#!/usr/bin/python3

def arrondir_notes(liste_notes = []):
    notes_arrondies = []

    try:
        if liste_notes == []:
            raise ValueError()
        
        for note in liste_notes:

            if note < 40:  # Si la note est inférieure à 40, l'étudiant échoue
                notes_arrondies.append(note)
            else:  # Si la note est supérieure ou égale à 40, l'étudiant réussit
                multiple_suivant = ((note // 5) + 1) * 5

                if multiple_suivant - note < 3:  # Si la note est à moins de 3 points du multiple de 5 suivant
                    notes_arrondies.append(multiple_suivant)  # On arrondit à ce multiple
                else:
                    notes_arrondies.append(note)  # Sinon, on garde la note telle quelle
        print(f'Liste de notes arrondies :\n{notes_arrondies}')
        return notes_arrondies
    except ValueError:
        print("⚠️​   ERREUR : Veuillez fournir une liste de nombres.")


liste_de_notes = [33, 38, 83, 82, 40, 45, 48, 50, 55, 58, 60]
arrondir_notes(liste_de_notes)