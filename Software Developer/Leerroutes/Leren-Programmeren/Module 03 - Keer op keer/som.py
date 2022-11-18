nummer = 50
totaal = 50
output = ""
getal = 0
while totaal < 1000:
    nummer += 1
    totaal += nummer
    output += f" + {nummer}"
    getal += 1
    print(f"{getal}. 50{output} = {totaal}")  