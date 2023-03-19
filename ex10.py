"""
*Problem: 
    'Zscalić' dwie posortowane tablice X i Y o długościach m i n bez dodatkowych struktur. 
    (Posortowane dane mają znaleźć się w zadanych tablicach).
*Rozwiązanie:
    Iterując po elementach listy pierwszej. Jeśli i-ty element jest mniejszy od Y[0] to jest na swojej pozycji.
    Jeśli natomiast jest większy to zamieniamy X[i] oraz Y[0], ponadto 'przesuwamy Y[0] na właściwą pozycję w tablicy Y.
*Złożoności:
    !Obliczeniowa: O(m*n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/inplace-merge-two-sorted-arrays/
"""

def merge(X, Y):
 
    m = len(X)
    n = len(Y)
    for i in range(m):
        if X[i] > Y[0]:
 
            temp = X[i]
            X[i] = Y[0]
            Y[0] = temp
 
            first = Y[0]
            k = 1
            while k < n and Y[k] < first:
                Y[k - 1] = Y[k]
                k = k + 1
 
            Y[k - 1] = first
 
  
X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]

merge(X, Y)

print("X:", X)
print("Y:", Y)