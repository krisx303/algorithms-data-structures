from queue import PriorityQueue

"""
Lista sąsiedztwa z wagami:
G = [[], [], ...],
G[i] = [(u1, wi), (u2, w2), ...]   <-> i-ty wierzchołek ma krawędź do wierzchołka u1 z wagą w1, ...
"""


def dikstry(G: list[list[tuple[int, int]]], s: int):
    n = len(G)
    D = [10 ** 10 for _ in range(n)]  # teblica odległości od {s}
    P = [10 ** 10 for _ in range(n)]  # tablica 'rodziców'
    queue = PriorityQueue()
    queue.put((0, s))
    D[s] = 0
    P[s] = s
    V = [False for _ in range(n)]  # tablica wartości czy dany wierzchołek został już przetworzony
    while True:
        _, current = queue.get()
        while not queue.empty() and V[current]:
            _, current = queue.get()
        if V[current]:
            break

        for v, w in G[current]:
            if D[current] + w < D[v]:
                D[v] = D[current] + w
                P[v] = current
                queue.put((D[v], v))

        V[current] = True
