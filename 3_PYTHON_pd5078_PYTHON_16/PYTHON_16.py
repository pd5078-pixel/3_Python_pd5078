import numpy as np
import matplotlib.pyplot as plt

geny = ['GenA', 'GenB', 'GenC'] 
proby = ['Proba1', 'Proba2', 'Proba3']
ekspresja = np.array([
[5.1, 2.3, 7.8], # Ekspresja GenA
[3.2, 4.5, 6.1], # Ekspresja GenB
[4.8, 5.5, 3.9] # Ekspresja GenC
])

plt.figure(figsize=(12, 10))

# Wykres liniowy:
plt.subplot(2, 2, 1)  
plt.plot(proby, ekspresja, marker='o')
plt.title('Ekspresja genów w różnych próbach')
plt.xlabel('Próby')
plt.ylabel('Poziom ekspresji')
plt.legend(['GenA', 'GenB', 'GenC'])


# Wykres słupkowy:
plt.subplot(2, 2, 2)  
bar_width = 0.2
x = np.arange(len(proby))

for i, gen in enumerate(geny):
    plt.bar(x + i * bar_width, ekspresja[i], width=bar_width, label=gen)

plt.title('Ekspresja genów w różnych próbach')
plt.xlabel('Próby')
plt.ylabel('Poziom ekspresji')
plt.xticks(x + bar_width, proby)
plt.legend()

# Wykres rozrzutu
plt.subplot(2, 2, 3)
plt.scatter(ekspresja[0], ekspresja[1], color='blue', label='GenA vs GenB')
plt.title('Wykres rozrzutu ekspresji GenA i GenB')
plt.xlabel('Ekspresja GenA')
plt.ylabel('Ekspresja GenB')
plt.legend()
plt.grid(True)
plt.savefig('ekspresja_genow.png')
plt.show()

