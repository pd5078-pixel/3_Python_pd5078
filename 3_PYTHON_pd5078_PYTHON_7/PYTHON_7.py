# Zadeklaruj zmienne typu boolean i przypisz im wartości logiczne na podstawie dowolnych warunków

czy_sekwencja_zawiera_guanine = False
czy_nukleotyd_jest_metylowany = True

# Użyj funkcji bool() do sprawdzenia, czy różne zmienne są puste lub nie. 

liczba_genow_do_analizy = 5
lista_nukleotydow = ["A", "C", "G", "T"]
sekwencja_DNA = "AGTTAACGGACT"
opis_badania = ""

print("Czy istnieją geny do analizy:", bool(liczba_genow_do_analizy))
print("Czy lista nukleotydów coś zawiera:", bool(lista_nukleotydow))
print("Czy posiadamy sekwencję DNA gotową do badania:", bool(sekwencja_DNA))
print("Czy posiadamy opis badania:", bool(opis_badania))

# Przeprowadź kilka operacji arytmetycznych na liczbach oraz wypisz wyniki tych operacji

a = 17
b = 5

suma = a+b
roznica = a-b
iloczyn = a*b
iloraz = a/b
reszta_z_dzielenia = a%b
dzielenie_calkowite = a//b

print("\nOperacje arytmetyczne:")
print(f"\n{a} + {b} = {suma}")
print(f"{a} - {b} = {roznica}")
print(f"{a} * {b} = {iloczyn}")
print(f"{a} / {b} = {iloraz}")
print(f"{a} // {b} = {dzielenie_calkowite}")
print(f"{a} % {b} = {reszta_z_dzielenia}")

# Zastosuj operatory przypisania do zmiany wartości istniejących zmiennych

suma += 4
roznica *= 2
iloczyn /= 5
iloraz -= 7
reszta_z_dzielenia **= 3
dzielenie_calkowite %= 2

print("\nsuma plus 4 to:", suma)
print("roznica razy dwa to:", roznica)
print("iloczyn podzielony przez pięć to:", iloczyn)
print("iloraz minus siedem to:", iloraz)
print("reszta_z_dzielenia do potęgi trzeciej to:", reszta_z_dzielenia)
print("Reszta z dzielenia dzielenie_calkowite przez dwa to:", dzielenie_calkowite)

# Użyj operatorów porównania, aby porównać wartości zmiennych

print("\nOperatory porównania:")
print("Czy a > b?", a > b)
print("Czy a == b?", a == b)
print("Czy suma <= iloczyn?", suma <= iloczyn)
print("Czy lista nukleotydów jest większa niż 2 elementy?", len(lista_nukleotydow) > 2)