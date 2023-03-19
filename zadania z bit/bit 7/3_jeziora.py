"""
Rozwiązanie działa w odbitych względem y = x współrzędnych. xD
Trzeba naprawić, ale ogólnie pomysł działa.
"""

from queue import Queue


def remove_lake(W: list[str], visited: list[list[bool]], x: int, y: int) -> int:
    q = Queue()
    n = len(W)
    size = 1
    q.put((x, y))
    visited[x][y] = True
    while not q.empty():
        field = q.get()
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nextx = field[0] + move[0]
            nexty = field[1] + move[1]
            if -1 < nexty < n and -1 < nextx < n:
                if not visited[nextx][nexty] and W[nextx][nexty] == "W":
                    visited[nextx][nexty] = True
                    size += 1
                    q.put((nextx, nexty))
    return size


def jeziora_1(W: list[str]):
    n = len(W)
    visited = [[False for _ in range(n)] for _ in range(n)]
    lakes = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if W[i][j] == 'W':
                    lakes += 1
                    remove_lake(W, visited, i, j)
                else:
                    visited[i][j] = True
    return lakes


def jeziora_2(W: list[str]):
    n = len(W)
    visited = [[False for _ in range(n)] for _ in range(n)]
    biggest = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if W[i][j] == 'W':
                    w = remove_lake(W, visited, i, j)
                    if w > biggest:
                        biggest = w
                else:
                    visited[i][j] = True
    return biggest


def jeziora_3(W: list[str]):
    n = len(W)
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = Queue()
    n = len(W)
    q.put((0, 0))
    visited[0][0] = True
    while not q.empty():
        field = q.get()
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nextx = field[0] + move[0]
            nexty = field[1] + move[1]
            if -1 < nexty < n and -1 < nextx < n:
                if not visited[nextx][nexty] and W[nextx][nexty] == "L":
                    visited[nextx][nexty] = True
                    q.put((nextx, nexty))
    return visited[n-1][n-1]


def jeziora_4(W: list[str]):
    n = len(W)
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[-1 for _ in range(n)] for _ in range(n)]
    q = Queue()
    n = len(W)
    q.put((0, 0))
    visited[0][0] = True
    while not q.empty():
        field = q.get()
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nextx = field[0] + move[0]
            nexty = field[1] + move[1]
            if -1 < nexty < n and -1 < nextx < n:
                if not visited[nextx][nexty] and W[nextx][nexty] == "L":
                    visited[nextx][nexty] = True
                    parent[nextx][nexty] = field
                    q.put((nextx, nexty))
    last = parent[n-1][n-1]
    while last != -1:
        lx = last[0]
        ly = last[1]
        print(lx, ly)
        last = parent[lx][ly]


if __name__ == "__main__":
    W = ["LWLLLLLL",
         "LWLWWLLL",
         "LLLWWLWL",
         "LWWWWLWL",
         "LLWWLLLL",
         "LWLLLLWW",
         "WWLWWLWL",
         "LLLWLLLL"]
    print("liczba jezior:", jeziora_1(W))
    print("wielkość największego jeziora:", jeziora_2(W))
    print("czy da się dojść do lewego dolnego rogu:", jeziora_3(W))
    print(jeziora_4(W))
