"""
*Problem: 
    Zamienić zadaną tablicę liczb w tablicę iloczynów takich że:
    Na pozycji i-tej ma być utworzony iloczyn liczb t[0]*t[1]*...*t[i-1]*t[i+1]*...t[n].
*Rozwiązanie:
    Tworzymy dwie tablice left i right zawirające odpowiednio iloczyny liczb po lewej stronie indexu i oraz prawej stronie.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(n)
https://www.techiedelight.com/replace-element-array-product-every-element-without-using-division-operator/
"""

t = [5, 3, 4, 2, 6, 8]

n = len(t)

left = [1]*n
right = [1]*n

for i in range(1, n):
    left[i] *= t[i-1] * left[i-1]
    right[n-i-1] *= t[n-i] * right[n-i] 

for i in range(n):
    t[i] = left[i]*right[i]

print(t)