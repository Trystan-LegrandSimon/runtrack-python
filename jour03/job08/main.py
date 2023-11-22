#!/usr/bin/python3

def show_type_and_season(type, saison):
    # FRUITS
    if type.lower() == "fruits" and saison.lower() == "hiver":
        print("Orange, Mandarine et Kiwi")
    elif type.lower() == "fruits" and saison.lower() == "ete":
        print("Poire, Fraise, Cassis")
    # LEGUME
    elif type.lower() == "legume" and saison.lower() == "hiver":
        print("Carotte, Topinambour, Endive")
    elif type.lower() == "legume" and saison.lower() == "ete":
        print("Artichaut, Aubergine, Navet")

# FRUITS test
show_type_and_season("Fruits", "Hiver")
show_type_and_season("Fruits", "Ete")

# LEGUME test
show_type_and_season("legume", "Hiver")
show_type_and_season("legume", "Ete")