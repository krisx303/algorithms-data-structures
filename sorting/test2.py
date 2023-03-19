def partition(A, p, r):
    k = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= k:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickselect(A, p, k, r):
    if p == r:
        return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return quickselect(A, q + 1, k, r)
        else:
            return quickselect(A, p, k, q - 1)


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def insertion_sort(A):
    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while j >= 0 and k < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = k