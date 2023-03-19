"""
f(i, j) - największy zysk z pociętej tkaniny na kwadracie (0, 0) - (i, j)

f(i, j) = max(for p = [x, y, c] in P){f(i-x, y) + f(i, j - y) + f(i - x, j - y) + c}
"""


def tkanina(P: list[tuple[int, int, int]], X: int, Y: int) -> int:
    F = [[0 for _ in range(Y+1)] for _ in range(X+1)]

    def f(i: int, j: int) -> int:
        if i <= 0 or j <= 0:
            return 0
        m = 0
        for p in P:
            x, y, c = p
            if i - x < 0 or j - y < 0:
                continue
            m = max(m, f(i-x, y) + f(x, j-y) + f(i-x, j-y) + c)
        F[i][j] = m
        return m
    return f(10, 10)


if __name__ == "__main__":
    P = [(1, 2, 1),
         (10, 10, 100),
         (5, 4, 80),
         (2, 10, 50)]
    print(tkanina(P, 10, 10))
