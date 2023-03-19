"""
Wyszukujemy dwóch wartości na przekątnej głównej macierzy ([0][0] oraz [n-1][n-1])
Następnie liniowo przechodząc po głównej macierzy jeżeli wartość jest mniejsza od najmniejszej na przekątnej
to należy ją umieścić pod. A gdy jest większa od największej na przekątnej to nad.
"""


def quickselect(A: list[list[int]], k: int) -> int:
    return select(A, 0, k, len(A)**2-1)


def select(A, p, k, r):
    n = len(A)
    if p == r:
        return A[p//n][p % n]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q//n][q % n]
        elif q < k:
            return select(A, q+1, k, r)
        else:
            return select(A, p, k, q-1)


def partition(A, p, r):
    n = len(A)
    x = A[r//n][r%n]
    i = p - 1
    for j in range(p, r):
        if A[j//n][j%n] <= x:
            i += 1
            A[i//n][i % n], A[j//n][j%n] = A[j//n][j%n], A[i//n][i%n]
    A[(i + 1)//n][(i+1)%n], A[r//n][r%n] = A[r//n][r%n], A[(i + 1)//n][(i+1)%n]
    return i + 1


def mediana(T: list[list[int]]) -> list[list[int]]:
    n = len(T)
    D = [[0 for _ in range(n)] for _ in range(n)]
    x1 = ((n-1)*n)/2
    minx = quickselect(T, x1)
    x2 = n**2 - x1 - 1
    maxx = quickselect(T, x2)
    io = 0
    ioi = 1
    jo = 0
    joj = 1
    po = 0
    for i in range(n**2):
        x = T[i//n][i % n]
        if x < minx:
            D[ioi][io] = x
            io += 1
            if io == ioi:
                ioi += 1
                io = 0
        elif x > maxx:
            D[joj][n-1-jo] = x
            jo += 1
            if jo == joj:
                joj -= 1
                jo = 0
        else:
            D[po][po] = x
    return D


if __name__ == "__main__":
    T = [[2, 3, 5],
         [7, 11, 13],
         [17, 19, 23]]
    print(mediana(T))