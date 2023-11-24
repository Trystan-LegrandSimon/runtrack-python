#!/usr/bin/python3

def info_user():

    try:
        name = input("Quel est votre prénom ? ") 
        if not name:
            raise ValueError()
        else:
            print(f"Hello {name} !")

    except:
        print(" ⚠️​  ", "ERREUR : Veuillez rentrer votre prénom.")

info_user()