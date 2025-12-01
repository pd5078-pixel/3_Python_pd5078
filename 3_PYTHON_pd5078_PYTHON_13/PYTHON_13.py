import os
import datetime
import biologia

nowy_katalog = "dane_bio"

if not os.path.exists(nowy_katalog):
    os.mkdir(nowy_katalog)
    print(f"Katalog {nowy_katalog} został utworzony.")

sciezka_do_pliku = os.path.join(nowy_katalog, "nukleotydy.txt")

with open(sciezka_do_pliku, "w") as plik:

    sekwencja_DNA = "AGCTTAGCTAAGGCT"
    
    opis_komorki = biologia.opis_komorki()
    licznik_nukleotydow = biologia.licz_nukleotydy(sekwencja_DNA)

    plik.write(f"{str(datetime.datetime.now())}\n\n{opis_komorki}")

    plik.write(f"\nŁączna liczba nukleotydów w sekwencji {sekwencja_DNA} to {sum(licznik_nukleotydow.values())}.")
    
    plik.write(f"\nAdenina występuje {licznik_nukleotydow['A']} razy, tymina {licznik_nukleotydow['T']} razy, guanina {licznik_nukleotydow['G']} razy, a cytozyna {licznik_nukleotydow['C']} razy.")

    print(sciezka_do_pliku, "został utworzony")
