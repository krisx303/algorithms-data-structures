from queue import Queue


def bfs(G: list[list[int]], start: int):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    q = Queue()
    q.put(start)
    distance[start] = 0
    visited[start] = True
    while not q.empty():
        v = q.get()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                distance[u] = distance[v] + 1
                q.put(u)
