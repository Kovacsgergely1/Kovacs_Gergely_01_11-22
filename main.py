#Main
from functions import menu, fajlBetoltes, termekekKiir, termekekArakkalKiir, ujTermek, Torles, Armodositas, Darabmodositas, saveFullFile
from os import system



valasztas = ''

while valasztas !='0':
    valasztas = menu()
    if valasztas == '1':
        fajlBetoltes()
        termekekKiir()
    elif valasztas =='2':
        fajlBetoltes()
        termekekArakkalKiir()
    elif valasztas =='3':
        fajlBetoltes()
        ujTermek()
    elif valasztas =='4':
        fajlBetoltes()
        Torles()
    elif valasztas =='5':
        fajlBetoltes()
        Armodositas()
    elif valasztas =='6':
        fajlBetoltes()
        Darabmodositas()
    elif valasztas == '7':
        saveFullFile()

