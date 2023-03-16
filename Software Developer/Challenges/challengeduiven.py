birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]

print('Bird counter until dot')

for bird in birds:
    print(f" {bird['name']} key: {bird['key']}")


def get_bird_by_key(birds: list, key:str):
    for bird in birds:
        if bird['key'] == key:
            return bird
       return None

while True:
    key = input("Enter bird key, or '.' to quit. ")
    if key == '.':
        break
    bird = get_bird_by_key(birds, key)
    if bird is not None:
        bird['count'] += 1
        print(f"{bird['name']} count: {bird['count']}")
    else:
        print("Invalid answer, please try again. ")

print('Bird count:')
totaal = 0
for bird in birds:
    print(f"{bird['name']}: {bird['count']}")
    totaal += bird['count']

print("Percentage of total")
for bird in birds:
    if totaal > 0:
        percentage = bird['count'] / totaal *100 
    else:
        percentage = 0
    print(f"{bird['name']}: {percentage:.2f}%")



