import pandas as pd
import numpy as np
from openpyxl import load_workbook

df = pd.DataFrame({
'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
'Proba1': [5.1, 2.3, np.nan, 4.4],
'Proba2': [3.2, 4.5, 3.9, np.nan],
'Proba3': [6.3, 5.6, np.nan, 6.6]
})


# Sprawdź, które wartości w DataFrame są brakujące (NaN), i wyświetl wynik
print(df.isnull())

# Usuń wszystkie wiersze z brakującymi danymi i wyświetl nowy DataFrame
df_bez_nan = df.dropna()
print("DataFrame bez wierszy zawierających NaN:")
print(df_bez_nan)

# Uzupełnij brakujące dane za pomocą średnich wartości dla każdej kolumny
df_uzupelnione = df.fillna(df[["Proba1", "Proba2", "Proba3"]].mean())
print("DataFrame z uzupełnionymi wartościami NaN średnią kolumny:")
print(df_uzupelnione)


# ○ Wyciągnij dane dotyczące genu GenA i wyświetl je
info_genA = df_uzupelnione['Gen'] == 'GenA'
print("Informacje o GenA:")
print(df_uzupelnione[info_genA])

# Oblicz średnią ekspresję genów dla każdej z próbek i wyświetl wynik
srednia_ekspresja_dla_probek = df[['Proba1', 'Proba2', 'Proba3']].mean()
print("Średnia ekspresja dla każdej próbki:")
print(srednia_ekspresja_dla_probek)

# Filtrowanie: Wyświetl wszystkie geny, których ekspresja w próbce 1 wynosi więcej niż 4
ekspresja_wiecej_niz_4_w_probce_1 = df_uzupelnione['Proba1'] > 4
print("Geny z ekspresją większą niż 4 w Próbie 1:") 
print(df_uzupelnione[ekspresja_wiecej_niz_4_w_probce_1])

# Zapisz wynikowy DataFrame (po uzupełnieniu brakujących wartości) do pliku CSV o nazwie
# wynik.csv bez indeksów
df_uzupelnione.to_csv('wynik.csv', index=False    )