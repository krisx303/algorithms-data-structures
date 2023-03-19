"""
Zmodyfikowana dijkstra. Relaksujemy najpierw po długości a następnie (jeżeli porównywane długości są sobie równe)
relaksujemy po ilości krawędzi do tego wierzchołka od wierzchołka s.
"""

import queue


def sciezki(G: list[list[tuple[int, int]]], s: int, e: int) -> list[int]:
    V = len(G)
    q = queue.PriorityQueue()
    visited = [False for _ in range(V)]
    parent = [-1 for _ in range(V)]
    distance = [10**5 for _ in range(V)]
    edges = [-1 for _ in range(V)]
    q.put((0, s))
    distance[s] = 0
    edges[s] = 0
    while not q.empty():
        value, current = q.get()  # value is not used
        if not visited[current]:
            for v, w in G[current]:
                if distance[current] + w < distance[v]:  # relaxation
                    distance[v] = distance[current] + w
                    edges[v] = edges[current] + 1
                    parent[v] = current
                    q.put((distance[v], v))
                elif distance[current] + w == distance[v]:
                    if edges[current] + 1 < edges[v]:
                        edges[v] = edges[current] + 1
                        parent[v] = current
        visited[current] = True
    print(distance)
    print(edges)


if __name__ == "__main__":
    G = [[(1, 6), (9, 1), (2, 4), (5, 2)],
         [(7, 5), (0, 6), (8, 3)],
         [(0, 4), (3, 5)],
         [(2, 5), (4, 4), (5, 12)],
         [(3, 4), (6, 4), (5, 7)],
         [(0, 2), (3, 12), (6, 3), (4, 7)],
         [(5, 3), (4, 4)],
         [(8, 3), (1, 5)],
         [(7, 3), (10, 2), (1, 3)],
         [(10, 2), (0, 1)],
         [(8, 2), (9, 2)]]
    print(sciezki(G, 0, 8))
