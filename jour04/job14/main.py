#!/usr/bin/python3

def my_long_word(number_integer: int = 0, chain_character: str = ""):
    
    try:
        if number_integer == 0 or chain_character == "":
            raise ValueError("Les paramètres ne peuvent pas être vides")
        
        print(f"Le chiffre/nombre entier de base est : \n-> {number_integer}\n")
        print(f"La chaîne de caractère de base est : \n-> {chain_character}\n")

        mots = []
        mot = ''
        for lettre in chain_character:
            if lettre == ' ':
                if mot != '':
                    mots.append(mot)
                    mot = ''
            else:
                mot += lettre
        if mot != '':
            mots.append(mot)

        new_chain_character = ''
        for mot in mots:
            compteur = 0
            for lettre in mot:
                compteur += 1
            if compteur > number_integer:
                new_chain_character += mot + ' '

        print(f"La nouvelle chaîne de caractère est : \n-> {new_chain_character}")
        return new_chain_character.strip()
    
    except ValueError as ve:
        print(" ⚠️​  ", f"Erreur : {ve}.")

number = 3
chaine = " La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

my_long_word(number, chaine)
