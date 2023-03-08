from fruitmand import fruitmand 

for index in range(len(fruitmand)):
    if fruitmand[index]['name'] == 'druif':
        fruitmand.pop(index)
        break

kleuren = []

for x in range (len(fruitmand)):
    if not fruitmand[x]['color'] in kleuren:
        kleuren.append(fruitmand[x]['color'])
print(kleuren) 
