"""
Tworzymy dwie zmienne liczbowe j i c które przechowują godzinę zakończenia aktualnie wykonywanej czynności.
Z posortowanej (po godzinach rozpoczęcia) listy czynności bierzemy pokolei obiekty i przydzielamy rodzicowi którego
aktualna czynność kończy się wcześniej niż zaczyna nowa. Jeżeli żaden rodzic nie jest wtedy wolny to IMPOSSIBLE.

Złożoność obliczeniowa: O(nlogn) - posortowanie i przejście liniowo po tablicy
Złożoność pamięciowa: O(1)
"""


def opieka(T: list[tuple[int, int]]) -> str:
    for x in range(len(T)):
        T[x] = (T[x][0], T[x][1], x)
    s = [" " for _ in range(len(T))]
    j = 0
    c = 0
    T = sorted(T, key=lambda x: x[0])
    for x in T:
        if j <= x[0]:
            s[x[2]] = "J"
            j = x[1]
        elif c <= x[0]:
            s[x[2]] = "C"
            c = x[1]
        else:
            return "IMPOSSIBLE"
    return "".join(s)


if __name__ == "__main__":
    T = [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]
    print(opieka(T))
