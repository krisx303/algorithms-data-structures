

# spójność grafu
# dwudzielność
# wykrywanie cykli
# sortowanie topologiczne
# cykl Eulera
# silnie spójne składowe
# mosty / pkt artukulacji
# macierz - O(V^2)
# listy - O(V + E)

def dfs(G):
    n = len(G)
    visited = [False] * n
    parent = [None] * n

    def dfsVisit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfsVisit(G, v)

    for u in range(len(G)):
        if not visited[u]:
            dfsVisit(G, u)
