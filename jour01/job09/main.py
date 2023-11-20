# Variables représentant le produit
nom_produit = "PC Portable"
prix_unitaire = 1000.0
quantite_en_stock = 50

# Afficher les informations du produit
print("Informations du produit :")
print("Nom du produit :", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_en_stock)

# Demander à l'utilisateur de saisir la quantité de produits à acheter
quantite_achat = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))

# Mettre à jour le stock
quantite_en_stock -= quantite_achat

# Augmenter le prix du produit de 10% en raison de l'inflation
prix_unitaire *= 1.10

# Afficher à nouveau les informations du produit après la mise à jour
print("\nInformations du produit après la mise à jour :")
print("Nom du produit :", nom_produit)
print("Prix unitaire après inflation :", prix_unitaire)
print("Quantité en stock après achat :", quantite_en_stock)