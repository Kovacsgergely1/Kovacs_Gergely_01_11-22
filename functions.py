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
    print('6 - Darabszám módosítása')
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

def Save(termek, ar, darab):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{termek};{ar};{darab}')
    file.close()

def termekekKiir():
    termek.clear()
    ar.clear()
    darab.clear()
    fajlBetoltes()
    system('cls')
    print('----------TERMÉKEK----------')
    for i in range(len(termek)):
        print(f'\t{termek[i]}')
    input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')

def termekekArakkalKiir():
    termek.clear()
    ar.clear()
    darab.clear()
    fajlBetoltes()
    system('cls')
    for i in range(len(termek)):
        print(f'\t{termek[i]} {ar[i]} Ft  {darab[i]} db.')
    input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')

def ujTermek():
    termek.clear()
    ar.clear()
    darab.clear()
    fajlBetoltes()
    system('cls')
    print('--------ÚJ TERMÉK---------')
    bekertTermek = input('Termék neve: ')
    bekertAr = float(input('Termék ára: '))
    bekertDarab = int(input('Darabszám: '))
    Save(bekertTermek, bekertAr, bekertDarab)
    print('Sikeres felvétel!')
    input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')

def kereses(keresett):
    for index,ertek in enumerate(termek):
        if keresett == ertek:
            return index
    return -1

def Torles():
    termek.clear()
    ar.clear()
    darab.clear()
    fajlBetoltes()
    system('cls')
    print('------TERMÉK TÖRLÉSE--------')
    torlendo = input('Törlendő termék neve: ')

    if kereses(torlendo) != -1:
        termek.remove(termek[kereses(torlendo)])
        ar.remove(ar[kereses(torlendo)])
        darab.remove(darab[kereses(torlendo)])
        saveFullFile()
        print('Sikeres törlés!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')
    else:
        print('Nincs ilyen termék!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')

def saveFullFile():
    file = open(fajlnev, 'w', encoding = 'utf-8')
    for i in range(len(termek)):
        file.write(f'{termek[i]};{ar[i]};{darab[i]}')
        if (i != len(termek) -1):
            file.write('\n')
    file.close()

def Armodositas():
    termek.clear()
    ar.clear()
    darab.clear()
    fajlBetoltes()
    system('cls')
    print('-------ÁR MÓDOSÍTÁSA--------')
    keresett = input('Módosítandó termék neve: ')

    if kereses(keresett) != -1:
        print(f'Jelenlegi ár: {ar[kereses(keresett)]}')
        ar[kereses(keresett)] = input('Új ár: ')
        saveFullFile()
        print('Sikeres módosítás!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')
    else:
        print('Nincs ilyen termék!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')

def Darabmodositas():
    termek.clear()
    ar.clear()
    darab.clear()
    fajlBetoltes()
    system('cls')
    print('------DARAB MÓDOSÍTÁSA-------')
    keresett = input('Módosítandó termék neve: ')

    if kereses(keresett) != -1:
        print(f'Jelenlegi darab: {darab[kereses(keresett)]}')
        ujDarab = input('Új darab: ')
        darab[kereses(keresett)] = ujDarab
        saveFullFile()
        print('Sikeres módosítás!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')
    else:
        print('Nincs ilyen termék!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')