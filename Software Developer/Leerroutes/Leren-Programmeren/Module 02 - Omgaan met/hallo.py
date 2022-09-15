time = float(input("Hoe laat is het?: "))

h = float(input("Hoe laat is het in uren?: "))
m = float(input("Hoe laat is het in minuten?: "))

endH = 23.00
endM = 60

h2 = endH - h
m2 = endM - m

print(f"Het duurt nog {h2} uur en {m2} minuten voordat de dag voorbij is.")
