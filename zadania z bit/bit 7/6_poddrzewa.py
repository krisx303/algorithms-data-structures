"""
NIE DZIAŁA
"""


def poddrzewa(G: list[tuple[int, int]]) -> list[int]:
    V = 0
    for x in G:
        V = max(V, *x)
    V += 1
    G = sorted(G, key=lambda x: x[0])
    W = [0 for _ in range(V)]
    print(G)


if __name__ == "__main__":
    G = [(3, 1), (5, 4), (6, 4), (4, 1), (1, 0), (0, 2), (2, 7), (7, 9), (7, 8)]
    print(poddrzewa(G))
