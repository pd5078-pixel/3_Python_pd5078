nukleotydy =  ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G'] 
zasady_azotowe =  ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')

# pierwszy element listy
print(nukleotydy[0])

# ostatni element listy
print(nukleotydy[-1])

# pierwszy element krotki
print(zasady_azotowe[0])

# ostatni element krotki
print(zasady_azotowe[-1])

# modyfikacja elementu listy
nukleotydy[1] = 'C'
print(nukleotydy)

# modyfikacja elementu krotki - nie da się
# zasady_azotowe[1] = 'Uracyl'
# print(zasady_azotowe)
# TypeError: 'tuple' object does not support item assignment

nukleotydy.append("A")
print(nukleotydy)

# drukowanie elementów listy na dwa sposoby 

for nukleotyd in nukleotydy:
    print(nukleotyd)

for i in range(len(nukleotydy)):
    print(nukleotydy[i])

# drukowanie elementów krotki na dwa sposoby 

for zasada in zasady_azotowe:
    print(zasada)

for i in range(len(zasady_azotowe)):
    print(zasady_azotowe[i])

# skorzystaj z list comprehension, aby utworzyć nową listę na podstawie istniejącej

nukleotydy_bez_guaniny = [n for n in nukleotydy if n!='G']
print(nukleotydy_bez_guaniny)
