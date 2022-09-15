a = int(input("Kies een getal: "))
b = int(input("Kies een getal: "))

if a > b:
    max = a
    min = b
    print (f"""
    {max} is maximum
    {min} is minimum
    {max} is groter dan {min}
    """)

elif b > a:
    max = b
    min = a
    print (f"""
    {max} is maximum
    {min} is minimum
    {max} is groter dan {min}
    """)
else:
    print (f"{a} is gelijk aan {b}")