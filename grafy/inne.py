# --------------------------------------------------------------------------------------------
# *sortowanie topologiczne
# elementu następują tylko po sobie - krawędzie w prawą stronę
# listy zadań do wykonania

# !algorytm:
# uruchomić dfs
# po przetworzeniu wierzchołka dopisać go na początek listy
# --------------------------------------------------------------------------------------------
# * cykl eulera
# cykl przez wszystkie krawędzie dokładnie raz
# każdy wierzchołek ma stopień parzysty

# algorytm:
# wykonujemy dfs nie stosując pola visited ale usuwając odwiedzone krawędzie
# po przetworzeniu wierzchołka dopisujemy go na początek tworzonego cyklu
# przetworzenie - nie ma więcej krawędzi

def printEulersCircuit(G):  # Graf ten jest listą sąsiedztwa i jest nieskierowany
    eulers_path = []

    def dfs(u):
        tmp = G[u].copy()
        for v in tmp:
            if len(G[u]) == 0: break
            G[u].pop(G[u].index(v))  # albo poprostu .pop(0)
            idx = G[v].index(u)
            G[v].pop(idx)
            dfs(v)
        eulers_path.append(u)
        # path.pop()

    dfs(0)
    print(eulers_path)


# G = [[1, 2], [0, 2, 3, 5], [0, 1, 3, 5], [1, 2, 4, 5], [3, 5], [2, 3, 4, 1]]
# printEulersCircuit(G)


# --------------------------------------------------------------------------------------------
# *silnie spójne składowe

# !algorytm:
# wykonanaj dfs na grafie G zapamiętując czasy przetworzenia
# odwróć kierunek wszystkich krawędzi
# wykonaj dfs w kolejności malejących czasów przetworzenia
# --------------------------------------------------------------------------------------------
# *mosty w grafach nieskierowanych
# krawędź której usunięcie rozspujnia graf

# algorytm:
# wykonaj dfs dla każdego wierzchołka v zapamiętując czas odwiedzenia d(v)
# dla każdego wierzchołka oblicz:
# low(v) = min(d(v), min(d(u), min(low(w)))), u - krawędź wsteczna z v do u, w - dziecko v
# mosty to krawędzie {v, p(v)} gdzie d(v) = low(w)

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

# G = [[1, 6], [0, 2], [1, 3, 6], [2, 4, 5], [3, 5], [3, 4], [0, 2, 7], [6]]
# mosty(G)
# --------------------------------------------------------------------------------------------
