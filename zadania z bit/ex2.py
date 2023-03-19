"""
Sortujemy najpierw po długości słów counting sortem zliczając ile jest słów danej długości a następnie sortujemy
od końca listy słowa o długości [i, max_i] gdzie max_i to największa długość słowa
"""

ARR = ["aab", "bca", "cge", "a", "bac", "ca", "aaaac", "aaaad", "c", "ac", "aac"]

max_len = 0
n = len(ARR)
for i in range(n):
    l = len(ARR[i])
    if l > max_len:
        max_len = l
    ARR[i] = (ARR[i], l)

# Counting sort po długości
C = [0]*max_len
B = [None] * n

for x in ARR:
    C[x[1]-1] += 1

for i in range(1, max_len):
    C[i] = C[i] + C[i-1]

lengths = [0, *C]

for x in ARR:
    B[C[x[1]-1]-1] = x[0]
    C[x[1]-1] -= 1

ARR = B
print(ARR)
print(lengths)
for i in range(max_len, 0, -1):
    # Sortowanie słów na indexach lenghts[i-1] do n (po i-tej literze)
    # Pominięcie przypadków gdzie nie dochodzą do sortowania żadne słowa
    if lengths[i-1] == lengths[i]:
        continue
    print(lengths[i-1], i)
    print(ARR[lengths[i-1]:n])
    # Counting sort po i-tej literze
    C = [0]*26
    B = [0]*(n-lengths[i-1])
    for x in range(n-1, lengths[i-1]-1, -1):
        C[ord(ARR[x][i-1])-97] += 1
    for x in range(1, 26):
        C[x] = C[x] + C[x-1]
    for x in range(n-1, lengths[i-1]-1, -1):
        B[C[ord(ARR[x][i-1])-97]-1] = ARR[x]
        C[ord(ARR[x][i - 1]) - 97] -= 1
    print(B)
    ARR = ARR[:lengths[i-1]] + B
print(ARR)
# "ca"
# "bc"
# "aa"
# "aab"
# "bba"
#
# [3, 1, 1] -> [3, 4, 5]
#
# "ca"
# "aa"
# "aab"
# "bba"
# "bc"
#
# [2, 2, 1] -> [2, 4, 5]
#
# "aa"
# "aab"
# "bba"
# "bc"
# "ca"
