"""
Reprezętacja macierzowa grafu.
G[i][j] = 7 <-> pomiędzy wierzchołkami i oraz j jest krawędź o wadze 7.
"""


def kruskal(G):
    n = len(G)
    E = []
    for i in range(n):
        for j in range(i+1, n):
            if G[i][j] != float("inf"):  # lub np MAX = 10 ** 10
                E.append((G[i][j], i, j))

    E = sorted(E)
    S = [make_set(i) for i in range(n)]
    T = []
    for _, p, q in E:
        if find_set(S[p]) != find_set(S[q]):
            T.append((p, q))
            union_sets(S[p], S[q])


def make_set(x: int):
    """Funkcja tworząca zbiór jednostkowy z elementem {x}"""
    pass


def find_set(x):
    """Zwraca reprezentanta zbioru do którego należy x"""
    pass


def union_sets(x, y):
    """Łączy zbiory x oraz y w jeden zbiór"""
    pass
