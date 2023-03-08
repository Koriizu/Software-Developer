import random

Colors = ('orange:', 'blue:', 'green:', 'brown:', 'red:', 'yellow:','black:')
Aantal_M = int(input("Hoeveel M&M's moeten er in de zak toegevoegd worden? "))

Ms = {}

for i in range (0,Aantal_M):
    kleur = random.choice(Colors)
    # Als de kleur niet voorkomt in Ms, dan voeg ik hem toe met de waarde nul.
    if kleur not in Ms:
        Ms[kleur] = 1
    else:
    # Anders dit:
        Ms[kleur]+=1

for key, value in Ms.items():
    if not value == 0:
        print(key, value)