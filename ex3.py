"""
*Problem: 
    Znalezienie wszystkich pod-tablic których elementy sumują się do 0. (patrz zadanie 2).
*Rozwiązanie: 
    Tworzymy listę sum dotychczasowych elementów. Sprawdzamy czy dodanie kolejnego elementu
    nie sprawi, że suma pojawi się powtórnie, jeśli się pojawi to znaczy, że te elementy sumują się do 0.
    Rozważamy tylko pod-tablice ciągłe, czyli o wszystkich elementach sąsiednich.
*Złożoności:
    !Obliczeniowa: O(n^2)
    !Pamięciowa: O(n) - dodatkowa tablica na sumy
https://www.techiedelight.com/find-sub-array-with-0-sum/
"""

t = [4, 2, -3, -1, 0, 4]


def findZeroSumSublist(nums):
    values = [0]
    val_len = 0
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        j = val_len
        while j > -1:
            if values[j] == total:
                print(j, i, t[j:i+1])
            j -= 1
        else:
            values.append(total)
            val_len += 1


print(findZeroSumSublist(t))