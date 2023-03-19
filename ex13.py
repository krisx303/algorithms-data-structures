"""
*Problem: 
    Znaleźć w tablicy dwie wartości które dają największy możliwy iloczyn.
*Rozwiązanie:
    Szukamy w tablicy minimum, drugiego minimum, maximum oraz drugiego maximum.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/find-maximum-product-two-integers-array/
"""

T = [-10, -3, 5, 6, -2]

min_1, min_2 = 10000, 10000
max_1, max_2 = 0, 0

for i in range(len(T)):
    if T[i] > max_1:
        max_2 = max_1
        max_1 = T[i]
    elif T[i] > max_2:
        max_2 = T[i]
    
    if T[i] < min_1:
        min_2 = min_1
        min_1 = T[i]
    elif T[i] < min_2:
        min_2 = T[i]

if min_1 * min_2 > max_1 * max_2:
    print(min_1, min_2)
else:
    print(max_1, max_2)