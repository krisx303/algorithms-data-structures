"""
Wykonujemy dijkstrę na drzewie rozpinającym (daje to nam w efekcie wszystkie odległości do wierzchołków od punktu 0
poruszając się jedynie po drzewie rozpinającym).
Następnie wykonujemy ponowinie dijkstrę, tym razem na całym grafie.
Podczas relaksacji, jeżeli odległość do jakiegoś wierzchołka jest mniejsza niż odległość z drzewa T to znaczy że nie
jest to drzewo najkrótszych ścieżek.
"""


from queue import PriorityQueue, Queue


def drzewo(G, T):
    n = len(G)
    distance = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = Queue()
    queue.put(0)
    distance[0] = 0
    visited[0] = True
    while not queue.empty():
        v = queue.get()
        for u, d in T[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + d
                queue.put(u)
    # tablica distances zawiera odległości od punktu 0 poruszając się tylko krawędziami z drzewa rozpinającego
    dist = [10**5 for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()
    queue.put((0, 0))
    dist[0] = 0
    while not queue.empty():
        v = queue.get()[1]
        if not visited[v]:
            for u, w in G[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    if dist[u] < distance[u]:
                        return False
                    queue.put((dist[u], u))
        visited[v] = True
    return True


if __name__ == "__main__":
    G = [[(1, 3), (3, 4), (2, 1)],
         [(0, 3), (4, 8)],
         [(0, 1), (3, 2), (5, 5)],
         [(0, 4), (4, 7), (5, 1), (2, 2)],
         [(1, 8), (3, 7)],
         [(3, 1), (2, 5)]]

    T = [[(1, 3), (3, 4), (2, 1)],
         [(0, 3)],
         [(0, 1)],
         [(0, 4), (4, 7), (5, 1)],
         [(3, 7)],
         [(3, 1)]]

    print(drzewo(G, T))

    T = [[(1, 3), (2, 1)],
         [(0, 3)],
         [(0, 1), (3, 2)],
         [(4, 7), (5, 1), (2, 2)],
         [(3, 7)],
         [(3, 1)]]

    print(drzewo(G, T))