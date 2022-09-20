
from ast import While
from operator import truediv


naam = input("Wat is uw naam?: ")
if naam == 'Kevin'.lower():
    raise NameError('U bent jammer genoeg veelste slim voor een baan')


leeftijd = input("Wat is uw leeftijd?: ")

lievelings_dier = input("Wat is uw favoriete circusdier?: ")

gender = input("Geslacht: Man/Vrouw?: ").lower()
if not gender in ('man' ,'vrouw'):
    raise NameError("Er zijn maar 2 genders, probeer opnieuw")


vraag1_ervaring = input("Heeft u praktijkervaring met dieren-dressuur?: ")
vraag1_ervaring = vraag1_ervaring.lower()

if vraag1_ervaring in ("ja"):   
    ervaring1_tijd = int(input("Hoeveel jaar heeft u praktijkervaring met dieren dressuur?: "))

vraag2_ervaring = input("Heeft u praktijkervaring met jongleren?: ")
vraag2_ervaring = vraag2_ervaring.lower()

if vraag2_ervaring in ("ja"):
    ervaring2_tijd = int(input("Hoeveel jaar heeft u praktijkervaring met jongleren?:  "))

vraag3_ervaring = input("Heeft u praktijkervaring met acrobatiek?: ")
vraag3_ervaring = vraag3_ervaring.lower()

if vraag3_ervaring in ("ja"):
    ervaring3_tijd = int(input("Hoeveel jaar heeft u praktijkervaring met acrobatiek?: "))

ervaring = False
if ((vraag1_ervaring == "ja") and (int(ervaring1_tijd) > 4)) or ((vraag2_ervaring == "ja") and (int(ervaring2_tijd) > 2)) or ((vraag3_ervaring == "ja") and (int(ervaring3_tijd) > 3)):
    ervaring = True

vraag_diploma = input("Bent u in bezit van een Diploma MBO-4 ondernemen?: ").lower()
if not vraag_diploma in ('ja'):
    raise NameError("U mag niet verder zonder diploma")

vraag_rijbewijs = input("Bent u in bezit van een geldig vrachtwagen-rijebewijs?: ")

vraag_hoed = input("Bent u in bezit van een hoge hoed?: ")

if gender in ("man"):
    vraag_snor = input("Heeft u een snor?: ")
    vraag_snor = vraag_snor.lower()
    if vraag_snor in ("ja"):
        lengte_snor = int(input("Wat is de lengte van uw snor?(in centimeters): "))
    
if gender in ("vrouw)"):
    vraag_haar = input ("Heeft u krulhaar?: ")
    vraag_haar = vraag_haar.lower()
    if vraag_haar in ("ja"):
        lengte_haar = int(input("Wat is de lengte van uw haar?(in centimeters): "))

vraag_lengte = int(input("Hoe lang bent u?(in centimeters): "))

vraag_gewicht = int(input("Wat is uw lichaamsgewicht?: "))

vraag_certificaat = input("Heeft u een certificaat 'Overleven met gevaarlijk personeel'?: ")

reden = input("Geef ons een reden waarom wij u moeten aannemen boven de andere sollicitanten: ")

criteria = False
if ((gender == "vrouw" and lengte_haar > 20) or (gender == "man" and lengte_snor > 10)) and vraag_diploma == "ja" and vraag_gewicht > 90 and vraag_lengte > 150 and vraag_certificaat == "ja" and vraag_rijbewijs == "ja" and vraag_hoed == "ja":
    criteria = True

if criteria and ervaring:
    print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek. stuur snel je CV door naar: waarschijnlijkiemandzijnemail@gmail.com")
else:
    print("U voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur voor Circus HotelDeBotel, het spijt ons!")




    

    
