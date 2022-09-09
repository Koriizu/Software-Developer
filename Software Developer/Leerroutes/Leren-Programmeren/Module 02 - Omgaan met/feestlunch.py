aantalcroissanten = int(input("Hoeveel Croissanten?"))
prijscroissant = 0.39
aantalstokbroden = int(input("Hoevel Stokbroden?"))
prijsstokbrood = 2.78
aantalkortingsbonnen = 3
korting = 1.50

Totaalprijs = (aantalcroissanten * prijscroissant) + (aantalstokbroden * prijsstokbrood) - korting
Afgerondeprijs = round(Totaalprijs, 2)

print(f"De feestlunch kost je bij de bakker {Afgerondeprijs} euro voor de {aantalcroissanten} croissantjes en de {aantalstokbroden} stokbroden als de {aantalkortingsbonnen} nog geldig zijn!")