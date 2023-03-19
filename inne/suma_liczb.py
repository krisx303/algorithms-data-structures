"""
Sortujemy listę w czasie (nlogn) następnie dla każdego elementu tablicy tworzymy dwa wskaźniki i sprawdzamy czy liczby
pod nimi sumują się do aktualnie sprawdzanego elementu. Jeżeli nie to przesuwamy odpowiednio jeden albo drugi.
Jeśli wskaźniki się miną to oznacza że nie ma takiego rozwiązania.
"""


def quick_sort(A: list[int], start: int, end: int):
    if start < end:
        mid = partition(A, start, end)
        quick_sort(A, start, mid-1)
        quick_sort(A, mid+1, end)


def partition(A: list[int], start: int, end: int) -> int:
    pointer = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < pointer:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1


def check(A: list[int]) -> bool:
    quick_sort(A, 0, len(A)-1)
    print(A)
    for i in range(len(A)):
        x = A[i]
        j = 0
        k = len(A)-1
        while True:
            if j == k:
                return False
            y = A[j] + A[k]
            if y == x:
                break
            if y > x:
                k -= 1
            else:
                j += 1
    return True


if __name__ == "__main__":
    T = [5, -2, 7, -1, 6, 1, 3, -1]
    print(check(T))
