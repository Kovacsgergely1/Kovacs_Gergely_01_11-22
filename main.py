#Main
from functions import menu, fajlBetoltes, termekekKiir, termekekArakkalKiir, ujTermek, Torles, Armodositas, Darabmodositas, saveFullFile
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
        Torles()
    elif valasztas =='5':
        Armodositas()
    elif valasztas =='6':
        Darabmodositas()
    elif valasztas == '7':
        saveFullFile()

