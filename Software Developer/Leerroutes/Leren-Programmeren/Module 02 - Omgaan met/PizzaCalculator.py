# Arda Ozcoban
# De Pizza Calculator
from ast import While


print ('''----------------------Welkom bij Dominarda----------------------
Wat mag het zijn?''')
# Hier word laten zien wat op het menu staat
print ('''
Small pizza's zijn €4,99.
Medium pizza's zijn €7,50.
En de large pizza's zijn $9.99.''')

prijs_small = 4.99
prijs_medium = 7.50
prijs_large = 9.99

aantal_small = -1
# Hier kiest de klant hoeveel die van elke afmeting pizza's wilt
while aantal_small == -1:
    try:
        aantal_small = int(input("Hoeveel small pizza's?: "))
    except:
        print("Dat is geen aantal in nummers!")

while True:
    try:
        aantal_medium = int(input("Hoeveel medium pizza's?: "))
        break
    except:
        print("Dat is geen aantal in nummers!")
    
while True:
    try:
        aantal_large = int(input("Hoeveel large pizza's?: "))
        break
    except:
        print("Dat is geen aantal in nummers!")


prijs_totaal = prijs_small * aantal_small + prijs_medium * aantal_medium + prijs_large * aantal_large
afgeronde_totaalbedrag = round(prijs_totaal, 2)

# Hier print de bon zich uit
print (f'''
_________________________________________________________________________________________________
|
| U heeft:
| {aantal_small} Small
|________________________
| {aantal_medium} Medium
|________________________
| {aantal_large} Large
|________________________
|
| Uw totaal prijs is €{afgeronde_totaalbedrag}
| Fijne dag en totziens!
|________________________________________________________________________________________________''')




