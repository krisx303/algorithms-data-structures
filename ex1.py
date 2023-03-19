"""
*Problem: 
    Znaleźć wszystkie pary liczb w tablicy nieposortowanej które w sumie dają liczbę k.
*Rozwiązanie:
    Sortowanie kopcem (standardowe), następnie przesuwając się dwoma wskaźnikami od początku do końca
szukamy pary. Jeśli ich suma jest za mała to przesuwamy prawy wskaźnik. Jeśli za duża to lewy.
Tablica posortowana jest malejąco.
*Złożoności:
    !Obliczeniowa: O(nlogn + n) = O(nlogn)
    !Pamięciowa: O(1) - żadnych dodatkowych struktur
http://www.techiedelight.com/find-pair-with-given-sum-array/
"""


t = [8, 3, 5, 7, 2, 4, 1]


def heapify(tab, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    max_i = i
    if l < n and tab[l] < tab[max_i]:
        max_i = l
    if r < n and tab[r] < tab[max_i]:
        max_i = r
    if max_i != i:
        tab[max_i], tab[i] = tab[i], tab[max_i]
        heapify(tab, n, max_i)


def build_heap(tab, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)


build_heap(t, len(t))
n = len(t)
for i in range(1, n):
    t[0], t[n - i] = t[n - i], t[0]
    heapify(t, n - i, 0)
print(t)

k = 10
i = 0
j = n - 1
while i < j:
    s = t[i] + t[j]
    if s == k:
        print((t[i], t[j]))
        i += 1
    elif s < k:
        j -= 1
    else:
        i += 1
