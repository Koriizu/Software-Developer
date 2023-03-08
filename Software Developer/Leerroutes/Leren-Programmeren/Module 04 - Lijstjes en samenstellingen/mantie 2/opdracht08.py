from fruitmand import fruitmand 

fruitmand.append({    
    'name' : 'watermeloen',
    'weight' : 800,
    'color' : 'green',
    'round' : True
    })

totaalgewicht = 0

for x in range(len(fruitmand)):
    totaalgewicht+=(fruitmand[x]['weight'])

print (totaalgewicht)