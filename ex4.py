"""
*Problem: 
    Posortowanie listy składającej się tylko z zer i jedynek.
*Rozwiązanie: 
    Iterując po tablicy od końca, znajdując 1 przenosimy ją na ostatnie wolne miejsce.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1) - brak żadnych dodatkowych struktur.
https://www.techiedelight.com/sort-binary-array-linear-time/
"""

t = [1, 0, 1, 0, 1, 0, 0, 1]

j = len(t)-1
for i in range(len(t)-1, -1, -1):
    if t[i] == 1:
        t[j], t[i] = t[i], t[j]
        j -= 1

print(t)