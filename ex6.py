"""
*Problem: 
    Znaleźć nadłuższy spójny podciąg w zadanej tablicy którego elementy są kolejnymi liczbami naturalnymi.
    Liczby w podciągu mogą być pomieszane.
*Przykład:
    Input: [2, 0, 2, 1, 4, 3, 1, 0]
    Output:   [0, 2, 1, 4, 3]
*Rozwiązanie:
    Tworzymy tablicę sum prefiksowych kolejnych spójnych podciągów (od 0 do N).
    Sprawdzamy każdy możliwy spójny podciąg (od największych możliwych do najmniejszych):
    t[0:7], t[0:6], t[1:7], t[0:5], t[1:6], t[2:7] ... t[0:1] ... t[6:7] 
    Jeżeli suma elementów danego podciągu t[i:j] jest sumą ciągu arytmetycznego o różnicy 1 i a1 = min(t[i:j])
    to podciąg spełnia warunki zadania.
*Złożoności:
    !Obliczeniowa: O(n^2) - w praktyce sporo mniej
    !Pamięciowa: O(n) - tablica sum prefiksowych
https://www.techiedelight.com/find-largest-sub-array-formed-by-consecutive-integers/
"""

def findSubArray(T):
    n = len(T)
    v = [0]*(n+1)
    s = 0
    for i in range(n):
        s += T[i]
        v[i+1] = s
    for i in range(n-1, 0, -1):
        for j in range(n-i):
            m = min(T[j:j+i])
            if (m + m + (i))*(i+1)/2 == m*(i+1) + (v[j+i+1] - v[j]):
                return (j, j+i+1)



t = [2, 0, 2, 1, 4, 3, 1, 0]

res = findSubArray(t)
print(t[res[0]:res[1]])