"""
f(x, y) - minimalny koszt dojścia do komórki (x, y) z pola (0, 0)

Rozwiązanie top-down. Wywołujemy rekurencyjną funkcję f(n-1, n-1) która oblicza wszystkie poprzednie wartości

Złożoność obliczeniowa: O(n^2)
Złożoność pamięciowa: O(n^2)
"""


def pathfinding(T: list[list[int]]) -> int:
    n = len(T)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    INF = 100000
    F[0][0] = 0

    def f(x: int, y: int, d: int) -> int:
        # jeżeli pozycja jest spoza zakresu to nie da się tam dotrzeć - INF
        if x < 0 or x > n - 1 or y < 0:
            return INF
        # jeżeli wartość już jest obliczona to ją zwracamy
        if F[x][y] != -1:
            return F[x][y]
        m = INF
        # 'switch' dla poszczególnych kierunków: 0 - przyszliśmy z lewej, 1 - z prawej, 2 - z dołu
        if d == 0:
            m = min(m, f(x + 1, y, 0) + T[x][y], f(x, y - 1, 2) + T[x][y])
        elif d == 1:
            m = min(m, f(x - 1, y, 1) + T[x][y], f(x, y - 1, 2) + T[x][y])
        else:
            m = min(m, f(x + 1, y, 0) + T[x][y], f(x - 1, y, 1) + T[x][y], f(x, y - 1, 2) + T[x][y])
        F[x][y] = m
        return F[x][y]

    f(n-1, n-1, 1)
    for x in F:
        print(x)
    return F[n-1][n-1]


if __name__ == "__main__":
    T = [[0, 1, 4, 9],
         [4, 2, 6, 2],
         [5, 6, 8, 3],
         [3, 2, 1, 1]]
    print(pathfinding(T))
