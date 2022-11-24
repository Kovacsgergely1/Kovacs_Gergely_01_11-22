#Functions
from data import termek, ar, darab
from os import system

fajlnev = 'data.csv'

def menu():
    valasztott=''
    system('cls')
    print('-----------PÉKSÉG-----------')
    print('0 - Kilépés')
    print('1 - Termékek kiírása')
    print('2 - Termékek és árak kiírása')
    print('3 - Termékek darabszámának kiírása')
    print('4 - Új termék felvétele')
    print('5 - Termék törlése')
    print('6 - Ár módosítása')
    print('7 - Mentés fájlba')
    valasztott=input('Válasszon egy menüpontot: ')
    return valasztott

def  fajlBetoltes():
    file = open(fajlnev, 'r', encoding='utf-8')
    for row in file:
        darabolt = row.strip().split(';')
        termek.append(darabolt[0])
        ar.append(float(darabolt[1]))
        darab.append(int(darabolt[2]))
    file.close()

def termekekKiir():
    system('cls')
    print('----------TERMÉKEK----------')
    for i in range(len(termek)):
        print(f'\t{termek[i]}')
    input('...')

def termekekArakkalKiir():
    system('cls')
    for i in range(len(termek)):
        print(f'\t{termek[i]} {ar[i]} Ft  {darab[i]} db.')
    input('...')