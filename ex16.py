"""
*Problem: 
    Znaleźć w tablicy index równowagi j - suma elementów po lewej stronie j jest równa sumie po prawej stronie j.
*Rozwiązanie:
    Obliczamy sumę wszystkich elementów zadanej tablicy.
    Iterujac po kolejnych wartościach w tablicy. Sprawdzamy czy nie zachodzi warunek:
    2*(suma dotychczas napotkanych elementów) = suma - (aktualna wartość)
    jeśli zachodzi to i jest indexem równowagi.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/find-equilibrium-index-array/
"""

def findIndexes(A):
    s = 0
    for i in A:
        s += i
    
    left = 0
    for i in range(len(A)):
        if 2*(left) == s - A[i]:
            print(i)
        left += A[i]

A = [0, -3, 5, -4, -2, 3, 1, 0]
findIndexes(A)