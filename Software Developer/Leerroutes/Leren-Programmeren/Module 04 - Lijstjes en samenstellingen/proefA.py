import random

lijst_namen = []
lijst_loten = []
nogmeer = True

while nogmeer:
    vraagNamen = input("Geef een naam op. \n").lower()
    if vraagNamen in lijst_namen:
        print("Deze naam zit al in de lijst!")
    else:
        lijst_namen.append(vraagNamen)
    if len(lijst_namen) >= 3:
        meer = input("Wil je meer namen toevoegen? \n")
        if meer == "nee":
            nogmeer = False

lijst_loten = lijst_namen.copy()
goed = False


while not goed:
    goed = True
    random.shuffle(lijst_loten)
    for i in range(len(lijst_namen)):
        if lijst_namen[i] == lijst_loten[i]:
            goed = False

for x in range (len(lijst_namen)):
    print(f"{lijst_namen[0]} heeft {lijst_loten[0]} getrokken!")
    del lijst_loten[0]
    del lijst_namen[0]