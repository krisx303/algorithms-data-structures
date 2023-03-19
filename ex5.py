"""
*Problem: 
    W tablicy n elementowej zawierwającej elementy od 1 do n jeden element jest zduplikowany. Należy go znaleźć.
*Rozwiązanie 1): 
    Wykorzystując operację xor na wszystkich elementach tablicy a następnie na wszystkich liczbach od 1 do n
    otrzymujemy zduplikowany element.

*Rozwiązanie 2): 
    Wykorzystując dodatkową tablicę rozmiaru n "zaznaczamy" który element już wystąpił.

!Złożoności 1): obl: O(n) pam:O(1)
!Złożoności 2): obl: O(n) pam:O(n)
https://www.techiedelight.com/find-duplicate-element-limited-range-array/
"""

t = [1, 2, 3, 4, 4]

# rozw 1)
xor = 0
for i in t:
    xor ^= i
for i in range(len(t)):
    xor ^= i
print(xor)


# rozw 2)
d = [False for i in range(len(t))]

for i in t:
    if d[i]:
        print(i)
        break
    else:
        d[i] = True