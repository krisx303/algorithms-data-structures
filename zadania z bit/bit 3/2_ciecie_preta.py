"""
Analogiczne rozwiązanie co w pierwszym.
Przy wyliczaniu najmniejszego kosztu pręta o długości i zapisujemy jaki pręt daje to rozwiązanie do oddzielnej tablicy.
Przykład jeżeli dla pręta o długości 4 największy koszt daje pręt o długości 3 i nowo pocięty o długości 1 to C[4] = 1
Złożoność obliczeniowa: O(n^2)
Złożoność pamięciowa: O(n)
"""


# T - koszta prętów
def pret(T: list[int]) -> list[int]:
    n = len(T)
    F = [0 for _ in range(n)]
    C = [0 for _ in range(n)]

    # obliczanie f(i) dla każdego i
    for i in range(1, n):
        # m - maxymalny możliwy koszt za pocięcie pręta, mi - długość docinana do uzyskania najlepszej ceny
        m = 0
        mi = 0
        # wyszukiwanie najlepszej ceny poprzez sprawdzanie wszystkich wcześniejszych kosztów prętów o długości i - k
        # + cena pręta k
        for k in range(i + 1):
            x = F[i - k] + T[k]
            if x > m:
                m = x
                mi = k
        F[i] = m
        C[i] = mi
    return C


def rozw(C, x) -> list[int]:
    W = []
    while x > 0:
        W.append(C[x])
        x -= C[x]
    return W


if __name__ == "__main__":
    T = [0, 2, 3, 6, 9, 5]
    C = pret(T)
    print(rozw(C, 5))

# # wypisywanie rozwiązania
# x = 5
# while x > 0:
#     print("Pręt długości:", C[x], "w cenie:", T[C[x]])
#     x = x - C[x]
