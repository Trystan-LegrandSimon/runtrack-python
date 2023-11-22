#!/usr/bin/python3

def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        print(f"{heures} heure et {minutes_restantes} minutes")

    else:
        print("Veuillez entrer un nombre entier positif.")

# Appel de la fonction avec différents paramètres
time_to_text(120)
time_to_text(30)
time_to_text(75)
time_to_text(-5)
time_to_text("texte")  # Test avec une chaîne de caractères
