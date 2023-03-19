"""
*Problem: 
    Znaleźć nadłuższy spójny podciąg w zadanej tablicy którego elementy sumują się do k.
*Przykład:
    Input: [11, 12, 4, 2, 0, -3, -1, 0, 4], k = 2
    Output:        [4, 2, 0, -3, -1, 0]
*Rozwiązanie:
    Iterujemy po zadanej liście i wykonujemy: (Rozważamy i-ty element)
    1) obliczamy sumę S do i-tego elementu
    2) jeśli liczba S-k pojawiła się już wcześniej jako suma (na pozycji j) to oznacza że elementy t[j:i] sumują się do k
        i zapisujemy początek i koniec podciągu do innej tablicy
    3) w przeciwnym wypadku zapisujemy sumę S do tablicy z sumami
    Na koniec iteracji sprawdzamy który podciąg ze znalezionych jest największy i wybieramy go.
*Złożoności:
    !Obliczeniowa: O(n^2) - w praktyce sporo mniej
    !Pamięciowa: O(n) - tablica sum prefiksowych
https://www.techiedelight.com/find-maximum-length-sub-array-having-given-sum/
"""

t = [11, 12, 4, 2, -2, -3, 2, -1, 0, 4]

k = 2


def findZeroSumSublist(nums):
    values = [0]
    val_len = 0
    total = 0
    found = []
    for i in range(len(nums)):
        total += nums[i]
        j = val_len
        while j > -1:
            if values[j] == total - k:
                found.append((j, i-j+1))
            j -= 1
        else:
            values.append(total)
            val_len += 1
    ml = 0
    mi = 0
    for (start, l) in found:
        if l > ml:
            ml = l
            mi = start
    return t[mi:mi+ml]


print(findZeroSumSublist(t))