"""

"""
import queue


def mapa(G: list[list[tuple[int, int]]], S: list[int]):
    V = len(G)
    visited = [False for _ in range(V)]
    distance = [10**5 for _ in range(V)]
    q = queue.PriorityQueue()
    for s in S:
        q.put((0, s))
        distance[s] = 0
    while not q.empty():
        d, v = q.get()
        if not visited[v]:
            for u, w in G[v]:
                if distance[v] + w < distance[u]:
                    distance[u] = distance[v] + w
                    q.put((distance[u], u))
        visited[v] = True
    print(distance)


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
    S = [1, 10, 4]
    print(mapa(G, S))