boodschappen = {}

while True:
    item = input("Wat wilt u toevoegen aan de boodschappenlijst? (type 'stop' om te stoppen)").lower()
    if item == "stop":
        break
    hoeveelheid = int(input("Hoeveel wilt u er van hebben?"))
    
    if item in boodschappen:
        boodschappen[item] += hoeveelheid
    else:
        boodschappen[item] = hoeveelheid

print("Uw boodschappenlijst:")
for item in boodschappen:
    print(item + ": " + str(boodschappen[item]))
