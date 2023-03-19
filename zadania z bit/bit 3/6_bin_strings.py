"""
f(i) - liczba binarnych stringów o długości i bez jedynek obok siebie

f(i) = f(i-1) + f(i-2)

Złożoność obliczeniowa: O(n)
Złożoność pamięciowa: O(n)
"""


def strings(n: int) -> int:
    F = [0 for _ in range(n+1)]
    F[1] = 2
    F[2] = 3

    def f(i: int) -> int:
        if F[i] != 0:
            return F[i]
        F[i] = f(i - 1) + f(i - 2)
        return F[i]
    return f(n)


if __name__ == "__main__":
    print(strings(4))
