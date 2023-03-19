R = 5
T = [(0, 0), (3, 3), (1.98, 4.18), (0.54, 0.5), (0.6, 4.44), (-1.56, 4.1), (-3.2, 2.88), (0.64, 2.42), (2.7, 0.94),
     (1.3, 0.96), (3.56, -2.48), (1.42, 3.3)]
n = len(T)
for i in range(n):
    T[i] = (T[i], T[i][0] ** 2 + T[i][1] ** 2)

buckets = [[] for _ in range(n)]
ranges = [0.0] * n
nr = R * R / n
for i in range(n):
    ranges[i] = nr
    nr = R * R / n + nr
for x in T:
    for r in range(n):
        if ranges[r] > x[1]:
            buckets[r].append(x)
            break

for x in range(n):
    print(ranges[x], buckets[x])