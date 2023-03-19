"""
*Problem: 
    Przenieść w tablicy wszystkie zera na koniec nie zmieniając kolejności pozostałych elementów.
*Rozwiązanie:
    Iterujemy po zadanej tablicy, jeśli dany element jest różny od zera to zamieniamy go z wolnym miejscem po lewej.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/move-zeros-present-array-end/
"""

t = [6, 0, 8, 2, 3, 0, 4, 0, 1]

j = 0
for i in range(len(t)):
    if t[i] != 0:
        t[i], t[j] = t[j], t[i]
        j += 1
print(t)