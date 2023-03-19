def counting_sort(T, k):
    n = len(T)
    C = [0] * k
    B = [0] * n
    for x in T:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[T[i]]-1] = T[i]
        C[T[i]] -= 1
    for i in range(n):
        T[i] = B[i]


ARR = [1, 0, 3, 2, 2, 1, 2, 0]
counting_sort(ARR, 4)
print(ARR)
