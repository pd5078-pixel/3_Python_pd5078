try:
    with open("sekwencje.txt", "r") as plik:
        tresc = plik.read()
        print(tresc)
except FileNotFoundError:
    print("Plik nie został znaleziony.")



class NieprawidlowaSekwencjaDNA(Exception):
    def __init__(self, wiadomosc="Sekwencja zawiera nieprawidłowe nukleotydy."):
        self.wiadomosc = wiadomosc
        super().__init__(wiadomosc)

try:
    nowa_sekwencja = input("Proszę podać sekwencję DNA: ").upper()

    if not set(nowa_sekwencja).issubset({"A", "T", "C", "G"}):
        raise NieprawidlowaSekwencjaDNA()
    
    print("Sekwencja poprawna.")

    with open("nowy_plik", "w") as plik:
        plik.write(nowa_sekwencja)
    
    print("Zapisano do pliku nowa_sekwencja.txt.")

except NieprawidlowaSekwencjaDNA as e:
    print(e.wiadomosc)