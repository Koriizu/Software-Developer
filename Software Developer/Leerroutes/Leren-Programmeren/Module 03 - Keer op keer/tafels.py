getal = int(input("Kies een getal: "))

print(f"De tafel van {getal}")
for nummer in range(1, 11):
    eind_nummer = nummer * getal
    print(getal, "x", nummer, "=", eind_nummer)