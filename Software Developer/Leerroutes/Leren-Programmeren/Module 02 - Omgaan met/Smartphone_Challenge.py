
iphone_prijs = round(float(input("Hoe duur is de Iphone? ")), 2)
samsung_prijs = round(float(input("Hoe duur is de Samsung? ")), 2)


if iphone_prijs > samsung_prijs:
        verschil = round(iphone_prijs - samsung_prijs, 2)
        if verschil > 50:
            print(f"""
            De Iphone is het duurst, de telefoon kost: {iphone_prijs} Euro.
            De Samsung is het goedkoopst, de telefoon kost: {samsung_prijs} Euro.
            Het advies is dus de Samsung te kopen. Deze is namelijk {verschil} euro goedkoper dan de Iphone.""")
        else:
            print(f"""
            Omdat u een lichte voorkeur voor de Iphone heeft, raden we je aan om de Iphone te kopen.
            Deze is namelijk maar {verschil} euro duurder dan de Samsung.""")

elif samsung_prijs > iphone_prijs:
        verschil = round(samsung_prijs - iphone_prijs, 2)
        print(f"""
        De Samsung is het duurst, de telefoon kost: {samsung_prijs} Euro.
        De Iphone is het goedkoopst, de telefoon kost {iphone_prijs} Euro.
        Het advies is dus de Iphone te kopen. Deze is namelijk {verschil} euro goedkoper dan de Samsung""")


else:
    print("De prijzen van de Iphone en Samsung zijn gelijk, toch raden we je aan om de Iphone te kopen, deze telefoon werkt namelijk sneller.")
