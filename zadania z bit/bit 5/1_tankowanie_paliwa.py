"""
Algorytm Zachłanny.
Jedziemy najdalej jak tylko możemy do momentu aż (ostatnia stacja) + d >= F, gdy odległość pomiedzy stacjami jest większa niż d to -1.
"""


def paliwa(S: list[int], d: int, F: int) -> int:
    last = 0
    j = 0
    jumps = 0
    while True:
        if last + d >= F:
            break
        else:
            if j > len(S) and last + d < F:
                return -1
            if j == len(S) or S[j] > last + d:
                # print("jump to", S[j-1])
                jumps += 1
                last = S[j-1]
        j += 1
    return jumps


if __name__ == "__main__":
    S = [2, 4, 5, 9, 14, 15, 16, 17, 18, 19]
    d = 6
    F = 20
    print(paliwa(S, d, F))
