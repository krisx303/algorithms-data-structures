"""
Działa
"""


def binsearch(K: list[tuple[int, int]], p: int) -> int:
    s = 0
    e = len(K) - 1
    m = 0
    while s <= e:
        m = (e + s) // 2
        if K[m][0] < p:
            s = m + 1
        elif K[m][0] > p:
            e = m - 1
        else:
            return m
    return -1


def findPlatform(K: list[tuple[int, int]], O: list[bool], start: int) -> tuple[int, int]:
    first = -1
    for i in range(len(K)):
        if K[i][0] < start:
            continue
        if O[i]:
            first = i
            O[i] = False
            break
    if first == -1:
        return -1, -1
    next = first
    start = K[first][0]
    end = K[first][1]
    while True:
        next = binsearch(K, K[next][1])
        if next == -1:
            break
        else:
            end = K[next][1]
            O[next] = False
    return start, end


def pin(A: tuple[int, int], B: tuple[int, int]) -> bool:
    return A[0] <= B[0] and A[1] >= B[1]


def klocki(K: list[tuple[int, int]]) -> list[int]:
    n = len(K)
    K = sorted(K, key=lambda x: x[0])
    O = [True for _ in range(n)]
    levels = []
    level = []
    start = 0
    while True:
        f = findPlatform(K, O, start)
        if f[0] != -1:
            start = f[1]
            level.append(f)
        else:
            if len(level) == 0:
                break
            levels.append(level)
            level = []
            start = 0
    print(levels)
    for i in range(1, len(levels)):
        for r in levels[i]:
            flag = False
            for p in levels[i-1]:
                if pin(p, r):
                    flag = True
            if not flag:
                return []
    return [1]


if __name__ == "__main__":
    # K = [(2, 4),
    #      (5, 7),
    #      (3, 6),
    #      (4, 5),
    #      (9, 11),
    #      (11, 14),
    #      (10, 13),
    #      (6, 8)]
    K = [(2, 7),
         (3, 6),
         (4, 5),
         (6, 8),
         (9, 14),
         (10, 13)]
    print(klocki(K))
