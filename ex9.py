"""
*Problem: 
    Posortować tablicę składającą się tylko z liczb 0/1/2. Możliwie jak najszybciej.
*Rozwiązanie:
    Tworzymy dwa znaczniki na tablicy (start) oraz (end).
    Iterując po zadanej tablicy analizujemy wartość pod i-tym indexem.
    Jeśli t[i] == 0 to zamieniamy liczby t[start] z t[i], a jeśli t[i] == 2 to t[end] z t[i].
    Przy czym przesuwamy znaczniki odpowiednio o jeden w prawo i jeden w lewo.
    Kończymy gdy znacznik i oraz end się 'miną'.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/sort-array-containing-0s-1s-2s-dutch-national-flag-problem/
"""

t = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]

start = 0
end = len(t)-1
i = 0
while i <= end:
    if t[i] == 2:
        t[i], t[end] = t[end], t[i]
        end -= 1
    elif t[i] == 0:
        t[i], t[start] = t[start], t[i]
        start += 1
        i += 1
    else:
        i += 1
print(t)