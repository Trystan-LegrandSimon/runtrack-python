#!/usr/bin/python3

def info_user(name = ""):
    try:
        if name == "":
            raise ValueError("Les paramètres ne peuvent pas être vides")
        
        print(f"Hello {name}")

    except:
        print(" ⚠️​  ", "ERREUR : Veuillez rentrer votre prénom")

name = "Pierre"
info_user()