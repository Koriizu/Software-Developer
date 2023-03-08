from fruitmand import fruitmand 
import random 
Aantal = int(input("Kies een aantal uit: "))
for x in range(Aantal):
    print(random.choice(fruitmand)['name'])
