"""
Szukanie najkrótszej ścieżki za pomocą zmodyfikowanego algorytmu bfs
Tworzymy graf z krawędziami na zasadach:
1) jeśli pomiędzy wierzchołkami jest odległość <= Z to krawędź pomiędzy ma długość 1.
2) jeśli odległość ta wynosi <= 2*Z to krawędź ma długość 2
Do kolejki wrzucamy wierzchołki ze sztucznymi odległościami.
Wierzchołek został przetworzony gdy wyjmieny go z wartością równą 1.
W przeciwnym wypadku wrzucamy go spowrotem zmiejszając sztuczną odległość o jeden.
"""


from queue import Queue


def bfs(graph, s, e) -> int:
    n = len(graph)
    visited = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    queue = Queue()
    queue.put((s, 0))
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        if u[1] < 2:
            for v, d in graph[u[0]]:
                if not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u[0]] + 1
                    queue.put((v, d))
        else:
            queue.put((u[0], u[1]-1))
            distance[u[0]] += 1
    print(distance)
    return distance[e]


def dist(A: tuple[int, int], B: tuple[int, int]) -> int:
    return (A[0] - B[0])**2 + (A[1] - B[1])**2


def henryk(P: list[tuple[int, int]], Z: int, p0: int, p1: int) -> int:
    Z2 = (2*Z)**2
    Z = Z**2
    v = len(P)
    L = [[] for _ in range(v)]
    for a in range(v):
        for b in range(a+1, v):
            d = dist(P[a], P[b])
            if d <= Z:
                L[a].append((b, 1))
                L[b].append((a, 1))
            elif d <= Z2:
                L[a].append((b, 2))
                L[b].append((a, 2))
    return bfs(L, p0, p1)


if __name__ == "__main__":
    P = [(3, 2),
         (2, 3),
         (2, 5),
         (3, 7),
         (4, 4),
         (5, 3),
         (5, 6),
         (6, 4),
         (8, 4),
         (9, 1)]
    Z = 2
    print(henryk(P, Z, 1, 9))
