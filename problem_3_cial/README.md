# Problem Trzech Ciał - Symulacja 2D

## Autorzy
- [Maja] – podstawa symulacji, GUI, animacja, JSON
- [Maria] – część rozszerzona
- [Paulina] – część rozszerzona

---

## Co to za program?

Program symuluje ruch trzech ciał, które przyciągają się grawitacyjnie (jak Ziemia, Księżyc i Słońce).  
Użytkownik może:
- ustawić masy, pozycje i prędkości trzech ciał
- wybrać gotową konfigurację z listy
- uruchomić animację i obserwować trajektorie
- zatrzymać, zresetować i eksperymentować z parametrami

## Co robi ten program?

Program wykonuje obliczenia fizyczne dla problemu trzech ciał takie jak:

- Oblicza przyspieszenia każdego ciała wynikające z grawitacji
- Wykonuje symulację krok po kroku (metodą numeryczną)
- Wczytuje dane początkowe z pliku JSON
- Wyświetla w konsoli stan początkowy i końcowy symulacji
- Zawiera 4 gotowe konfiguracje układów

## Aby uruchomić należy wpisać w terminal: python main.py