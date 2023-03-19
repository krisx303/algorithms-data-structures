from queue import PriorityQueue

"""
Tworzymy kolejkę priorytetową.
Na początku wrzucamy do niej krotki (zysk, wkład) które mają mniejszy wkład niż W.
Następnie k razy wyciągamy z niej element o największym zysku, a następnie dorzucamy 'odblokowane' zlecenia 
(te które teraz mają mniejszy wkład niż aktualne W).
"""


def zlecenia(P: list[int], C: list[int], W: int, k: int) -> int:
    q = PriorityQueue()
    n = len(P)
    R = [(-P[i], C[i]) for i in range(n)]
    R = sorted(R, key=lambda x: x[1])
    p = 0
    while p < n and R[p][1] <= W:
        q.put(R[p])
        p += 1
    for t in range(k):
        u = q.get()
        W += -u[0]
        while p < n and R[p][1] <= W:
            q.put(R[p])
            p += 1
    return W


if __name__ == "__main__":
    W = 0
    k = 2
    P = [1, 2, 3]
    C = [0, 1, 1]
    print(zlecenia(P, C, W, k))
