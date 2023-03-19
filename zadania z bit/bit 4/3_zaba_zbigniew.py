"""
f(i, y) - minimalna liczba skoków potrzebna aby dostać się na liść i mając y energii

"""


def zaba(A: list[int]) -> int:
    n = len(A)
    F = [[10000 for _ in range(n)] for _ in range(n)]
    k = A[0]
    for i in range(k + 1):
        F[0][i] = 0

    def f(i: int, y: int) -> int:
        if i < 0 or y < 0 or y > n-1 or i > n-1:
            return 10000
        if F[i][y] != 10000:
            return F[i][y]
        m = 10000
        for k in range(1, i+1):
            m = min(m, f(i - k, y + k)+1)
        F[i][y] = m
        return m

    for u in range(1, n):
        for i in range(n-1, -1, -1):
            x = f(u, i)
            if x == 10000:
                continue
            for o in range(1, A[u]+1):
                if i + o < n:
                    if F[u][i + o] > x:
                        F[u][i+o] = x
    return min(*F[-1])


if __name__ == "__main__":
    # A = [4, 5, 2, 4, 1, 2, 1, 0]
    A = [2, 2, 1, 0, 0, 0]
    print(zaba(A))
