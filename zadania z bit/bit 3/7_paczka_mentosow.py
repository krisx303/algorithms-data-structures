"""
f(i, j) - maksymalna wartość jaką możemy uzyskać z A[i:j]

f(i, j) = max(min(f(i+2, j), f(i+1, j-1)) + A[i], min(f(i+1, j-1), f(i, j-2)) + A[j])

f(i+2, j) + A[i] - bierzemy z lewej i przeciwnik też
f(i+1, j-1) + A[i] - bierzemy z lewej a przeciwnik z prawej
f(i+1, j-1) + A[j] - bierzemy z prawej a przeciwnik z lewej
f(i, j-2) + A[j] - bierzemy oboje z prawej
"""


def mentosy(T: list[int]) -> int:
    n = len(T)
    F = [[0 for _ in range(n)] for _ in range(n)]

    def f(i:int, j:int) -> int:
        if i > j or i > n-1 or j < 0:
            return 0
        if i == j:
            return T[i]
        if F[i][j] != 0:
            return F[i][j]
        F[i][j] = max(min(f(i+2, j), f(i+1, j-1)) + T[i],
                      min(f(i+1, j-1), f(i, j-2)) + T[j])
        return F[i][j]

    f(0, n-1)
    return F[0][n-1]


if __name__ == "__main__":
    T = [9, 5, 100, 2, 3]
    print(mentosy(T))

# f(0, 4) = max(9 + min(f(2, 4), f(1, 3)), 3 + min(f(1, 3), f(0, 2)))
# f(2, 4) = max(100 + min(f(4, 4), f(3, 3)), 3 + min(f(3, 3), f(2, 2)))
# f(2, 4) = max(100 + min(3, 2), 3 + min(2, 100))
# f(2, 4) = max(100 + 2, 3 + 2) = 102
#
# f(1, 3) = max(5 + min(f(3, 3), f(2, 2)), 2 + min(f(2, 2), f(1, 1)))
# f(1, 3) = max(5 + min(2, 100), 2 + min(100, 5))
# f(1, 3) = max(5 + 2, 2 + 5) = 7