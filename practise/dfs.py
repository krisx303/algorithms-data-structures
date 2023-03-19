

def dfs(G: list[list[int]], start: int):
    n = len(G)
    visited = [False] * n
    parent = [None] * n

    def dfsVisit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfsVisit(G, v)

    dfsVisit(G, start)
    # for u in range(len(G)):
    #     if not visited[u]:
    #         dfsVisit(G, u)

