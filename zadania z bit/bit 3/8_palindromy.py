"""
f(i, j) - czy wyraz od i do j jest palindromem

f(i, j) = S[i] == S[j] and f(i+1, j-1)
"""


def palindromy(S: str) -> int:
    n = len(S)
    F = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = True
    for i in range(n - 1):
        F[i][i + 1] = (S[i] == S[i + 1])

    def f(i: int, j: int) -> bool:
        return F[i + 1][j - 1] and S[i] == S[j]

    for i in range(n-2, 0, -1):
        for j in range(i):
            F[j][n-i+j] = f(j, n-i+j)

    for i in range(1, n):
        for j in range(i):
            if F[j][n-i+j]:
                return n-i+1
    return 1


if __name__ == "__main__":
    print(palindromy("ukoooketwquyabababa"))


# (2, 0), (3, 1), (4, 2), (5, 3), (6, 4)
#         (3, 0), (4, 1), (5, 2), (6, 3)
#                 (4, 0), (5, 1), (6, 2)
#                         (5, 0), (6, 1)
#                                 (6, 0)

