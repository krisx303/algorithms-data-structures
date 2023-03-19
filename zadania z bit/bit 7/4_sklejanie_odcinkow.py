"""
Tworzymy graf skierowany którego wierzchołkami są punkty na osi liczbowej, a krawędź od a do b istnieje tylko wtedy
gdy w zbiorze odcinków jest odcinek [a, b] (krawędź tylko w jedną stronę).
Następnie po takim grafie jedno wywołanie algorytmu bfs z wierzchołka a rozwiązuje zadanie
(Jeżeli wierzchołek b został odwiedzony to da się dobrać takie przedziały).
"""
import queue


def sklej(O: list[tuple[int, int]], a: int, b: int) -> bool:
    V = 0
    for x in O:
        V = max(V, *x)
    V += 1
    G = [[] for _ in range(V)]
    for o in O:
        G[o[0]].append(o[1])
    visited = [False for _ in range(V)]
    q = queue.Queue()
    q.put(a)
    visited[a] = True
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
    return visited[b]


if __name__ == "__main__":
    O = [(0, 2),
         (1, 3),
         (0, 3),
         (2, 4),
         (3, 5)]
    a = 0
    b = 5
    print(sklej(O, a, b))
