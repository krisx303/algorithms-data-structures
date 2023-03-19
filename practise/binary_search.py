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


if __name__ == "__main__":
    A = [1, 2, 5, 7, 7, 7, 8, 9, 12, 16]
    print(binary_search(A, 0, len(A) - 1, 8))
