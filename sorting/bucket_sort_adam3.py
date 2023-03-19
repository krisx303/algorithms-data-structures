def insertion_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b

# Zares [-1; 1]


def bucket_sort(x):
    print(x)
    ranges = len(x)
    buckets = [[] for _ in range(ranges)]

    # przedział [-1;1] jest długości 2, można by też szukać min i max
    r = 2/ranges
    for j in x:
        index_b = int((j - (-1))/r)  # -1 ponieważ to najmniejsza możliwa wartość
        buckets[index_b].append(j)

    for i in range(ranges):
        insertion_sort(buckets[i])

    print("buckets", buckets)
    k = 0
    for i in range(ranges):
        for j in range(len(buckets[i])):
            x[k] = buckets[i][j]
            k += 1
    return x


T = [-0.897, -0.895, -0.18, 0.685, -0.3434, 0.15]
print(bucket_sort(T))