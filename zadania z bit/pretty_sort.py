def convert_list(A):
    digits = [0]*10
    for i in range(len(A)):
        x = A[i]
        digits = [0]*10
        while x != 0:
            digits[x % 10] += 1
            x //= 10
        j = 0
        w = 0
        for digit in digits:
            if digit == 1:
                j += 1
            elif digit > 1:
                w += 1
        A[i] = (j, w, A[i])


def sort_w(A):
    n = len(A)
    C = [0]*10
    B = [0]*n
    for x in A:
        C[x[1]] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i-1]
    for i in range(n):
        B[C[A[i][1]]-1] = A[i]
        C[A[i][1]] -= 1
    for i in range(n):
        A[i] = B[n-i-1]


def sort_j(A):
    n = len(A)
    C = [0]*10
    B = [0]*n
    for x in A:
        C[x[0]] += 1
    for i in range(8, -1, -1):
        C[i] = C[i] + C[i+1]
    for i in range(n):
        B[C[A[i][0]]-1] = A[i]
        C[A[i][0]] -= 1
    for i in range(n):
        A[i] = B[i]


def pretty_sort(A):
    sort_w(A)
    print(A)
    sort_j(A)


T = [1266, 123, 455, 67333, 114577, 2344]

convert_list(T)

print(T)

pretty_sort(T)

print(T)



