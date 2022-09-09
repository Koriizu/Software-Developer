aantalcroissanten = int(input("Hoeveel Croissanten?"))
prijscroissant = 0.39
aantalstokbroden = int(input("Hoevel Stokbroden?"))
prijsstokbrood = 2.78
aantalkortingsbonnen = 3
korting = 1.50

Totaalprijs = (aantalcroissanten * prijscroissant) + (aantalstokbroden * prijsstokbrood) - korting

print("De feestlunch kost je bij de bakker", Totaalprijs, "euro voor de", aantalcroissanten, "croissantjes en de ", aantalstokbroden, "stokbroden als de", aantalkortingsbonnen, "nog geldig zijn!")