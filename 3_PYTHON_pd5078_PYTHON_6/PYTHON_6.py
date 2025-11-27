sekwencja_1 = "ACTGCGTGA"
sekwencja_2 = "TAGCTAGCTGACTG"
sekwencja_laczna = sekwencja_1 + sekwencja_2
fragment_sekwencji = sekwencja_laczna[7:13]
wystepowanie_A = sekwencja_laczna.count("A")
zmiana_T_na_U = sekwencja_laczna.replace("T", "U")
pozycja_pierwszego_GC = sekwencja_laczna.find("GC")
pozycja_ostatniego_GC = sekwencja_laczna.rfind("GC")
wynik = f"Połączona sekwencja to: {sekwencja_laczna}.\nWycięty fragment sekwencji to: {fragment_sekwencji}.\nAdenina występuje w polączonej sekwencji {wystepowanie_A} razy.\nTak wygląda sekwencja po zamianie tyminy na uracyl: {zmiana_T_na_U}.\n\"GC\" po raz pierwszy pojawia się na pozycji {pozycja_pierwszego_GC}, a po raz ostatni na pozycji {pozycja_ostatniego_GC}."
print(wynik)
