from zad1testy import runtests


def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                # The value from the left half has been used
                A[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                A[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def chaos_index( T ):
    n = len(T)
    R = [(i, T[i]) for i in range(n)]
    mergeSort(R)
    diff = 0
    for x in range(n):
        adiff = abs(x - R[x][0])
        if adiff > diff:
            diff = adiff
    return diff


runtests( chaos_index )
