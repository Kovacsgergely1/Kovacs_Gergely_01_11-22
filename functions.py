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
    print('2 - Termékek, árak, darabszám kiírása')
    print('3 - Új termék felvétele')
    print('4 - Termék törlése')
    print('5 - Ár módosítása')
    print('6 - Mentés fájlba')
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