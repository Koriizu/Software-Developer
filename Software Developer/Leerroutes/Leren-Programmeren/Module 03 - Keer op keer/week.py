
week = ["ma", "di", "wo", "do", "vr", "za", "zo"]


while True:
    dag_Vandaag = input("Welk dag is het vandaag? Ma/Di/Wo/Do/Vr/Za/Zo: ").lower()
    if dag_Vandaag in week:
        break
    else:
        print("Probeer het opnieuw aub.")

dag = 0
while True:
    print(week[dag])
    if week[dag] == dag_Vandaag:
        break
    dag += 1
    