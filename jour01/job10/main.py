# Initialisation des variables
montant_initial = 50000 # Montant initial de l'investissement
taux_rendement_annuel = 20 # Taux de rendement annuel en pourcentage

# Afficher le gain annuel initial
gain_annuel =  montant_initial * (taux_rendement_annuel / 100)
print("Le rendement annuel est de", gain_annuel)

# Augmenter le capital de 5 000 euros et augmenter le taux de rendement de 2%
montant_initial += 5000
taux_rendement_annuel += 2


# Calculer et afficher le nouveau gain annuel
noouveau_gain_annuel =  montant_initial * (taux_rendement_annuel / 100)
print("Le rendement annuel est de", noouveau_gain_annuel)

# Retirer 10% du montant total et diminuer le rendement de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calculer et afficher le montant final et le nouveau gain
montant_final = montant_initial + noouveau_gain_annuel
print("Montant final de l'investissement après retrait et diminution du rendement :", montant_final)