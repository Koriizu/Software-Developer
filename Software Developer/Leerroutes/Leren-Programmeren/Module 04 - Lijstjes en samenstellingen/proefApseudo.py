# lijst_namen, hierin zitten alle namen dat de user beantwoord bij vraag 1
# dict_loten, hierin worden waardes toegevoegd aan de namen

# herhaal
#     naam = vraag waarbij een naam word gevraagt
#         als deze naam niet in de lijst lijst_namen  zitten word deze toegevoegd aan deze lijst
#     als er drie of meer namen in deze lijst zit word er gevraagd:
#     wilt u meer namen toevoegen?
#     als hierop het antwoord nee is, hervat het programma met regel 11. Anders hervat het programma vanaf het begin van deze herhaling.

# lijst_loten = lijst_namen, hier kopiëren we de namen vanuit lijst_namen naar lijst_loten

# zo lang er elementen in lijst_namen zijn, blijft het programma in werking.
# als de allereerste elementen van lijst_namen en lijst_loten niet met elkaar overeen komen: 
# voegen we allebei de elementen toe aan dict_loten;
# verwijderen we de namen van de eerste elementen van de 2 lijsten
# shuffelen we beiden lijsten, en gaan we terug naar het begin van deze loop

# print dict_loten