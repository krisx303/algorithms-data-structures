"""
f(i) - czy jesteśmy w stanie zapakować bagaże o wadze i
"""


def pakowanie(P: list[int], W: int):
    F = [None for i in range(W + 1)]
    F[0] = True

    def f(i: int) -> bool:
        if i < 0:
            return False
        if F[i] is not None:
            return F[i]
        flag = False
        for x in P:
            if f(i - x):
                flag = True
        F[i] = flag
        return F[i]
    if sum(P) % 2 == 1:
        return False
    return f(W//2)


if __name__ == "__main__":
    P = [4, 4, 4]
    print(pakowanie(P, sum(P)))
