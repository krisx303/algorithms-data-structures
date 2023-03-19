T = [12, 32, 15, 11, 87, 54]


def counting_sort(A, index):
    n = len(A)
    C = [0]*10
    B = [0]*n
    for x in A:
        C[x[index]] += 1
    for i in range(8, -1, -1):
        C[i] = C[i] + C[i+1]
    for i in range(n):
        B[C[A[i][index]]-1] = A[i]
        C[A[i][index]] -= 1
    for i in range(n):
        A[i] = B[i]


for i in range(len(T)):
    T[i] = (T[i]//10, T[i]%10)

counting_sort(T, 0)
print(T)
