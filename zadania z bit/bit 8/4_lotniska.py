"""
Znajdujemy Minimalne Drzewo Rozpinające (MST), ale bierzemy tylko krawędzie które mają mniejszy koszt niż K. Ponieważ
jeżeli koszt budowy drogi z tego miasta będzie większy bądź równy budowie lotniska to bardziej opłaca się budować lotnisko.
"""


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def make_set(x: int):
    return Node(x)


def find_set(x):
    if x.parent != x:
        x.parent = find_set(x.parent)
    return x.parent


def union_sets(x: Node, y: Node):
    x = find_set(x)
    y = find_set(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def lotniska(G: list[list[int]], k: int) -> int:
    n = len(G)
    E = []
    for a in range(n):
        for b, d in G[a]:
            E.append((d, a, b))
    E = sorted(E)
    S = [make_set(i) for i in range(n)]
    T = []
    for d, p, q in E:
        if d >= k:
            break
        if find_set(S[p]) != find_set(S[q]):
            T.append((p, q))
            union_sets(S[p], S[q])
    cost = 0
    for e in T:
        cost += e[1]
    U = [find_set(s).value for s in S]
    cost += len(set(U))*k
    return cost


if __name__ == "__main__":
    G = [[(6, 2), (5, 3), (3, 29)],
         [(4, 6), (3, 8), (8, 35)],
         [(5, 30), (4, 15), (3, 7), (10, 50)],
         [(0, 29), (1, 8), (2, 7), (4, 12)],
         [(2, 15), (3, 12), (1, 6)],
         [(0, 3), (6, 6), (2, 30)],
         [(5, 6), (0, 2)],
         [(9, 3), (8, 2)],
         [(1, 35), (7, 2), (9, 4), (11, 6)],
         [(7, 3), (8, 4), (10, 3)],
         [(2, 50), (9, 3), (11, 5)],
         [(8, 6), (10, 5)]]
    k = 10
    print(lotniska(G, k))
