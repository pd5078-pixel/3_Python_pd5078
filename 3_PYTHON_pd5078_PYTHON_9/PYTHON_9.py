# Utwórz zbiór zawierający unikalne elementy oraz słownik

mutacje_1 = {"missense", "nonsense", "silent", "frameshift"}

geny = {
    "TP53": "hamuje rozwój nowotworów",
    "BRCA1": "naprawa DNA, ochrona przed rakiem piersi/jajnika",
    "CFTR": "transport jonów chlorkowych w komórkach",
    "HTT": "funkcje neuronów, związany z chorobą Huntingtona",
    "APOE": "metabolizm lipidów, ryzyko choroby Alzheimera"
}

# Dodaj nowy element do zbioru oraz nową parę klucz-wartość do słownika

mutacje_1.add("insercja")

geny["INS"] = "produkcja insuliny"

# Sprawdź, czy określony element istnieje w zbiorze oraz czy klucz znajduje się w słowniku, korzystając z operatora in

if "BRCA1" in geny:
    print("Gen BRCA1 istnieje w słowniku.") 

if "missense" in mutacje_1:
    print("Mutacja missense istnieje w zbiorze.")

# Usuń jeden z elementów ze zbioru, korzystając z metody remove() lub discard(). 

mutacje_1.discard("silent")

# Wyświetl zawartość słownika: klucze oraz wartości za pomocą iteracji pętli for

for klucz, wartosc in geny.items():
    print(klucz, wartosc)

# Skorzystaj z instrukcji warunkowej if-else, aby sprawdzić długość zbioru. Jeśli zawiera więcej niż 3 elementy, wydrukuj odpowiedni komunikat. 

print("Zbiór ma ponad 3 elementy.") if len(mutacje_1) > 3 else print("Zbiór ma 3 lub mniej elementów.")

# Skorzystaj z instrukcji warunkowej, aby sprawdzić, czy określony klucz istnieje w słowniku i jeśli tak, wyświetl jego wartość. 

if "CFTR" in geny:
    print(geny["CFTR"])

# Przeprowadź operację łączenia zbiorów (za pomocą metody union()), a następnie wydrukuj wynik.

mutacje_2 = {"delecja", "duplikacja", "translokacja", "aneuploidia", "poliploidia"}

mutacje = mutacje_1.union(mutacje_2)
print(mutacje)