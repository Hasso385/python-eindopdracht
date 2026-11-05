
# Kies een character class
player_class = "Warrior"

# Bepaal de health en damage
match player_class:
    case "Warrior":
        health = 150
        damage = 20

    case "Mage":
        health = 80
        damage = 35

    case "Archer":
        health = 100
        damage = 25

    case "Rogue":
        health = 90
        damage = 30

    case _:
        health = 0
        damage = 0
        print("Onbekende character class!")

# Print de resultaten
print("Gekozen class:", player_class)
print("Health:", health)
print("Damage:", damage)
