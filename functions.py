#Functions

def menu():
    valasztott=''
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