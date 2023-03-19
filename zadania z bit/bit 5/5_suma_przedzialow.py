"""
Dla każdego przedziału szukamy takiego przedziału który znajduje się 'po nim', nie nachodzą na siebie i kończy
się możliwie jak najwcześniej.
"""


def dis(P: tuple[int, int]) -> int:
    return P[1] - P[0]


def suma(P: list[tuple[int, int]], k: int) -> list[int]:
    W = [-1 for _ in range(len(P))]
    for i in range(len(P)):
        p1 = P[i]
        end = 10000
        for j in range(len(P)):
            p2 = P[j]
            if i != j and p2[0] >= p1[1]:
                if p2[1] < end:
                    end = p2[1]
                    W[i] = j
    print(W)
    m = 10000
    mi = -1
    for t in range(len(P)):
        p = P[t]
        start = p[0]
        end = p[1]
        tt = t
        for i in range(k-1):
            if W[tt] == -1:
                end = -1
                break
            tt = W[tt]
            end = P[tt][1]
        if end != -1 and end - start < m:
            m = end - start
            mi = t
    T = []
    for _ in range(k):
        T.append(mi)
        mi = W[mi]
    return T


if __name__ == "__main__":
    P = [(0, 8),
         (8, 10),
         (8, 14),
         (14, 16),
         (14, 19)]
    k = 3
    print(suma(P, k))
