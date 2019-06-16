# Python 3

import random

wynik_gracza = 0
wynik_komputera = 0
def gra_w_papier(twoj_wybor, wybor_komputera):
    """
    Funkcja odpowiadająca za logikę gry w Papier, kamień, nożyce

    :param twoj_wybor:
    :param wybor_komputera:
    :return:
    """

    reguly = [
        {"twoj" : 1, "komputer" : 2, "rezultat" : False},
        {"twoj" : 1, "komputer":3, "rezultat": True},
        {"twoj": 2, "komputer": 1, "rezultat": True},
        {"twoj": 2, "komputer": 3, "rezultat": False},
        {"twoj": 3, "komputer": 1, "rezultat": False},
        {"twoj": 3, "komputer": 2, "rezultat": True}
    ]

    if twoj_wybor != wybor_komputera:
        for opcja in reguly:
            if opcja["twoj"] is twoj_wybor and opcja["komputer"] is wybor_komputera:
                wynik = opcja["rezultat"]
    else:
        print("Remis!")
        wynik = 0
    return wynik

ilosc_powtorzen = int(input("Wprowadź liczbę rund decydujących o zwycięstwie: "))

if ilosc_powtorzen <= 0:
    while True:
        print("Wprowadź liczbę większą od 0")
        ilosc_powtorzen = int(input("Wprowadź liczbę rund decydujących o zwycięstwie: "))

while wynik_gracza != ilosc_powtorzen != wynik_komputera :
    twoj_wybor = int(input("""
                           Wybór;
                           1 - papier
                           2 - nożyczki
                           3 - kamień 
                           """))

    wybor_komputera = random.randint(1,3)
    print("Wybrałeś {}, natomiast komputer wybrał {}".format(twoj_wybor, wybor_komputera))

    wynik = gra_w_papier(twoj_wybor, wybor_komputera)

    if type(wynik) is bool:
        if wynik is True:
            print("Wygrałeś tę partię")
            wynik_gracza += 1
        else:
            wynik_komputera += 1
            print("Komputer wygrał tę partię")


if wynik_gracza == ilosc_powtorzen:
    print("Gratulacje wygrałeś!")
else:
    print("Niestety komputer wygrał")
