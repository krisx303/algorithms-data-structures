"""
Uruchamiamy pojedyńczego bfs/dfs i jeżeli natrafimy na wierzchołek już odwiedzony to znaleźliśmy cykl.
Reprezentacja listowa.
"""

from queue import Queue


def has_cycle(G: list[list[int]]) -> bool:
    q = Queue()
    V = len(G)
    visited = [False for _ in range(V)]
    parent = [-1 for _ in range(V)]
    visited[0] = True
    q.put(0)
    while not q.empty():
        v = q.get()
        for u in G[v]:
            if visited[u] and parent[v] != u:
                return True
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                q.put(u)
    return False
        

if __name__ == "__main__":
    G = [[1],
         [0, 2, 4],
         [1, 3],
         [2, 4],
         [1, 5, 3],
         [4]]
    print(has_cycle(G))
