import numpy as np
from physics import oblicz_przyspieszenia

# Dane testowe
masy = [1.0, 1.0, 1.0]
pozycje = [[-0.5, 0.0], [0.5, 0.0], [0.0, 0.866]]
G = 1.0

# Wywołanie funkcji 
wynik = oblicz_przyspieszenia(masy, pozycje, G)
print('Przyspieszenia:', wynik)