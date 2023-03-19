from practise.insertion_sort import insertion_sort


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


if __name__ == "__main__":
    A = [1, 4, 3, 5, 6, 0, 2]
    bucket_sort(A)
    print(A)
