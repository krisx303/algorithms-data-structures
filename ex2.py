"""
*Problem: 
    Określenie czy tablica zawiera pod-tablicę której elementy sumują się do 0.
*Rozwiązanie: 
    Tworzymy listę sum dotychczasowych elementów. Sprawdzamy czy dodanie kolejnego elementu
    nie sprawi, że suma pojawi się powtórnie, jeśli się pojawi to znaczy, że te elementy sumują się do 0.
    Rozważamy tylko pod-tablice ciągłe, czyli o wszystkich elementach sąsiednich.
*Przykład:
    Np dana jest tablica [1, 1, 1, 1, -2]
    kolejne sumy to: 0, 1, 2, 3, 4, 2.
    Ponieważ 2 pojawia się po raz drugi to oznacza że elementy t[2], t[3], t[4] mają sumę 0.
    Analogicznie [4, 3, 5, 2, 1, -5, 2] -> 0, 4, 7, 12, 14, 15, 10, 12 (12 się powtarza) zatem t[3]+t[4]+t[5]+t[6]=0
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(n) - dodatkowa tablica na sumy
http://www.techiedelight.com/check-subarray-with-0-sum-exists-not/
"""

t = [1, 1, 1, -2]


def hasZeroSumSublist(nums):
    values = [0]
    val_len = 0
    total = 0
    for i in nums:
        total += i
        j = val_len
        while j > -1 and values[j] >= total:
            if values[j] == total:
                return True
            j -= 1
        else:
            values.append(total)
            val_len += 1
    return False


print(hasZeroSumSublist(t))