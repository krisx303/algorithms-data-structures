"""

"""


def counting_sort(A: list[int], k: int):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


if __name__ == "__main__":
    A = [1, 2, 3, 0, 1, 4, 2, 3, 4, 0, 4, 2, 2, 1, 1]
    counting_sort(A, 5)
    print(A)