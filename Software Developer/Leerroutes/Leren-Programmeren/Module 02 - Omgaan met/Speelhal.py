toegangsticket = 7.45
aantalpersonen = int(input("Hoeveel personen?"))
gameseatprijs = 0.37
gameseat5min = 9
aantalminuten = gameseat5min * 5

totaalprijs = (aantalpersonen * toegangsticket) + (gameseatprijs * gameseat5min * aantalpersonen)
afgeronde_prijs = round(totaalprijs, 2)

print("Dit geweldige dagje-uit met", aantalpersonen , "in de speel hal met", aantalminuten, "minuten VR kost je maar",  afgeronde_prijs, "euro")
