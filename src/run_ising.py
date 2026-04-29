import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ising_numba import symulacja
#argparse pozwala podawac parametru jako argumentu w terminalu
# np. python run_ising.py --N 120 --beta 0.55
#jesli nic nie wpisze to bierze domyślne
#parametry wpisywane w terminal
parser = argparse.ArgumentParser(description='Symulacja modelu Isinga')

parser.add_argument('--N', type=int, default=100, help='Rozmiar siatki')
parser.add_argument('--J', type=float, default=1.0, help='Stała oddziaływania')
parser.add_argument('--B', type=float, default=0.0, help='Pole magnetyczne')
parser.add_argument('--beta', type=float, default=0.44, help='Parametr temperaturowy')
parser.add_argument('--M', type=int, default=100, help='Makrokroki')

#zapsiywanie do pliku, w terminalu podaje string
parser.add_argument('--magnetization-file', type=str, default=None, help='Plik do zapisu historii magnetyzacji')
parser.add_argument('--animation-file', type=str, default=None, help='Plik do zapisu animacji magnetyzacji')

#włączanie animacji action='store_true' -jesli podamy --animation to będzie true, jesli nie to false
parser.add_argument('--show-animation', action='store_true', help='Wyświetl animację')

#ODCZYTANIE TERMINALU
args = parser.parse_args() #wszystkie do jednej zmiennej args nazywamy

#OBSŁUGA BŁĘDÓW

try:
    if args.N <= 0:
        raise ValueError('Rozmiar siatki N musi być większy od zera! >.<')
    if args.M <= 0:
        raise ValueError('Liczba makrokroków M musi być większa od zera! >.<')
    if args.beta < 0:
        raise ValueError('Parametr beta (odwrotność temperatury) nie może być ujemny! >.<')

#macierz-losowanie położenia na siatce -spinu
    state=np.random.choice([-1,1],size=(args.N,args.N))

    hist_m, klatki_animacji = symulacja(state, args.N, args.J, args.B, args.beta, args.M)

#sprawdzanie czy użytkownik zapisal plik do historii magnetyzacji
#np.savetxt('nazwa_pliku.txt', zmienna_z_tablica)
    if args.magnetization_file is not None:
        np.savetxt(args.magnetization_file, hist_m)

    #sprawdzanie czy użytkownik chce zapisac animacje
    if args.show_animation or args.animation_file is not None:

        #wykres
        fig, ax = plt.subplots(figsize=(6, 6))
        obraz = ax.imshow(klatki_animacji[0], vmin=-1, vmax=1)
        ax.set_title('Model Isinga - Animacja')

        def aktualizuj(numer_klatki):
            obraz.set_data(klatki_animacji[numer_klatki])
            return [obraz]

        anim = FuncAnimation(fig, aktualizuj, frames=args.M, interval=50, blit=True)
        
        if args.animation_file is not None:
            print('zapisuje animacje do pliku:', args.animation_file)
            anim.save(args.animation_file)

        if args.show_animation: #wyswietanie animacji
            plt.show()

#co jesli sie stanie ValueError:
except ValueError as e:
    print('Błąd danych wejściowych:', e,'Sprobuj jeszcze raz z poprawnymi parametrami! >.<')
except Exception as e:
    print('Nieoczekiwany błąd:', e, ':O')
#trzeba cd src i potem python run_ising.py --show-animation

#TESTOWANIE
#python run_ising.py
#python run_ising.py --N 120 --M 1000 --beta 0.55 --B 0.1 --J 1.0
#python run_ising.py --N 120 --M 1000 --beta 0.55 --B 0.1 --J 1.0 --magnetization-file magnetization.csv


#python run_ising.py --magnetization-file wyniki.csv
#python run_ising.py --show-animation 
#python run_ising.py --show-animation --animation-file animacja.gif

#