T = [-2, 2, 1, 0, -1]
n = len(T)
buckets = [[] for _ in range(n)]

min_v = 0
max_v = T[0]

for x in T:
    if x < min_v:
        min_v = x
    elif x > max_v:
        max_v = x

const = -min_v
r = (max_v - min_v + 1)/n
for x in T:
    buckets[int((x+const)/r)].append(x)

print(buckets)
