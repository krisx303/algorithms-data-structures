# Rozkład jednostajny na przedziale [-2, 3]

T = [-1.8, 1.5, 0.8, -0.1, 2.1]
n = len(T)
buckets = [[] for _ in range(n)]

const = 2
for x in T:
    buckets[int((x+const))].append(x)

print(buckets)
