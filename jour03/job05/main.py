#!/usr/bin/python3

def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Éviter la division par zéro
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:  # Éviter le modulo par zéro
            return num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Opérateur non valide"

# Appel de la fonction avec différents paramètres
resultat_addition = calcule(5, '+', 3)
resultat_multiplication = calcule(4, '*', 6)
resultat_division = calcule(10, '/', 2)

# Affichage des résultats
print(f"Résultat de l'addition : {resultat_addition}")
print(f"Résultat de la multiplication : {resultat_multiplication}")
print(f"Résultat de la division : {resultat_division}")

