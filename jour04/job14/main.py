#!/usr/bin/python3

def my_long_word(number_integer: int = 0, chain_character: str = ""):
   
    print(f"Le chiffre/nombre entier est : \n{number_integer}")
    print(f"La chaîne de caractère est : \n{chain_character}\n")

    
    split_chain_character = chain_character.split(' ')
    new_chain_character = ''
    for mot in split_chain_character:
        compteur = 0
        for lettre in mot:
            compteur += 1
        if compteur > number_integer:
            new_chain_character += mot + ' '

    print(f"La nouvelle chaîne de caractère est : \n-> {new_chain_character}\n")
    return new_chain_character.strip()




number = 3
chaine = " La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

my_long_word(number, chaine)