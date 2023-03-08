import random

AANTALBEURTEN = 3
AANTALRONDES = 7
punten = 0
ronde = 0

while ronde < AANTALRONDES:
    getal = random.randint(1,1000)
    print(getal)
    beurt = 0
    ronde+=1
    print(f"Ronde:{ronde}")

    while beurt < AANTALBEURTEN:
        nummer = int(input("Raad een getal tussen de 1 en 1000. "))
        verschil = abs(getal - nummer)
        beurt+=1

        if nummer == getal:
            print("Je hebt het goed!")
            punten+=1

        else:
            if nummer < getal:
                print("Hoger")
            
            elif nummer > getal:
                print("Lager")

            if verschil < 20:
                print("Je bent erg warm")

            elif verschil < 50:
                print("Je bent warm")            
                
    if beurt == AANTALBEURTEN:
        print(f"Score = {punten}")
        vraag = input("Nog een keer raden? Y/N: ").lower()
        if vraag == "n":
            break

        
print(f"Aantal punten behaald: {punten}")