"""
*Problem: 
    Stwórz permutację danej tablicy T.
*Złożoności:
    !Obliczeniowa: O(n)
    !Pamięciowa: O(1)
https://www.techiedelight.com/shuffle-given-array-elements-fisher-yates-shuffle/
"""


from random import randrange

def shuffle(A):
    for i in reversed(range(1, len(A))):
        j = randrange(i + 1)
        A[i], A[j] = A[j], A[i]
 

T = [1, 2, 3, 4, 5, 6]

shuffle(T)
print(T)
 