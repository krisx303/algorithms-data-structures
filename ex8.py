"""
*Problem: 
    Znaleźć nadłuższy spójny podciąg w zadanej tablicy który zawiera tyle samo jedynek co zer. (Tablica składa się tylko z zer i jedynek)
*Przykład:
    Input: [0, 0, 1, 0, 1, 0, 0]
    Output:   [0, 1, 0, 1]
*Rozwiązanie:
    Tworzymy dwie tablice w których zapisujemy na indeksie i-tym liczbę zer/jedynek do i-tego elementu.
    Następnie rozważając tylko podciągi o parzystej długości (rozpoczynając od najdłuższych) sprawdzamy czy 
    liczba jedynek jest równa liczbie zer w tym podciągu za pomocą obliczonych tablic.
*Złożoności:
    !Obliczeniowa: O(n^2) - w praktyce sporo mniej
    !Pamięciowa: O(n) - tablica sum prefiksowych
https://www.techiedelight.com/find-maximum-length-sub-array-equal-number-0s-1s/
"""

t = [0, 0, 1, 0, 1, 0, 0]


def findLongestSubArray(T):
    n = len(T)
    c0 = [0 for _ in range(n+1)]
    c1 = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        c0[i] = c0[i-1] + (t[i-1] == 0)
        c1[i] = c1[i-1] + (t[i-1] == 1)

    for i in range((n//2)*2, 0, -2):
        for j in range(n-i+1):
            if (c0[j+i] - c0[j]) == (c1[j+i] - c1[j]):
                return (j, j+i)

res = findLongestSubArray(t)
print(t[res[0]:res[1]])