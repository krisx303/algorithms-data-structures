"""
Tak jak mówił Igor robimy tablicę liczników wielkości 26. Oraz wskaźniki na początki tablicy słowa 1 i słowa 2.
Idziemy wskaźnikiem słowa 2 aż wskaźniki będą pokazywać tą samą literę.
Przy okazji zliczamy na jakie litery natrafia wskaźnik 2 w swojej drodze.
Kiedy już znaleźliśmy miejsce gdzie wskaźnik 1 == wskaźnik 2 to wiemy na pewno jakie jest najmniejsze możliwe k bo
przynajmniej tyle musieliśmy przebyć. Teraz idziemy wskaźnikiem 1 odejmując od naszej tabeli liczników.
Ponieważ te liczby były w zakresie który przebyliśmy już to na pewno nie są oddalone bardziej niż to k które
wcześniej przebyliśmy. Robimy tak do momentu aż litera na którą natrafiliśmy wskaźnikiem 1 ma w liczniku 0.
Zaczynamy cykl od nowa i powtarzamy aż oba wskźniki będą na końcu stringów. Całość w O(n) 
"""


def tanagram(A: str, B: str, t: int) -> bool:
    n = len(A)
    if len(B) != n:
        return False
    CA = [0 for _ in range(26)]
    CB = [0 for _ in range(26)]
    for x in range(n):
        CA[ord(A[x])-97] += 1
        CB[ord(B[x])-97] += 1
    for x in range(26):
        if CA[x] != CB[x]:
            return False
    i = 0
    j = 0


if __name__ == "__main__":
    print(tanagram("kotomysz", "tokmysoz", 3))
    print(tanagram("kotomysz", "tokmysoz", 2))