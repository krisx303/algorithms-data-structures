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


t = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]

max_start = 0
max_len = 0
start = 0
l = 1
inc = True
for i in range(1, len(t)):
    if inc:
        if 