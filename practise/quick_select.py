"""
Algorytm wykorzystuje partition z algorytmu quick_sort.
Partition przenosi wszystkie wartości mniejsze od pivota na lewą stronę i zwróć liczbę przeniesionych elementów.
Jeżeli index początku i końca tablicy się zgadzają to wartość pod tym indexem jest szukaną.
W przeciwnym wypadku znajdujemy pivota funkcją partition. W zależności od pivota uruchamiamy rekurencyjnie algorytm.
"""


def quick_select(A: list[int], start: int, last: int, search: int) -> int:
    if start == last:
        return A[start]
    if start < last:
        pivot = partition(A, start, last)
        if pivot == search:
            return A[pivot]
        elif pivot < search:
            return quick_select(A, pivot+1, last, search)
        else:
            return quick_select(A, start, pivot-1, search)


def partition(A: list[int], first: int, last: int) -> int:
    pivot = A[last]
    i = first - 1
    for j in range(first, last):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[last] = A[last], A[i + 1]
