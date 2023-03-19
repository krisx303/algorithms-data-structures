"""
*Problem: 
    Znaleźć w tablicy A majorantę (element który pojawia się więcej niż N/2 razy).
*Rozwiązanie:
    Używając funkcji quickselect znajdujemy element który znajdzie się na środkowej pozycji w tablicy.
    Następnie zliczamy ilość wystąpień tego elementu w tablicy.
    Jeśli przekracza n//2 to znaczy że jest majorantą, w przeciwnym wypadku ta nie występuje.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/find-majority-element-in-an-array-boyer-moore-majority-vote-algorithm/
"""

from sorting.quickselect import quickselect

t = [2, 8, 7, 2, 2, 5, 2, 2, 1, 2, 3]

candidat = quickselect(t, len(t)//2)

count = 0
for i in t:
    if i == candidat:
        count += 1

if count > len(t)//2:
    print(candidat)
else:
    print("brak majoranty")