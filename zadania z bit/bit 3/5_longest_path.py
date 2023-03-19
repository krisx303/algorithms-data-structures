"""
f(x, y) - długość najdłuższej rosnącej ścieżki od punktu (x0, y0) do punktu (x, y)

Mając punkt początkowy (x0, y0) rozpoczynamy od niego rekurencję.
W tablicy pomocniczej F zapisujemy aktualnie długość najdłuższej ścieżki do punktu (x, y).
Gdy w jakąś stronę można iść powiększając ścieżkę to wykonujemy rekurencję w tym punkcie zwiększając wartość w F.

Złożoność obliczeniowa: O(n^2)
Złożoność pamięciowa: O(n^2)
"""


def path(T: list[list[int]], x0: int, y0: int) -> int:
    n = len(T)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    F[x0][y0] = 1
    m = 1

    def f(x: int, y: int):
        nonlocal m
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                continue
            if T[nx][ny] > T[x][y] and F[nx][ny] < F[x][y] + 1:
                F[nx][ny] = F[x][y] + 1
                if F[x][y] + 1 > m:
                    m = F[x][y] + 1
                f(nx, ny)

    f(x0, y0)
    return m


if __name__ == "__main__":
    T = [[0, 1, 7, 9],
         [4, 2, 6, 2],
         [5, 6, 8, 3],
         [3, 2, 9, 1]]  # 0-1-2-4-5-6-8-9 czyli 8
    print(path(T, 0, 0))
