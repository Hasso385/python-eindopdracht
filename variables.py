
# Producten
product_1 = "Laptop"
product_2 = "Telefoon"
product_3 = "Koptelefoon"

# Prijzen
price_1 = 899.99
price_2 = 499.99
price_3 = 79.99

# Aantallen verkochte producten
quantity_1 = 3
quantity_2 = 5
quantity_3 = 10

# Bereken de totale omzet
total_revenue = (
    price_1 * quantity_1
    + price_2 * quantity_2
    + price_3 * quantity_3
)

# Print de productgegevens
print("Winkel overzicht")
print("----------------")

print("Product:", product_1, "Prijs:", price_1, "Aantal:", quantity_1)
print("Product:", product_2, "Prijs:", price_2, "Aantal:", quantity_2)
print("Product:", product_3, "Prijs:", price_3, "Aantal:", quantity_3)

print("----------------")
print("Totale omzet:", total_revenue)
