"""
*Problem: 
    'Zscalić' dwie tablice X oraz Y o długościach m i n.
    Z tym że tablica X jest posortowana ale posiada n 'dziur' czyli 0. Y jest posortowana.
*Rozwiązanie:
    Tworzymy znacznik j który wskazuje na miejsce w tablicy Y.
    Iterujemy po elementach tablicy X, dopóki spotykane elementy są mniejsze od Y[j] to przestawiamy je na początek tablicy X.
    Jeśli nie to wstawiamy element z Y i przesuwamy znacznik w prawo.
*Złożoności:
    !Obliczeniowa: O(m+n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/merge-two-arrays-satisfying-given-constraints/
"""


def merge(X, Y):
    m = len(X)
    n = len(Y)
    j = 0
    k = 0
    i = 0
    while i < m:
        if X[i] < Y[j]:
            if X[i] != 0:
                X[k] = X[i]
                k += 1
            i += 1
            continue
        
        X[k] = Y[j]
        k += 1
        j += 1
    while j < n:
        X[k] = Y[j]
        k += 1
        j += 1


X = [0, 2, 0, 3, 0, 0, 5, 6, 0, 0]
Y = [1, 4, 8, 9, 10, 15]
merge(X, Y)
print(X)