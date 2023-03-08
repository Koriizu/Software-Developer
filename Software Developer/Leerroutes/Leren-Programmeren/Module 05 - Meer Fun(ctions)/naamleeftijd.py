def naam_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    return {'naam': naam, 'leeftijd': leeftijd}

mensen = []
while True:
    input_str = input("Toets enter om door te gaan of stop om te printen: ")
    if input_str == "stop":
        break
    mensen.append(naam_leeftijd())

for persoon in mensen:
    print(f"{persoon['naam']} is {persoon['leeftijd']} jaar")