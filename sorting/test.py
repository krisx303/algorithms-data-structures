def quickselect(A, p, k, r):
    if p == r:
        return A[p]
    elif p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return quickselect(A, q + 1, k, r)
        else:
            return quickselect(A, p, k, q - 1)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def insertion_sort(A):
    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while j >= 0 and k < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = k


def counting_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for x in A:
        B[C[x] - 1] = x
        C[x] -= 1
    for i in range(n):
        A[i] = B[i]


def heapify(A, n, i):
    l = 2*i+1
    r = 2*i+2
    max_i = i
    if r < n and A[r] > A[max_i]:
        max_i = r
    if l < n and A[l] > A[max_i]:
        max_i = l
    if max_i != i:
        A[max_i], A[i] = A[i], A[max_i]
        heapify(A, n, max_i)


def build_heap(A, n):
    for i in range(n // 2, -1, -1):
        heapify(A, n, i)


def heap_sort(A):
    n = len(A)
    build_heap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def bucket_sort(A):
    n = len(A)
    min_v = 0
    max_v = A[0]
    for x in A:
        if x > max_v:
            max_v = x
        elif x < min_v:
            min_v = x
    range_v = max_v - min_v
    r = range_v/n
    buckets = [[] for _ in range(n)]
    for x in A:
        index = int((x - min_v) / r)
        if index == n:
            index -= 1
        buckets[index].append(x)

    for bucket in buckets:
        if len(bucket) > 1:
            insertion_sort(bucket)

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            A[k] = buckets[i][j]
            k += 1


def merge_sort(A):
    n = len(A)
    if n > 1:
        mid = n//2
        left_part = A[:mid]
        right_part = A[mid:]
        merge_sort(left_part)
        merge_sort(right_part)
        l = 0
        r = 0
        m = 0
        while l < len(left_part) and r < len(right_part):
            if left_part[l] <= right_part[r]:
                A[m] = left_part[l]
                l += 1
            else:
                A[m] = right_part[r]
                r += 1
            m += 1

        while l < len(left_part):
            A[m] = left_part[l]
            l += 1
            m += 1
        while r < len(right_part):
            A[m] = right_part[r]
            r += 1
            m += 1


def binary_search(A, p, r, x):
    if r >= p:
        mid = (p + r)//2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binary_search(A, p, mid - 1, x)
        else:
            return binary_search(A, mid + 1, r, x)
    else:
        return -1


T = [1, 4, 2, 3]
merge_sort(T)
print(T)