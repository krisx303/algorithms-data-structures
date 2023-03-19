def heapify(T, n, i):
    l = 2*i+1
    r = 2*i+2
    max_i = i
    if r < n and T[r] > T[max_i]:
        max_i = r
    if l < n and T[l] > T[max_i]:
        max_i = l
    if max_i != i:
        T[i], T[max_i] = T[max_i], T[i]
        heapify(T, n, max_i)


def build_heap(T, n):
    for i in range(n//2, -1, -1):
        heapify(T, n, i)


ARR = [5, 2, 6, 8, 19, 23]
n = len(ARR)
build_heap(ARR, n)
for i in range(n-1, 0, -1):
    ARR[0], ARR[i] = ARR[i], ARR[0]
    heapify(ARR, i, 0)
print(ARR)