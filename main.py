#Main
from functions import menu, fajlBetoltes, termekekKiir, termekekArakkalKiir, ujTermek
from os import system

fajlBetoltes()

valasztas = ''

while valasztas !='0':
    valasztas = menu()
    if valasztas == '1':
        termekekKiir()
    elif valasztas =='2':
        termekekArakkalKiir()
    elif valasztas =='3':
        ujTermek()
    elif valasztas =='4':
        pass
    elif valasztas =='5':
        pass
    elif valasztas =='6':
        pass

