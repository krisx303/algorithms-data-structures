from queue import PriorityQueue

"""
Lista sąsiedztwa z wagami:
G = [[], [], ...],
G[i] = [(u1, wi), (u2, w2), ...]   <-> i-ty wierzchołek ma krawędź do wierzchołka u1 z wagą w1, ...
"""


def dikstry(G: list[list[tuple[int, int]]], s: int):
    n = len(G)
    distance = [float("inf") for _ in range(n)]  # teblica odległości od {s}
    parent = [-1 for _ in range(n)]  # tablica 'rodziców'
    queue = PriorityQueue()
    queue.put((0, s))
    distance[s] = 0
    parent[s] = s
    visited = [False for _ in range(n)]  # tablica wartości czy dany wierzchołek został już przetworzony
    while not queue.empty():
        value, current = queue.get()  # value not used
        if not visited[current]:
            for v, w in G[current]:
                if distance[current] + w < distance[v]:  # relaxation
                    distance[v] = distance[current] + w
                    parent[v] = current
                    queue.put((distance[v], v))
        visited[current] = True
