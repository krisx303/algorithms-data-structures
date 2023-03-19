"""
Wykonanie pojedyńczego bfs na grafie stworzonym z podanych par.
Dystans w którym dojdziemy do wierzchołka i jest jednocześnie dniem w którym i-ta osoba dostanie wiadomość.
Zatem wystarczy zliczyć najczęściej występującą odległość od 0.
*W tej implementacji liczebność odległości jest liczona na bieżąco i aktualizowana,
wynika to z charakterystyki działania algorytmu bfs - rozchodzi się falami, a każda fala to nowa odległość
zatem wystarczy policzyć ilość wierzchołków pomiędzy zmianą odległości.
"""
import queue


def wiadomosc(P: list[tuple[int, int]]) -> int:
    V = 0
    for x in P:
        V = max(V, *x)
    V += 1
    G = [[] for _ in range(V)]
    for x in P:
        G[x[0]].append(x[1])
        G[x[1]].append(x[0])
    q = queue.Queue()
    q.put(0)
    distance = [-1 for _ in range(V)]
    visited = [False for _ in range(V)]
    visited[0] = True
    distance[0] = 0
    lastD = -1
    counter = 1
    maxCounter = 1
    maxDay = 0
    while not q.empty():
        v = q.get()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                if lastD != distance[u]:
                    if counter > maxCounter:
                        maxCounter = counter
                        maxDay = lastD
                    counter = 1
                    lastD = distance[u]
                else:
                    counter += 1
                    if counter > maxCounter:
                        maxCounter = counter
                        maxDay = lastD
                q.put(u)
    print(distance)
    return maxDay


if __name__ == "__main__":
    P = [(0, 1), (1, 2), (1, 4), (2, 3), (3, 4), (3, 7), (3, 6), (4, 5), (5, 7), (5, 6), (6, 8),
         (8, 10), (8, 9), (9, 10), (3, 11)]
    print(wiadomosc(P))
