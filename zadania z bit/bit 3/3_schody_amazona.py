"""
f(i) - liczba możliwych dróg do polo i

Dla każdego T[i] zawierającego liczbę skoków j, dodaj do j następnych komórek liczbę możliwych przejść do komórki F[i]

Złożoność obliczeniowa: O(n^2)
Złożoność pamięciowa: O(n)
"""

def schody(T: list[int]) -> list[int]:
    n = len(T)
    F = [0 for i in range(n)]
    F[0] = 1
    for i in range(n):
        for x in range(1, T[i]+1):
            F[i+x] += F[i]
    return F

if __name__ == "__main__":
    T = [1, 3, 2, 1, 0]
    print(schody(T))
