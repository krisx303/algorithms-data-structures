"""
Algorytm dijkstry
"""

from queue import PriorityQueue as Queue


def windy(G: list[list[tuple[int, int]]], i: int, j: int):
    q = Queue()
    n = len(G)
    distance = [float("inf") for _ in range(n)]  # teblica odległości od {s}
    parent = [-1 for _ in range(n)]  # tablica 'rodziców'
    q.put((0, i))
    distance[i] = 0
    visited = [False for _ in range(n)]  # tablica wartości czy dany wierzchołek został już przetworzony
    while not q.empty():
        value, current = q.get()  # value is not used
        if not visited[current]:
            for v, w in G[current]:
                if distance[current] + w < distance[v]:  # relaxation
                    distance[v] = distance[current] + w
                    parent[v] = current
                    q.put((distance[v], v))
        visited[current] = True
    p = j
    print(distance[j])
    while p != -1:
        print(p, distance[p])
        p = parent[p]


if __name__ == "__main__":
    G = [[] for _ in range(5)]

    G[0] = [(1, 20)]
    G[1] = [(2, 5), (4, 60)]
    G[2] = [(1, 5), (3, 5), (3, 1)]
    G[3] = [(2, 1), (2, 5), (4, 5)]
    G[4] = [(3, 5), (1, 60)]

    windy(G, 0, 4)
