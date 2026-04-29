import numpy as np
import matplotlib.pyplot as plt 
import numba as nb
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

#delta E
#każdy spin ma 8 sąsiadów, sj _nn nearest neighbors
from numba import njit

@njit
def delta_E(S, x, y, N, J, B):
    gora  = S[(x - 1) % N, y]
    dol   = S[(x + 1) % N, y]
    lewo  = S[x, (y - 1) % N]
    prawo = S[x, (y + 1) % N]
    
   #przekątne
    lewo_gora   = S[(x - 1) % N, (y - 1) % N]
    prawo_gora  = S[(x - 1) % N, (y + 1) % N]
    lewo_dol    = S[(x + 1) % N, (y - 1) % N]
    prawo_dol   = S[(x + 1) % N, (y + 1) % N]
    
    suma_nn = gora + dol + lewo + prawo + lewo_gora + prawo_gora + lewo_dol + prawo_dol
    dE = 2 * S[x, y] * (J * suma_nn + B)
    
    return dE

#makrokrok
@njit
def makrokrok(S, N, J, B, beta):
    for _ in range(N * N): #całe pole maceirzy dostępne
        x = np.random.randint(0, N)
        y = np.random.randint(0, N) #losowanie wsp w macierzy
        
        dE = delta_E(S, x, y, N, J, B) #wywołanie dE
        
        if dE <0:
            S[x,y] = (-1)* S[x,y] #odwrócenie spinu
        else:
            prawdop = np.exp(-beta*dE)
            szansa=np.random.rand() #losowanie z zakresu 0,1 rozkald jendostajny
            if szansa < prawdop:
                S[x,y] = (-1)* S[x,y] #odwrócenie spinu
    return S
   
#delta E bez numby
#każdy spin ma 8 sąsiadów, sj _nn nearest neighbors
def delta_E_bez_numby(S, x, y, N, J, B):
    gora  = S[(x - 1) % N, y]
    dol   = S[(x + 1) % N, y]
    lewo  = S[x, (y - 1) % N]
    prawo = S[x, (y + 1) % N]
    
   #przekątne
    lewo_gora   = S[(x - 1) % N, (y - 1) % N]
    prawo_gora  = S[(x - 1) % N, (y + 1) % N]
    lewo_dol    = S[(x + 1) % N, (y - 1) % N]
    prawo_dol   = S[(x + 1) % N, (y + 1) % N]
    
    suma_nn = gora + dol + lewo + prawo + lewo_gora + prawo_gora + lewo_dol + prawo_dol
    dE = 2 * S[x, y] * (J * suma_nn + B)
    
    return dE

#makrokrok bez numby

def makrokrok_bez_numby(S, N, J, B, beta):
    for _ in range(N * N): #całe pole maceirzy dostępne
        x = np.random.randint(0, N)
        y = np.random.randint(0, N) #losowanie wsp w macierzy
        
        dE = delta_E_bez_numby(S, x, y, N, J, B) #wywołanie dE
        
        if dE <0:
            S[x,y] = (-1)* S[x,y] #odwrócenie spinu
        else:
            prawdop = np.exp(-beta*dE)
            szansa=np.random.rand() #losowanie z zakresu 0,1 rozkald jendostajny
            if szansa < prawdop:
                S[x,y] = (-1)* S[x,y] #odwrócenie spinu
    return S

#symulacja
import time  #do pomiaru czasu wykonania symulacji
def symulacja(S, N, J, B, beta, M,uzyj_numba=True):
    S=S.copy()
    hist_m=np.zeros(M) #historia mmagnetyzacji
    klatki_animacji = np.zeros((M, N, N)) #klatki animacji

    start_time = time.time() #poacztek liczenia czasu
    for i in range(M):
        if uzyj_numba:
            S = makrokrok(S, N, J, B, beta)
        else:
            S = makrokrok_bez_numby(S, N, J, B, beta)
    
        magnetyzacja = np.sum(S) / (N * N) 
        hist_m[i] = magnetyzacja
        klatki_animacji[i] = S.copy() #zapisanie klatki

    end_time = time.time()
    print('Czas wykonania:', end_time - start_time, 's dla uzyj_numba=', uzyj_numba)
    return hist_m, klatki_animacji #do wykresów
