from fruitmand import fruitmand 

lijst = sorted(fruitmand, key=lambda i: i['weight'], reverse=True)

for x in range(len(lijst)):
    print(lijst[x]['name'], lijst[x]['weight'], 'gram')
