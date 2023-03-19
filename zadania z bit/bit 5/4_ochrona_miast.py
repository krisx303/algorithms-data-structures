"""
Wybieramy miasto na indexie k, jeżeli można tam zbudować wieżyczkę to budujemy, jeśli nie to cofamy się aż do miasta
gdzie można to zrobić. Po zbudowaniu wieży na polu i-tym przesuwamy się na pole i + 2*k+1 i wykonujemy ponownie algorytm
Gdy cofając się wrócimy na ostatnią wieżę to oznacza że nie istnieje takie rozwiązanie.
"""


def ochrona(A: list[int], k: int) -> list[int]:
    i = k
    z = 0
    T = []
    while True:
        for j in range(2*k+1):
            if i - j > len(A) - 1:
                continue
            if A[i - j] == 1:
                # print("1 on", i - j)
                z = i - j + k
                T.append(i - j)
                i = i - j + 2 * k + 1
                # print("new i", i)
                # print("z", z)
                break
            if j == 2 * k and z < len(A)-1:
                return []
        if z >= len(A)-1:
            return T


if __name__ == "__main__":
    A = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    k = 3
    print(ochrona(A, k))
