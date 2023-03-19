"""
f(i) = maksymalny zysk po sprzedaży pręta o długości i

F - Tablica spamiętująca wyniki
T - Tablica z cenami prętów

f(i) = max{k=0, k<=i}(F[i-k] + T[k])

Złożoność obliczeniowa: O(n^2)
Złożoność pamięciowa: O(n)
"""

def pret(T: list[int]) -> list[int]:
    n = len(T)
    F = [0 for _ in range(n)]
    for i in range(1, n):
        m = 0
        for k in range(i+1):
            x = F[i - k] + T[k]
            m = max(m, x)
        F[i] = m
    return F


if __name__ == "__main__":
    n = 5
    T = [0, 2, 3, 6, 9, 5]
    print(pret(T))