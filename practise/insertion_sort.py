"""
Dla każdego elementu znajdź dla niego miejsce na poprzednich miejscach przestawiając kolejne elementy w którąś ze stron.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    A = [1, 25, 8, 1, 12, 7, 2]
    insertion_sort(A)
    print(A)