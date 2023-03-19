"""
Sortujemy rosąco po polu powierzchni lalki, następnie sprawdzamy każdą z każdą czy dana lalka się w niej zawiera
Jeżeli tak to incrementujemy licznik zawarty w tablicy pomocniczej pod jej indexem i zapisujemy do większej lalki.
"""


def isin(A: tuple[int, int], B: tuple[int, int]) -> bool:
    return A[0] <= B[0] and A[1] >= B[1]


def lalki(M: list[tuple[int, int]]) -> int:
    n = len(M)
    for m in range(n):
        M[m] = (M[m][0], M[m][1], M[m][0]*M[m][1])
    M = sorted(M, key=lambda x: x[2])
    W = [0 for _ in range(n)]
    for a in range(n):
        for b in range(a+1, n):
            if isin(M[a], M[b]):
                if W[a] + 1> W[b]:
                    W[b] = W[a] + 1
    return max(*W)+1


if __name__ == "__main__":
    M = [(100, 1),
         (1, 100),
         (20, 30),
         (10, 15),
         (40, 1),
         (20, 1)]
    print(lalki(M))
