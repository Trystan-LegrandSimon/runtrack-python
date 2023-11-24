#!/usr/bin/python3

def decaler_message(message="", decalage=0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    try:
        if not message or decalage == 0:
            raise ValueError("Veuillez fournir un message non vide et un nombre de décalage différent de zéro.")

        print(f"-> Votre message non chiffré est :\n=> {message}\n")

        message_decale = ''
        for lettre in message:
            if lettre in alphabet:
                index = (alphabet.index(lettre) + decalage) % len(alphabet)
                message_decale += alphabet[index]
            else:
                message_decale += lettre

        print(f"-> Votre message chiffré est :\n=> {message_decale}")
        return message_decale
    
    except ValueError as e:
        print(f"⚠️", "ERREUR :", e)

# Exemple d'utilisation :
decaler_message('clement', 3)
