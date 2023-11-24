def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:

        if note < 40:  # Si la note est inférieure à 40, l'étudiant échoue
            notes_arrondies.append(note)
        else:  # Si la note est supérieure ou égale à 40, l'étudiant réussit
            multiple_suivant = ((note // 5) + 1) * 5
            
            if multiple_suivant - note < 3:  # Si la note est à moins de 3 points du multiple de 5 suivant
                notes_arrondies.append(multiple_suivant)  # On arrondit à ce multiple
            else:
                notes_arrondies.append(note)  # Sinon, on garde la note telle quelle
    return notes_arrondies

# Exemple d'utilisation :
print(arrondir_notes([33, 38, 83, 82, 40, 45, 48, 50, 55, 58, 60]))