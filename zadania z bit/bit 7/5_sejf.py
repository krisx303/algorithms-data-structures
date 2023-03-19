"""

"""
import queue


def sejf(P: list[int], c: int, key: int) -> bool:
    V = [False for _ in range(10000)]
    V[c] = True
    q = queue.Queue()
    q.put(c)
    while not q.empty():
        u = q.get()
        for p in P:
            o = (u+p) % 10000
            if o == key:
                return True
            if not V[o]:
                V[o] = True
                q.put(o)
    return False


if __name__ == "__main__":
    P = [100, 75]
    c = 0000
    key = 150
    print(sejf(P, c, key))
