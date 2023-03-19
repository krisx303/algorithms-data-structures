"""
Dopóki wskaźnik początku sortowanej tablicy jest przed wskaźnikiem końca to wykonuj algorytm.
Wyznacz index pivota wykomując partition i wykonaj się rekurencyjnie dla dwóch części tablicy.
Partition przenosi wszystkie wartości mniejsze od pivota na lewą stronę i zwróć liczbę przeniesionych elementów.
"""


def quick_sort(A: list[int], s: int, e: int):
    if s < e:
        p = partition(A, s, e)
        quick_sort(A, s, p - 1)
        quick_sort(A, p + 1, e)


def partition(A: list[int], first: int, last: int) -> int:
    pivot = A[last]
    i = first - 1
    for j in range(first, last):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[last] = A[last], A[i+1]
    return i + 1


if __name__ == "__main__":
    A = [1, 25, 8, 1, 12, 7, 2]
    quick_sort(A, 0, len(A)-1)
    print(A)