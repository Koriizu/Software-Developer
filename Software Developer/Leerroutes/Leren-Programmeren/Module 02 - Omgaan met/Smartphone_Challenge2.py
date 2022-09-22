
iphone_prijs = round(float(input("Hoe duur is de Iphone? ")), 2)
samsung_prijs = round(float(input("Hoe duur is de Samsung? ")), 2)
zenfone_prijs = round(float(input("Hoe duur is de ZenFone? ")), 2)

if ((samsung_prijs > 900) and (iphone_prijs > 900)):
    print("Het advies is dus geen telefoons te kopen, ze zijn te duur.")
    
elif ((samsung_prijs > 900) and (iphone_prijs < 900)):
    print("Het advies is om de Iphone te kopen, deze is onder de 900 euro en goedkoper dan de Samsung.")

elif ((iphone_prijs > 900) and (samsung_prijs < 900)):
    print("Het advies is om de Samsung te kopen, deze is onder de 900 euro en goedkoper dan de Iphone.")

elif (((iphone_prijs - zenfone_prijs) > 0 < 100) and ((samsung_prijs - zenfone_prijs) > 0 < 100)):
    print("Het advies is om de ZenFone te kopen, deze is namelijk 100 euro goedkoper dan de Iphone zowel als de Samsung.")

else:
    if ((iphone_prijs > samsung_prijs) and not (((iphone_prijs - zenfone_prijs) > 0 < 100) and ((samsung_prijs - zenfone_prijs) > 0 < 100))):
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

    elif ((samsung_prijs > iphone_prijs) and not (((iphone_prijs - zenfone_prijs) > 0 < 100) and ((samsung_prijs - zenfone_prijs) > 0 < 100))):
            verschil = round(samsung_prijs - iphone_prijs, 2)
            print(f"""
            De Samsung is het duurst, de telefoon kost: {samsung_prijs} Euro.
            De Iphone is het goedkoopst, de telefoon kost {iphone_prijs} Euro.
            Het advies is dus de Iphone te kopen. Deze is namelijk {verschil} euro goedkoper dan de Samsung""")


    else:
        print("De prijzen van de Iphone en Samsung zijn gelijk, en de ZenFone is niet 100 euro goedkoper dan beide de Samsung en Iphone. Toch raden we je aan om de Iphone te kopen, deze telefoon werkt namelijk sneller.")
