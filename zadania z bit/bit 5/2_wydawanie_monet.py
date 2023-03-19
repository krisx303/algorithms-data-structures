"""
Wydajemy największą możliwą monetę dopóki kwota do wydania jest dodatnia.
"""


def monety(M: list[int], c: int):
    m = len(M)-1
    while c > 0:
        if c >= M[m]:
            print(M[m])
            c -= M[m]
        else:
            m -= 1


if __name__ == "__main__":
    M = [1, 2, 5, 10, 20, 50]
    c = 89
    monety(M, c)