#!/usr/bin/python3

def verifier_langage(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Appel de la fonction avec différents paramètres
verifier_langage("JavaScript")
verifier_langage("python")
verifier_langage("java")
verifier_langage("reactjs")
verifier_langage("C++")  # Un exemple pour le cas par défaut
