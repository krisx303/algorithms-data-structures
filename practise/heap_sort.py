"""
Algorytm sortujący za pomocą kopca.
Na początku budujemy kopiec (wystarczy naprawić elementy od 0 do n//2).
Następnie n razy zamieniamy 0 element (największy) z ostatnim z kopca i naprawiamy kopiec rozmiaru o jeden mniejszego.
"""


def heap_sort(A: list[int]):
    n = len(A)
    build_heap(A, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def heapify(A: list[int], n: int, i: int):
    l = 2*i+1
    r = 2*i+2
    max_i = i
    if r < n and A[r] > A[max_i]:
        max_i = r
    if l < n and A[l] > A[max_i]:
        max_i = l
    if max_i != i:
        A[i], A[max_i] = A[max_i], A[i]
        heapify(A, n, max_i)


def build_heap(A: list[int], n: int):
    for i in range(n//2, -1, -1):
        heapify(A, n, i)


if __name__ == "__main__":
    A = [1, 25, 8, 1, 12, 7, 2]
    heap_sort(A)
    print(A)