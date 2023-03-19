

def quickselect(A: list[int], k: int) -> int:
    """
    Funckja znajdująca element który znajdzie się na pozycji k po posortowaniu tablicy A.
    Złożoność obliczeniowa to O(n).
    Złożoność pamięciowa to O(1)
    """
    return select(A, 0, k, len(A)-1)


def select(A, p, k, r):
    if p == r:
        return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, q+1, k, r)
        else:
            return select(A, p, k, q-1)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    T = [5, 1, 2, 3, 4]

    print(select(T, 0, 2, 4))