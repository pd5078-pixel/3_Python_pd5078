import numpy as np

# Utwórz macierz NumPy (4 wiersze i 3 kolumny), w której wiersze będą odpowiadać 
# ekspresji 4 różnych genów, a kolumny trzem różnym próbom. Wartości ekspresji mogą
#  być dowolnymi liczbami zmiennoprzecinkowymi.

NumPy = np.array([[1.4, 4.2, 3.7],
                 [4.6, 3.5, 6.1],
                 [7.2, 5.4, 2.9],
                 [5.0, 8.3, 4.5]])

# Zwiększ ekspresję wszystkich genów o 5% i wyświetl wyniki
ekspresja_genow_zwiekszona = NumPy * 1.05
print(ekspresja_genow_zwiekszona)

# Oblicz średnią ekspresję dla każdego genu i wyświetl ją
srednia_ekspresja_genow = np.mean(NumPy, axis=1)
print(srednia_ekspresja_genow)

# Oblicz sumę ekspresji genów dla każdej próby i wyświetl ją.
suma_ekspresji_genow = np.sum(NumPy, axis=1)
print(suma_ekspresji_genow)

# Zaktualizuj macierz, wprowadzając wartości NaN dla kilku wartości. 
NumPy[0, 1] = np.nan
NumPy[2, 2] = np.nan
NumPy[3, 0] = np.nan
print(NumPy)

# Zaktualizuj macierz, wprowadzając wartości NaN dla kilku wartości. 
srednia_ekspresja_genow_bez_nan = np.nanmean(NumPy, axis=1) 
print(srednia_ekspresja_genow_bez_nan)