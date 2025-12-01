import collections

def opis_komorki():
    return "Komórka to podstawowa jednostka życia."

def licz_nukleotydy(sekwencja):
    wystapienia_nukleotydu = collections.Counter(sekwencja)
    return wystapienia_nukleotydu
