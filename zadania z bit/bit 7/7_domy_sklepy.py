"""
Mając listę sklepów S i graf G w reprezentacji listowej wykonujemy zmodyfikowany bfs.
Mianowicie na początku do kolejki jako wierzchołek początkowy nie wrzucamy jednego wierzchołka
a wszystkie wierzchołki które są sklepami. Tablica odległości zawiera minimalną odległość od domu do sklepu.
"""

# S - lista indexów sklepów
# G - graf, lista sąsiedstwa
import queue


def mapa(S: list[int], G: list[list[int]]) -> list[int]:
    V = len(G)
    q = queue.Queue()
    visited = [False for _ in range(V)]
    distance = [-1 for _ in range(V)]
    for s in S:
        q.put(s)
        visited[s] = True
        distance[s] = 0
    while not q.empty():
        v = q.get()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                q.put(u)
    return distance


if __name__ == "__main__":
    S = [0, 8]
    G = [[1, 2, 7],
         [0, 8],
         [0, 3],
         [2, 8, 4],
         [3, 5, 6],
         [4, 6],
         [4, 5],
         [0],
         [1, 3, 9],
         [8]]
    print(mapa(S, G))
