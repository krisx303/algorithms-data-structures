"""

"""


def mosty(G):
    n = len(G)
    visited = [False] * n
    low = [-1] * n
    d = [-1] * n
    time = 0

    def dfs(G, v, p=-1):
        nonlocal time
        visited[v] = True
        time = time + 1
        d[v] = time
        low[v] = time
        for j in G[v]:
            if j == p:
                continue
            if visited[j]:
                low[v] = min(low[v], d[j])
            else:
                dfs(G, j, v)
                low[v] = min(low[v], low[j])
                if low[j] > d[v]:
                    print(v, j)

    for i in range(n):
        if not visited[i]:
            dfs(G, i)


def trolle():
    pass


if __name__ == "__main__":
    pass
