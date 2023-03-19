"""
f(i, j) - największa piękność z i talerzy z pierwszych j stosów
"""


def talerze(S: list[list[int]], P: int) -> int:
    N = len(S)
    k = len(S[0])
    F = [[0 for _ in range(P+1)] for _ in range(N+1)]

    for n in range(N):
        for o in range(1, k):
            S[n][o] += S[n][o-1]

    def s(i: int, j: int) -> int:
        if j == 0:
            return 0
        return S[i][j-1]

    def f(i: int, j: int) -> int:
        if j <= 0:
            return 0
        if i == 0:
            if j > k:
                return 0
            return S[0][j-1]
        if F[i][j] != 0:
            return F[i][j]
        m = 0
        for l in range(k+1):
            if j - l < 0:
                continue
            o = f(i-1, j - l)
            # print(f"{i} {j} take {j-l} plates from 0-{i-1} stacks = {o} and add {l} plates from {i} stack with sum {s(i, l)}---{o + s(i,l)}")
            m = max(m, o + s(i, l))
        F[i][j] = m
        return m
    return f(N-1, P)


if __name__ == "__main__":
    S = [[1, 1, 1, 1],
         [2, 3, 7, 1],
         [2, 1, 3, 7],
         [4, 2, 0, 0]]
    P = 4
    print(talerze(S, P))
