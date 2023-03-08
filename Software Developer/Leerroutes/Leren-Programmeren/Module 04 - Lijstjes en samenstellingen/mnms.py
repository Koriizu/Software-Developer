import random

Colors = ('orange', 'blue', 'green', 'brown')

Aantal_M = int(input("Hoeveel M&M's moeten er in de zak toegevoegd worden? "))

Ms = []

for x in range(Aantal_M):
    Ms.append(random.choice(Colors))

print(Ms)