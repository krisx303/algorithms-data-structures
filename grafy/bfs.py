from queue import PriorityQueue

# najkrótsze ścieżki (bez wag)
# spójność grafu
# wykrywanie cukli
# dwudzielność
# macierz - O(V^2)
# listy - O(V + E)


def bfs(graph, s):
    n = len(graph)
    visited = [False] * n
    distance = [0] * n
    parent = [None] * n
    queue = PriorityQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for v, val in enumerate(graph[u]):
            if visited[v] is False:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.put(v)

