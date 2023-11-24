#!/usr/bin/python3

def meters_per_week(number_steps = 0, height_steps = 0):
    try:
        if number_steps and height_steps == 0:
            raise ValueError("Veuillez fournir un nombre de marche et une hauteur de marche.")

        # Conversion de la hauteur des marches en mètres
        height_steps_meters = height_steps / 100

        # Calcul de la distance parcourue pour monter et descendre une marche
        distance_per_step = 2 * height_steps_meters

        # Calcul de la distance totale parcourue par jour
        distance_per_day = number_steps * distance_per_step

        # Calcul de la distance totale parcourue par semaine
        distance_per_week = distance_per_day * 7

        # Affichage du résultat
        print(f"Pour {number_steps} marches de {height_steps} cm, le gardien parcourt {distance_per_week:.2f} m par semaine.")

    except ValueError as e:
        print(f"⚠️", "ERREUR :", e)

meters_per_week(10, )