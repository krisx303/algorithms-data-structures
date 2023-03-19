from queue import PriorityQueue


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = PriorityQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] is False) and (val > 0):
                queue.put(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = 10**6
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow
