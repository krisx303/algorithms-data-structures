"""
Uruchamiamy bfs z dowolnego wierzchołka, znajdujemy najdalej oddalony wierzchołek.
Następnie z niego uruchamiamy następnego bfs, ten wierzchołek z nowo znalezionym jest średnicą grafu.
"""
import queue


def bfs(G: list[list[int]], s: int) -> tuple[int, int]:
    V = len(G)
    visited = [False for _ in range(V)]
    distance = [-1 for _ in range(V)]
    q = queue.Queue()
    q.put(s)
    distance[s] = 0
    visited[s] = True
    while not q.empty():
        v = q.get()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                q.put(u)
    print(distance)
    mx = 0
    mi = s
    for x in range(V):
        if distance[x] > mx:
            mx = distance[x]
            mi = x
    return mi, mx


def srednica(K: list[tuple[int, int]]) -> int:
    V = 0
    for x in K:
        V = max(V, *x)
    V += 1
    G = [[] for _ in range(V)]
    for x in K:
        G[x[0]].append(x[1])
        G[x[1]].append(x[0])
    o = bfs(G, 0)[0]
    return bfs(G, o)[1]


if __name__ == "__main__":
    G = [(3, 1), (5, 4), (6, 4), (4, 1), (1, 0), (0, 2), (2, 7), (7, 9), (7, 8)]
    print(srednica(G))
