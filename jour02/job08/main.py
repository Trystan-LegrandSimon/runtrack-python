#!/usr/local/bin/python3

# Demander à l'utilisateur de saisir les longueurs des côtés du triangle
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Vérifier si les longueurs forment un triangle
if a + b > c and b + c > a and a + c > b:
    print("Ces longueurs forment un triangle.")
    
    # Vérifier le type de triangle
    if a == b == c:
        print("C'est un triangle équilatéral.")
    elif a == b or b == c or a == c:
        print("C'est un triangle isocèle.")
        
        # Vérifier si c'est aussi un triangle rectangle isocèle
        if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
            print("C'est également un triangle rectangle isocèle.")
    else:
        # Vérifier si c'est un triangle rectangle
        if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
            print("C'est un triangle rectangle.")
        else:
            print("C'est un triangle quelconque.")
else:
    print("Ces longueurs ne forment pas un triangle.")

