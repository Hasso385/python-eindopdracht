
# Maak een boodschappenlijst
shopping_list = ["Brood", "Melk", "Eieren", "Kaas", "Appels"]

# Voeg twee producten toe
shopping_list.append("Bananen")
shopping_list.append("Yoghurt")

# Verwijder één product
shopping_list.remove("Kaas")

# Controleer of een product aanwezig is
if "Brood" in shopping_list:
    print("Brood staat op de boodschappenlijst!")

# Print het aantal producten
print("Aantal producten:", len(shopping_list))

# Print de volledige boodschappenlijst
print("Boodschappenlijst:")
print(shopping_list)
